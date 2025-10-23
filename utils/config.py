#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/10/23 16:53
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   config.py
# @Desc     :   

from dataclasses import dataclass, field
from pathlib import Path
from torch import cuda

# Set base directory
BASE_DIR = Path(__file__).resolve().parent.parent


@dataclass
class FilePaths:
    SAVED_MODEL: Path = BASE_DIR / "models/model.pth"
    PAPER = BASE_DIR / "data/Pride_and_Prejudice.txt"


@dataclass
class DataPreprocessor:
    RANDOM_STATE: int = 27
    VALID_SIZE: float = 0.2
    IS_SHUFFLE: bool = True
    PCA_VARIANCE_THRESHOLD: float = 0.95
    BATCH_SIZE: int = 32


@dataclass
class ModelParameters:
    RNN_SEQUENTIAL_LENGTH: int = 12
    RNN_EMBEDDING_DIM: int = 256
    RNN_HIDDEN_SIZE: int = 512
    RNN_LAYERS: int = 2


@dataclass
class Hyperparameters:
    ALPHA: float = 1e-3
    ALPHA_REDUCTION: float = 0.3
    EPOCHS: int = 20
    ACCELERATOR: str = "cuda" if cuda.is_available() else "cpu"


@dataclass
class Configration:
    FILEPATHS: FilePaths = field(default_factory=FilePaths)
    PREPROCESSOR: DataPreprocessor = field(default_factory=DataPreprocessor)
    PARAMETERS: ModelParameters = field(default_factory=ModelParameters)
    HYPERPARAMETERS: Hyperparameters = field(default_factory=Hyperparameters)


# Singleton instance of Config
CONFIG = Configration()
