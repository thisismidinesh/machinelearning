# SpecKit User Rules for Machine Learning Project

## Project Overview
This is a Python-based machine learning project. All code should follow best practices for ML development.

## Python Version
- Use Python 3.8 or higher
- Ensure compatibility with the specified version

## Dependencies
- Use `requirements.txt` for dependencies
- Preferred libraries:
  - pandas for data manipulation
  - numpy for numerical computations
  - scikit-learn for ML algorithms
  - matplotlib/seaborn for visualization
  - jupyter for notebooks
- Pin versions in requirements.txt

## Code Style
- Follow PEP 8 style guide
- Use type hints where possible
- Write docstrings for functions and classes
- Use meaningful variable and function names

## Project Structure
- `src/` for source code
- `data/` for datasets (add to .gitignore)
- `notebooks/` for Jupyter notebooks
- `models/` for saved models
- `tests/` for unit tests
- `docs/` for documentation

## Data Handling
- Validate data inputs
- Handle missing values appropriately
- Split data into train/validation/test sets
- Use stratified splits for classification

## Model Development
- Use cross-validation for model evaluation
- Log experiments with parameters and results
- Save models in pickle or joblib format
- Document model performance metrics

## Version Control
- Use Git for version control
- Commit frequently with descriptive messages
- Use branches for features
- Ignore data files and models in .gitignore

## Testing
- Write unit tests for utility functions
- Test data preprocessing pipelines
- Validate model loading and prediction

## Documentation
- Maintain a README.md with setup instructions
- Document API if applicable
- Use comments in code for complex logic

## Security
- Do not commit sensitive data (API keys, passwords)
- Use environment variables for secrets
- Validate inputs to prevent injection attacks

## Performance
- Optimize code for memory and speed
- Use vectorized operations in pandas/numpy
- Profile code if performance issues arise

## Ethics
- Ensure fair and unbiased models
- Document potential biases
- Respect data privacy