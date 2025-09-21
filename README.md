# Autonomize QA Assignment  

This repository contains automation test suites for **UI Testing** and **API Testing** using **Pytest**.  


## Setup Instructions

1. **Download the repository to a local folder.**

2. **Install Python**

3. **Create & activate virtual environment**  
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

4. **Install dependencies**  
   pip install -r requirements.txt

5. **Directory Structure (example)**  
   ├── data/               # Logs & Excel files
   ├── tests/
   │   ├── ui/
   │   │   ├── test_login.py
   │   ├── api/
   │   │   ├── test_users_crud.py
   │   ├── features/
   │   │   ├── apiCRUD.feature
   │   │   ├── productList.feature
   |   |
   ├── pages/              # Page Object files (for UI)
   ├── utils/              # Helpers (e.g. excelReadWrite, Selenium helpers)
   ├── conftest.py         # Fixtures, logger
   ├── config.ini          # URLs
   ├── requirements.txt    # Dependencies
   ├── README.md           # Documentation
   ├── reports/            # Test reports (auto-generated)

## Running Tests  

1. Ensure you have **Google Chrome** installed.

2. Run tests:  
   pytest -v -s --html=reports/report.html --self-contained-html

- Product details are saved under the `data/` folder.
- To view the details, open the generated `.xlsx` file.

## Generating & Viewing Reports  

We use **pytest-html** for reporting.  

- Reports are saved under the `reports/` folder.  
- To view a report, open the generated `.html` file in any browser.  

This framework supports **UI tests**, **API tests**, and **HTML reports**, making it easy to run, analyze, and share results.

**Note - As mentioned in the DummyJSON API documenation for Add User action the API will not add it into the server. So, update, get and delete API tests will fail.** 
