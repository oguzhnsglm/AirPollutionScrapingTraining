AirPollutionScrapingTraining

Project Overview

This project involves web scraping and machine learning for analyzing air pollution data. The data is collected from an online source, preprocessed, and used to build a predictive model. The primary goal is to predict PM10 (\u00b5g/m\u00b3) values using other air quality parameters as features.

Features of the Project

1. Web Scraping

Library Used: selenium with undetected_chromedriver

Scraped Parameters:

PM10 (\u00b5g/m\u00b3)

PM2.5 (\u00b5g/m\u00b3)

SO2 (\u00b5g/m\u00b3)

CO (\u00b5g/m\u00b3)

NO2 (\u00b5g/m\u00b3)

NOX (\u00b5g/m\u00b3)

NO (\u00b5g/m\u00b3)

Source: sim.csb.gov.tr

Steps in Web Scraping:

Select city (e.g., İstanbul).

Configure date ranges and data parameters.

Extract data dynamically for all districts.

Parse tabular data into a structured DataFrame.

2. Data Preprocessing

Handled Missing Values:

Imputed missing data using mean or median values based on feature distribution.

Outlier Removal:

Identified and removed outliers using statistical thresholds (e.g., Z-scores).

Feature Selection:

Selected relevant features based on correlation analysis.

3. Machine Learning Pipeline

Target Variable:

PM10 (\u00b5g/m\u00b3)

Features:

PM2.5, SO2, CO, NO2, NOX, NO

Model Used:

Support Vector Regressor (SVR)

Model Performance:

Best R-squared Score: 0.1286

Hyperparameter Tuning:

Optimized SVR parameters using grid search for kernel and regularization values.

File Structure

AirPollutionScrapingTraining/
│
├── data/                 # Raw and processed data
│   ├── raw/              # Original scraped data
│   └── processed/        # Cleaned and preprocessed data
│
├── notebooks/            # Jupyter Notebook files
│   ├── scraping.ipynb    # Web scraping workflow
│   └── modeling.ipynb    # Machine learning pipeline
│
├── src/                  # Source code
│   ├── scraper.py        # Web scraping script
│   ├── preprocess.py     # Data preprocessing script
│   └── train_model.py    # Model training and evaluation
│
├── models/               # Saved machine learning models
│   └── svr_model.pkl     # Best SVR model
│
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies

Results

Model Performance

Best Model: Support Vector Regressor (SVR)

R-squared Score: 0.1286

Insights

Feature Importance:

Strong correlation between PM10 and PM2.5, NOX

SO2 and CO contribute less but are still relevant.

Web Scraping Outcome: Successfully extracted district-wise air pollution data for Ankara, covering multiple parameters across various time frames.

How to Use the Project

Prerequisites

Python 3.8+

Steps to Run

Web Scraping:

Execute the scraper script to fetch data:

python src/veri.py

Preprocessing:

Preprocess and train the data to handle missing values and outliers:

python src/app.py

Results:

View results and save the model in the models/ directory.

Future Enhancements

Expand scraping to multiple cities and time frames.

Include additional machine learning models for comparison.

Visualize data trends and model predictions interactively.

Demonstration

A detailed demonstration of the project's functionality, including web scraping and data preprocessing, is available on YouTube: Watch Here.

Acknowledgments

Data Source: Ministry of Environment, Urbanization, and Climate Change (sim.csb.gov.tr)

Libraries: Selenium, Pandas, Scikit-learn, Undetected ChromeDriver

Feel free to contribute to this project or use it for educational purposes!

