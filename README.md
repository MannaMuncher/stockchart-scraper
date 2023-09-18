# Stock Chart Screenshot Script

This script uses Selenium to automate the process of navigating to https://stockcharts.com/, searching for a given stock ticker, setting specific overlay and indicator settings, and capturing a screenshot of the resulting chart. The captured image is then inverted and displayed.

## Dependencies:

1. Selenium: This is required to automate the web browser.
2. Pillow (PIL): This is required to process the image.
3. Firefox Webdriver: The script uses Firefox's headless mode to navigate the web.

## Setup:

1. Install the required packages:
   ```bash
   pip install selenium pillow
   ```

2. Download the appropriate [geckodriver](https://github.com/mozilla/geckodriver/releases) for your platform and ensure it's in your PATH. This allows Selenium to interface with the Firefox browser.

## Usage:

1. By default, the script is set up to search for the stock ticker "WEAT". If you'd like to search for a different stock, change the value of the `stock_ticker` variable.

2. Run the script:
   ```bash
   python main.py
   ```

3. The script will navigate to the website, apply the specified overlay and indicator settings, and then capture a screenshot of the stock chart.

4. The captured screenshot is saved with a naming pattern: `StockChart_<TICKER>_<TIMESTAMP>.png`. For instance, if you searched for "WEAT" and ran the script on January 1, 2023 at 15:00:00, the filename would be `StockChart_WEAT_20230101-150000.png`.

5. The image is inverted (as a demonstration of image processing capabilities) and displayed.

## Points to Note:

- The script has a few hardcoded `time.sleep()` calls. This is to ensure the web page has enough time to load the required content. Adjusting these values might be necessary depending on your internet connection speed.
  
- You might need to update the CSS selectors in case the structure of the website changes in the future.

## License:

This script is provided without any warranties. Use at your own risk.
