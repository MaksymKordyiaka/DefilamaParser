DefilamaParser Documentation
1. Set up the scraping environment
To set up the environment for running the DefilamaParser project, follow these steps:

Requirements:
Python (recommended version: 3.8 or higher)
pip (Python package installer)
Git (optional, for cloning the repository)


Steps to Set Up:
    1) Clone the Repository (Optional): If you haven’t already, clone the project from GitHub:

        >>> git clone https://github.com/MaksymKordyiaka/DefilamaParser.git
        >>> cd DefilamaParser

    2) Set up a Virtual Environment: It’s recommended to use a virtual environment to isolate dependencies for your project.

        >>> python -m venv .venv

    3) Activate the Virtual Environment:

        Windows:

            >>> .venv\Scripts\activate

        Linux/macOS:

            >>> source .venv/bin/activate

    4) Install Dependencies: Install the required dependencies from requirements.txt:

            >>> pip install -r requirements.txt

This will install the necessary libraries for running the scraper, such as selenium, proxy and others.



2. Configure proxy settings and intervals for data collection

Proxy Configuration
If you need to configure a proxy server for your scraper to run (for example, to avoid IP blocking or to scrape
anonymously), you can use the proxy settings in your script.

Steps to Set Up Proxy:

    1) Install Proxy Manager (if needed):

        Use a proxy service like ProxyMesh or ScraperAPI.
        Alternatively, you can configure your local proxy using the proxy package.

    2) Configure the Proxy:

       >>> proxy (default http://127.0.0.1:8899)
         or
       >>> proxy --hostname 127.0.0.1 --port 9000 (You can set the proxy for your scraper by running the following command
       in the terminal (substitute localhost and 9000 with your proxy settings if necessary))

    3) Set Up Scraping Interval: Scraping too frequently can result in blocking or banning. You can set the interval between
    data collection. For example, if you want the scraper to run every 5 minutes, you can set the interval:

    config.json:

        {
            "scrape_interval_minutes": 5, (5 minutes)
            ...
        }

You can adjust this value in your script according to your needs.



3. Execute the Script
Running the Scraper Script:

    1) Create Virtual Environment (if not created):

        >>> python -m venv .venv

    2) Activate the Virtual Environment (if not already activated):

        >>> .venv\Scripts\activate  # For Windows
          or
        >>> source .venv/bin/activate  # For Linux/macOS

    3) Run the Scraper Script: To start scraping data from the website, run the following command:

        >>> python scraper.py

        The script will start scraping the data according to the defined parameters and intervals.

    4) Output: Once the script is finished scraping, it will output the results (e.g., saved to a file or printed to the console).



4. Submit Your Python Script Along with the Documentation. Include examples of the data extracted.

blockchain_data.json:

[
    {
        "Name": "Ethereum",
        "Protocols": "1210",
        "TVL": "$54,965b"
    },
    {
        "Name": "Solana",
        "Protocols": "173",
        "TVL": "$7,031b"
    },
    {
        "Name": "Tron",
        "Protocols": "34",
        "TVL": "$6,74b"
    },
    {
        "Name": "BSC",
        "Protocols": "808",
        "TVL": "$4,756b"
    },
    {
        "Name": "Bitcoin",
        "Protocols": "42",
        "TVL": "$3,045b"
    },
    {
        "Name": "Base",
        "Protocols": "380",
        "TVL": "$2,807b"
    },
    {
        "Name": "Arbitrum",
        "Protocols": "722",
        "TVL": "$2,589b"
    },
    {
        "Name": "Sui",
        "Protocols": "43",
        "TVL": "$1,101b"
    },
    {
        "Name": "Avalanche",
        "Protocols": "410",
        "TVL": "$1,095b"
    },
    {
        "Name": "Polygon",
        "Protocols": "581",
        "TVL": "$1,085b"
    },
    {
        "Name": "Hyperliquid",
        "Protocols": "3",
        "TVL": "$954,52m"
    },
    {
        "Name": "Aptos",
        "Protocols": "49",
        "TVL": "$896,51m"
    }
]

