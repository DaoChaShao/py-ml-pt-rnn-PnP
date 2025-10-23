<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com///compare/e542837ade41979f69f79358c5b882d0e76f495c...0.1.0) (2025-10-23)

### Features

- add TorchTrainer class for training and validation of neural networks ([dd6ff4a](https://github.com///commit/dd6ff4ae3842515d083e60a44c487ec20d96a4b4))
- add stopwords list for text processing ([616e7a6](https://github.com///commit/616e7a630f2099488699527b7cbdbf8531ba6018))
- add SpaCy NLP processor for tokenization and lemmatization of English text ([d46f5e9](https://github.com///commit/d46f5e9397cad0dfd1ed2923c9df94131006bf22))
- add functions to filter and tokenize English words in text ([9ba0f09](https://github.com///commit/9ba0f0985e7ad7c7fa1033d4f20782670cf2ec49))
- implement character-level RNN model in PyTorch ([4ec3a77](https://github.com///commit/4ec3a7714add5279295c66919a7672712d7b0ead))
- save a rnn model.pth parameters ([b7649ce](https://github.com///commit/b7649ce9b4e6d4600a8041cb0a68722e022182a4))
- implement data preprocessing and preparation for training ([32f67ba](https://github.com///commit/32f67ba3531bc5a56e1826e6c84386ee69a5743b))
- add save_json function to serialize dictionary data to JSON file ([7e05d4e](https://github.com///commit/7e05d4ecd1b827d97b1c2146be41a175a619fc2c))
- save a dictionary.json as word2id ([b24a1d2](https://github.com///commit/b24a1d2b1a6c3779fa9fc9efa1533f6b882d6df1))
- enhance Timer decorator to include a description parameter ([a2eb8fb](https://github.com///commit/a2eb8fb1bebaee9d4457ed534a6ce6f7ab68a5cd))
- update file paths in config.py for model, stopwords, and dictionary ([e263afc](https://github.com///commit/e263afc32c5dafa6231566f7a4775d52b96ee0b9))
- add BSD 3-Clause License file ([bd1edff](https://github.com///commit/bd1edff2789ed55b7df2b3f43d66ee88d8f351f3))
- add uv sync file uv.lock ([70b094b](https://github.com///commit/70b094b5b79c2d90a9f544d42ca4e9b0f7e1be77))
- add THULAC text segmentation functions for word cutting with and without POS tags ([4b46ef5](https://github.com///commit/4b46ef58ee5f8a248ed03ca13c3d2853abce17ab))
- add data processing functions including random seed management, data loading, preprocessing, and PCA feature importance ([0be27d1](https://github.com///commit/0be27d1312008b08678f56f11cd0487d2391f3e7))
- update Chinese README to include Stanza and spaCy as additional text processing tools ([6eb0c72](https://github.com///commit/6eb0c7218f4efc7b53c9e65bafd0135cdfcba6a8))
- update README to include Stanza and spaCy as additional text processing tools ([79574a3](https://github.com///commit/79574a3280fa0ba739fb56c6240dc5ef46d4a829))
- update dependencies in pyproject.toml for enhanced functionality and performance ([f69379d](https://github.com///commit/f69379d3543647245afed997e889bf5ee600d602))
- add custom PyTorch classes for random seed management, dataset handling, and device checking ([cad9eba](https://github.com///commit/cad9eba259b8b941a809ccc1f9b9ddc2f7c00f9c))
- add an English article as data ([9debb01](https://github.com///commit/9debb01722a5dcd98407582d3ed2b1c3bf1e00c2))
- add Outputter class for controlled message printing ([c5b5ed9](https://github.com///commit/c5b5ed9f608c4fed790c2dc487e46f4ebd47e188))
- add functions for Chinese text processing and analysis with performance tracking ([32d1aab](https://github.com///commit/32d1aab755bb175974af076494308d28279124d2))
- implement main function placeholder for future development ([fb6d19c](https://github.com///commit/fb6d19cb9eebe4539cae5031a2e0c2444df7660c))
- add jieba text processing functions with performance tracking ([783751c](https://github.com///commit/783751cf24f3acccb500f1165536114ed043b5e7))
- add text highlighting and formatting functions for improved output presentation ([ee2e97d](https://github.com///commit/ee2e97d4292ca839bbeb0ae3e898d776142bf79c))
- add Timer, Beautifier, and RandomSeed context managers for enhanced code performance and readability ([dc3ca40](https://github.com///commit/dc3ca405ec53160ff5a0d11194132d4ca7b0855c))
- add timer and beautifier decorators for function performance tracking ([f79df6d](https://github.com///commit/f79df6d2bce73cb64d1802b86092d9869230d713))
- implement log_mse_loss function for regression tasks ([df212fe](https://github.com///commit/df212febada96c9d2edb2088422249612de26766))
- add configuration classes for file paths, data preprocessing, model parameters, and hyperparameters ([a948ff3](https://github.com///commit/a948ff32ea76340fd7b4614c069a9f01fa75314e))
- create OUT.py with initial metadata and encoding declaration ([e907c17](https://github.com///commit/e907c17ddffcc4960a44699b9efeb2d0c7970be9))

### Bug Fixes

- remove unused main function from THU.py ([7e5daa8](https://github.com///commit/7e5daa842046fecc4652ceb0726b086f747b28b9))
- remove unused main function from stats.py ([92e1208](https://github.com///commit/92e1208845a26d33c8331ae94fd3b22b6a52a592))
- remove unused main function from PT.py ([197aa60](https://github.com///commit/197aa609532573dfaa0268dee3cf272eb44677b7))
- remove unused main function from nlp.py ([7c1d66e](https://github.com///commit/7c1d66ecd8a70c930c37c53f8790ff1e85fec064))
- remove unused main function from models.py ([784b001](https://github.com///commit/784b001aac9b1105cfa3574e6b5e70098f83fd7d))
- remove unused main function from main.py ([033a411](https://github.com///commit/033a41196e47d9afa5d51a261ebb38f41d577db7))
- remove unused main function from JB.py ([da95f26](https://github.com///commit/da95f260896b7eaafa2eb840ca84884d3e7ec582))
- remove unused main function from highlighter.py ([41185d1](https://github.com///commit/41185d1f548592cd658aecaaca2b7c65e99a537c))
- remove unused main function from helper.py ([390ec47](https://github.com///commit/390ec478ba7da0516bf2b4c6ae21def03769699c))
- remove unused main function from decorator.py ([0b5f446](https://github.com///commit/0b5f4468d535f2baf06209a46f39c495ae41031b))
- remove unused main function from criterion.py ([1466bcd](https://github.com///commit/1466bcd304528c522aa053ef75066d7ebfe0c6d7))
- remove unused main function and clean up config.py ([f3e1086](https://github.com///commit/f3e108636e9f9de22809686c2fd1b41b8d935a16))
- add missing newline at end of file and ensure main function is called ([a45690a](https://github.com///commit/a45690a36e8b8d2780c272fa1ef875b380a9de39))

### Chore

- update CHANGELOG.md to include BSD 3-Clause License addition ([8db137a](https://github.com///commit/8db137a92b0303c9601258baf38507e0d102a698))
- update CHANGELOG.md for version 0.1.0 with new features and improvements ([1a00a97](https://github.com///commit/1a00a97280435c7390864f4f90fc00628ad8f8bf))
- add CHANGELOG.md for version 0.0.1 with bug fixes and documentation updates ([3289cdc](https://github.com///commit/3289cdc9cb21e251b3a64464f75e9ab7d10de7a4))
- add git-changelog configuration to pyproject.toml ([437b03b](https://github.com///commit/437b03b9d2e5e6a0e197791c1671cd892380a477))
- add .gitignore to exclude Python-generated files and IDE configurations ([e1df047](https://github.com///commit/e1df047c36615889de09ce52a2c2e1e3b0ad528a))
- update .gitignore to exclude PyCharm files and virtual environment directories ([cb889ab](https://github.com///commit/cb889ab9d47cf345efd60c61955b730d7d475096))

### Docs

- add comprehensive project overview and environment setup instructions to README ([33a878a](https://github.com///commit/33a878a0bf4760a65e431e7d6f194f203cf8dda5))

### Code Refactoring

- comment out print statements for training and validation loss and accuracy ([045015b](https://github.com///commit/045015be92084d77ce51d8105b707ac8c8fad70f))
- rename methods and instance of Outputter for consistency ([66a0f9e](https://github.com///commit/66a0f9ebf8558460da84a4270905083ffcb3ded5))

