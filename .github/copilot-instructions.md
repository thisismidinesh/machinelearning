# Project Guidelines

## Code Style
Follow PEP 8 with type hints and docstrings for all functions. Reference [.speckit/rules.md](.speckit/rules.md) for detailed standards. Use meaningful variable names and consistent indentation.

## Architecture
This is a notebook-driven ML project with a sequential workflow: exploration → preprocessing → training → evaluation → visualization. Notebooks in `notebooks/` must be executed in order (01-05). Use `utils/utils.py` for shared functions. Data flows from `data/raw/` (immutable) to `data/processed/`, models saved in `models/`.

## Build and Test
Install dependencies: `pip install -r requirements.txt`. No automated tests yet—create unit tests in `tests/` for utilities and pipelines.

## Conventions
- Data: Validate inputs, handle missing values, use stratified splits for classification
- Models: Always use cross-validation, save with joblib, document metrics
- Version control: Frequent commits, ignore data files and models in .gitignore
- No sensitive data: Use environment variables for secrets