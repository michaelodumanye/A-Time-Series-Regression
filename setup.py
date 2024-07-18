from setuptools import setup, find_packages

setup(
    name='time_series_regression',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyodbc',
        'python-dotenv',
        'pandas',
        'numpy',
        'scipy',
        'seaborn',
        'matplotlib',
        'plotly',
        'scikit-learn',
        'xgboost',
        'statsmodels',
        'calplot',
        'catboost'
    ],
)
