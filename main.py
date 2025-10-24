#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/23 16:48
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :

from random import randint
from torch import nn, optim

from utils.config import CONFIG
from utils.helper import read_file, save_json, Timer
from utils.models import CharsRNNTorchModel
from utils.nlp import (snlp_analysis,
                       regular_english,
                       count_words_frequency)
from utils.OUT import out
from utils.PT import (SequentialTorchDataset, TorchDataLoader,
                      TorchRandomSeed)
from utils.trainer import TorchTrainer

out.yes()


def preprocess_data():
    # Read raw data
    raw = read_file(CONFIG.FILEPATHS.PAPER)

    # Tokenise the raw text
    # words = tokenize_english(raw)  # words: 130408
    words = snlp_analysis(raw)  # words: 155383
    # print(words)

    # Filter the words to retain only English words
    filtered = regular_english(words)  # words: 108823
    # print(filtered)

    # Set up the special tokens
    tokens: list[str] = ["<PAD>", "<UNK>"]

    # Get word frequency
    frequency, _ = count_words_frequency(filtered)
    # print(len(frequency), frequency[:20])
    vocabs: list[str] = tokens + frequency
    # Build unique vocabulary list based on frequency order - word2id
    dictionary: dict[str, int] = {word: idx for idx, word in enumerate(vocabs)}
    save_json(dictionary, CONFIG.FILEPATHS.DICTIONARY)
    # print(dictionary)

    # Build text sequences
    sequences: list[int] = []
    for word in filtered:
        word_index = dictionary[word]
        sequences.append(word_index)
    # print(sequences)

    return vocabs, dictionary, sequences


def prepare_data():
    _, dictionary, sequences = preprocess_data()

    dataset = SequentialTorchDataset(
        sequences,
        CONFIG.PARAMETERS.RNN_SEQUENTIAL_LENGTH,
        dictionary["<PAD>"],
    )

    loader = TorchDataLoader(dataset, CONFIG.PREPROCESSOR.BATCH_SIZE)

    return dictionary, loader


def main() -> None:
    """ Main Function """
    with Timer("Get Data for Training"):
        dictionary, loader = prepare_data()
        index: int = randint(0, len(dictionary) - 1)
        print(loader[index])

    with TorchRandomSeed("Sequential Data Training"):
        # Setup rnn model
        model = CharsRNNTorchModel(
            vocab_size=len(dictionary),
            embedding_dim=CONFIG.PARAMETERS.RNN_EMBEDDING_DIM,
            hidden_size=CONFIG.PARAMETERS.RNN_HIDDEN_SIZE,
            num_layers=CONFIG.PARAMETERS.RNN_LAYERS,
        )
        # Setup optimizer and loss function
        optimizer = optim.Adam(model.parameters(), lr=CONFIG.HYPERPARAMETERS.ALPHA)
        criterion = nn.CrossEntropyLoss()

        # training loop
        trainer = TorchTrainer(model, optimizer, criterion, CONFIG.HYPERPARAMETERS.ACCELERATOR)
        trainer.fit(
            loader,
            loader,
            CONFIG.HYPERPARAMETERS.EPOCHS,
            str(CONFIG.FILEPATHS.MODEL),
        )


if __name__ == "__main__":
    main()
