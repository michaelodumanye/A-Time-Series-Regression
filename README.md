# Time Series Regression Project

## Project Overview

This project aims to explore and implement various regression models to understand the relationship between dependent and independent variables. The ultimate goal is to develop models that can predict future outcomes based on historical data, with a special focus on time series analysis. The project encompasses data exploration, feature engineering, model development, evaluation, and optimization.

## Data Sources

### Database
We use a Microsoft SQL Server database containing the following tables:
- `dbo.oil`
- `dbo.holidays_events`
- `dbo.stores`

Database Credentials:
- **Server Name:** dap-projects-database.database.windows.net
- **User:** learning_project_3
- **Password:** A$uB1Lp3$2@24
- **Database Name:** dapDB

### OneDrive
Two CSV files relevant for testing the models:
- `sample_submission.csv`
- `test.csv`

### GitHub
A zip file containing additional data and project documentation:
- Link to the repository: [GitHub Repository](#)

## Project Structure

Time-Series-Regression/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ └── analysis.ipynb
│
├── src/
│
├── tests/
│
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py


### Folder Descriptions
- **data/raw/**: Contains raw data files.
- **data/processed/**: Contains processed data files.
- **notebooks/**: Contains Jupyter notebooks for analysis and model development.
- **src/**: Contains source code for data processing and model building.
- **tests/**: Contains test scripts.

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- Git LFS (Large File Storage)

### Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/time-series-regression.git
    cd time-series-regression
    ```

2. **Initialize Git LFS:**
    ```sh
    git lfs install
    git lfs pull
    ```

3. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required libraries:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Connecting to the Database
Refer to the `notebooks/analysis.ipynb` for instructions on how to connect to the database and load data using `pyodbc`.

### Running the Analysis
Open the `notebooks/analysis.ipynb` in Jupyter Notebook and follow the steps to explore, preprocess, and analyze the data.

### Adding New Features
You can add new features to the `src/` directory and test them using scripts in the `tests/` directory.

## Project Tasks

### Business Understanding & Data Preprocessing
- Understand the project objectives and requirements.
- Define business success criteria and data mining goals.
- Produce a detailed project plan.
- Preprocess the data, handle missing values, and perform feature engineering.

### Exploratory Data Analysis
- Conduct exploratory data analysis to understand the data distribution and identify patterns.
- Visualize the data to gain insights.

### Model Development
- Develop regression models including Linear Regression, XGBoost, ARIMA, and SARIMA.
- Train and evaluate the models using metrics such as RMSLE, RME, and MSE.

### Model Optimization
- Perform hyperparameter tuning to optimize model performance.

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) before submitting a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please contact [modumanye@gmail.com](modumanye@gmail.com).

