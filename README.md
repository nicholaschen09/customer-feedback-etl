# Customer Feedback ETL Pipeline

This project focuses on the aggregation and analysis of customer feedback using an ETL (Extract, Transform, Load) pipeline. The goal is to collect feedback from various sources, process it, and generate insights that can help improve customer satisfaction.

## Project Structure

```
customer-feedback-etl
├── data
│   ├── raw
│   │   └── customer-feedback.csv  # Raw customer feedback data
│   ├── processed                   # Directory for cleaned and transformed data
│   └── output                      # Directory for final output data and insights
├── src
│   ├── extract.py                  # Functions to extract data from various sources
│   ├── transform.py                # Functions for data cleaning and transformation
│   ├── load.py                     # Functions to load processed data into storage
│   └── main.py                     # Entry point for the ETL pipeline
├── requirements.txt                # List of project dependencies
├── README.md                       # Project documentation
└── .gitignore                      # Files and directories to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd customer-feedback-etl
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Place your raw customer feedback data in the `data/raw` directory. Ensure the file is named `customer-feedback.csv` and follows the required format (it should include columns like `Timestamp`, `User`, and `Tweet`).
2. Make sure you `cd customer-feedback-etl/src` to run the program
3. Activate the virtual environment: `source venv/bin/activate` and `pip install pandas` and then run `python3 main.py`
4. The processed data will be saved in the `data/processed` directory once the etl pipeline is done running.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
