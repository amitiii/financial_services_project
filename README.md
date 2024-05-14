SEC Filings Downloader

Overview
This Python script utilizes the `sec_edgar_downloader` library to download 10-K filings from the U.S. Securities and Exchange Commission (SEC) database for a specified company ticker symbol.

 Requirements
- Python 3.x
- `sec_edgar_downloader` library

 Installation
1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install the `sec_edgar_downloader` library using pip:
    ```
    pip install sec_edgar_downloader
    ```

 Usage
1. Run the script `sec_filings_downloader.py`.
2. Enter the company ticker symbol when prompted.
3. The script will download 10-K filings for the specified company for each year from 1995 to 2023.
4. Filings will be saved to the current directory.

 Notes
- Ensure the company ticker symbol is accurate to retrieve the correct filings.
- If interrupted, the script can be resumed from where it left off.
- Customize the script as needed for specific requirements or additional functionality.
