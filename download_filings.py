from sec_edgar_downloader import Downloader

# Define the company ticker symbol (ticker) provided by the user
company_ticker = input("Enter the company ticker symbol: ")

# Initialize a downloader instance with the company name and email address
dl = Downloader("Financial Services Project", "amiti94799@gmail.com")

try:
    # Loop through each year to download 10-K filings for the specified company ticker
    for year in range(1995, 2024):
        try:
            # Download 10-K filings for the specified company ticker and year
            dl.get("10-K", company_ticker)
            print(f"Downloaded 10-K filing for {company_ticker} in {year}")
        except Exception as e:
            print(f"Error downloading 10-K filing for {company_ticker} in {year} - {e}")
except KeyboardInterrupt:
    print("\nDownload interrupted by user.")


