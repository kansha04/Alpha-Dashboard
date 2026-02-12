# 📈 Alpha Dashboard

**A quantitative finance tool built to fetch, analyze, and visualize real-time stock market data.**

## 🚀 About the Project
Alpha Dashboard is a Python-based application designed to assist in financial analysis. It interfaces with market data APIs to retrieve real-time pricing information, logs your searches, and provides visual insights.

**Current Capabilities:**
* User-friendly CLI (Command Line Interface) for ticker input.
* Real-time data fetching using the `yfinance` library.
* Automatic logging of searched tickers to `stock_log.csv`.
* Basic statistical analysis and visualization of tracked stocks.
* Jupyter Notebook integration for interactive analysis.

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Libraries:** 
    * `yfinance` - Real-time market data
    * `pandas` - Data manipulation and analysis
    * `matplotlib` - Data visualization

## 📂 Project Structure
```text
.
├── dashboard.ipynb      # Interactive dashboard notebook
├── graph.py             # Script for visualizing graphs with matplotlib
├── main.py              # Main entry point (CLI)
└── README.md        # Project Documantation
```

## 💻 Getting Started

### Prerequisites
Make sure you have Python installed on your machine. You will also need the following libraries:
```bash
pip install yfinance pandas matplotlib
```

### Installation
1.  Clone the repository:
    ```bash
    git clone https://github.com/kansha04/alpha-dashboard.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd "Alpha Dashboard"
    ```

## 🏃 Usage

### 1. Main Application
Run the main script to fetch real-time prices. Your results will be saved to `stock_log.csv`.
```bash
python main.py
```
*   Enter a stock ticker (e.g., `AAPL` or `BTC-USD`) when prompted.
*   Type `EXIT` or `Q` to quit and see your session history.

### 2. Data Analysis
To see a summary of the data stored in `stock_log.csv`:
```bash
python analysis.py
```

### 3. Visualization
To generate a bar chart of the top 5 highest-priced stocks in your log:
```bash
python graph.py
```

### 4. Interactive Notebooks
Open `dashboard.ipynb` in a Jupyter environment (like VS Code or JupyterLab) for an interactive experience.

## 🧪 Testing
- [TODO] Implement automated unit tests for data fetching and processing.

## 🔐 Environment Variables
- [TODO] Add support for API keys if moving beyond free-tier `yfinance` data.

## 📜 License
- [TODO] Specify license (e.g., MIT).

---
Created by Tinovonga Mushayi - Class of 2027