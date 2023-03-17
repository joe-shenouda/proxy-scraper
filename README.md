
 Proxy Scraper

Created by Joe Shenouda (www.shenouda.nl)

A lightweight, single-site focused proxy scraper tool that efficiently generates a `proxies.txt` file containing a list of proxy addresses. This tool is perfect for those who require a simple yet effective proxy scraper without any unnecessary overhead.

 Features

- Scrapes proxies from a single, targeted website
- Generates a `proxies.txt` file containing the scraped proxies
- Easy to use with minimal configuration required

 Requirements

- Python 3.x
- Elevated privileges (to create and modify the `proxies.txt` file)

 Dependencies

- BeautifulSoup4
- Requests

You can install these dependencies using `requirements.txt` by running `pip install -r requirements.txt`.

 Usage

 Installation

1. Clone the repository to your local machine:
git clone https://github.com/yourusername/proxy-scraper.git

2. Change the directory to the `proxy-scraper` folder:
cd proxy-scraper

3. (Optional) Create and activate a virtual environment to run the script in:
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux)

4. Install the required Python packages:
5. pip install -r requirements.txt

 Usage

1. Run the script with elevated privileges:

   - On Windows, open a command prompt or PowerShell window with "Run as Administrator" and navigate to the `proxy-scraper` folder.

   - On Linux, use `sudo` before the command or run the terminal as root.

2. Execute the `proxy_scraper.py` script: 

python proxy_scraper.py

3. The script will scrape proxies from the targeted website and save them to the `proxies.txt` file in the same directory.

 Customization

To target a different website for proxy scraping, modify the `proxy_scraper.py` script with the desired URL and parsing logic according to the new website's structure.

 License

This project is released under the MIT License. See the `LICENSE` file for more information.





