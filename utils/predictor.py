#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/24 21:01
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   predictor.py
# @Desc     :   

from pathlib import Path
from random import randint
from torch import (tensor, load,
                   Tensor, long,
                   softmax, multinomial)

from main import preprocess_data
from utils.config import CONFIG
from utils.helper import Timer
from utils.models import CharsRNNTorchModel


def main() -> None:
    """ Main Function """
    with Timer("Pride and Prejudice Prediction"):
        path = Path(CONFIG.FILEPATHS.MODEL)

        if path.exists():
            print("The model has already been trained and existed.\n")

            vocabs, dictionary, sequences = preprocess_data()
            # print(unique_chars)
            # print(dictionary)

            index = randint(0, len(vocabs) - 1)
            first_char: str = vocabs[index]
            print(first_char)
            first_index: int = dictionary[first_char]
            seq_len: int = CONFIG.PARAMETERS.RNN_SEQUENTIAL_LENGTH

            # Due to the saved model structure, we need to define the model architecture again
            model = CharsRNNTorchModel(
                vocab_size=len(vocabs),
                embedding_dim=CONFIG.PARAMETERS.RNN_EMBEDDING_DIM,
                hidden_size=CONFIG.PARAMETERS.RNN_HIDDEN_SIZE,
                num_layers=CONFIG.PARAMETERS.RNN_LAYERS,
            )
            state_dict = load(CONFIG.FILEPATHS.MODEL)
            model.load_state_dict(state_dict)
            model.eval()
            # print("The model has been loaded successfully!")
            print(model)

            # Generate predictions
            hx = None
            amount: int = randint(10, 21)
            print(amount)
            chars: list[str] = [first_char]
            padded = [dictionary["<PAD>"]] * (seq_len - 1) + [first_index]
            for i in range(amount):
                entry: Tensor = tensor([padded], dtype=long)

                predictions, _ = model(entry, hx)
                # print(predictions.shape)

                # Get the last time step's predictions, which means the next character prediction
                final_time_step = predictions[0, -1, :]

                # -------------------- Temperature Sampling --------------------
                # Scale the logits by temperature: 1.0 is default, 1.2 is more random, 0.8 is more conservative
                # temperature = 1.0
                scaled_logits = final_time_step / CONFIG.PARAMETERS.RNN_TEMPERATURE
                probs = softmax(scaled_logits, dim=-1)
                next_index = multinomial(probs, num_samples=1)
                # -------------------- End Temperature Sampling ----------------

                # -------------------- Greedy Sampling -------------------------
                # Get the probabilities distribution using softmax
                # probs = softmax(final_time_step, dim=-1)
                # Get the max probability index
                # _, next_index = probs.max(dim=-1)
                # -------------------- End Greedy Sampling ---------------------
                # print(probs)

                # print(next_index)
                next_char = vocabs[next_index.item()]
                # print(f"Step {i + 1}: Predicted next character: '{next_char}'")
                chars.append(next_char)

                # Update the entries tensor by appending the predicted character index and removing the first index
                padded = padded[1:] + [next_index.item()]

            print(f"Prediction outcome: {" ".join(chars)}")
        else:
            print("The model has not been trained.")


if __name__ == "__main__":
    main()
