import requests
from bs4 import BeautifulSoup
from datetime import datetime

class CryptoPriceScraper:
    def __init__(self, coin="bitcoin"):
        """
        Initialize the scraper with a specific cryptocurrency.
        
        :param coin: Name of the cryptocurrency to track (default is bitcoin)
        """
        self.coin = coin
        self.base_url = "https://www.google.com/search?q="
        self.price = None
        self.last_updated = None

    def fetch_price(self):
        """
        Fetch the current price of the cryptocurrency from Google search.
        
        :return: Current price as a string
        """
        try:
            # Construct the full URL
            search_url = f"{self.base_url}{self.coin} price"
            
            # Send GET request
            response = requests.get(search_url)
            
            # Parse the content
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the price element
            price_element = soup.find('div', attrs={
                'class': 'BNeawe iBp4i AP7Wnd'
            })
            
            # Update price and timestamp
            if price_element:
                self.price = price_element.text
                self.last_updated = datetime.now()
                return self.price
            else:
                raise ValueError("Price element not found")
        
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None

    def get_current_price(self):
        """
        Get the current price, fetching if not already fetched.
        
        :return: Current price as a string
        """
        if not self.price:
            self.fetch_price()
        return self.price

    def __str__(self):
        """
        String representation of the current cryptocurrency price.
        
        :return: Formatted string with coin name and price
        """
        if self.price:
            return f"{self.coin.capitalize()} Price: {self.price} (Updated: {self.last_updated})"
        return f"No price data for {self.coin}"

# Example usage
def main():
    # Create a scraper for Bitcoin
    bitcoin_scraper = CryptoPriceScraper("bitcoin")
    
    # Fetch and print the price
    print(bitcoin_scraper.get_current_price())
    
    # Print the full string representation
    print(bitcoin_scraper)

    # You can also create scrapers for other cryptocurrencies
    ethereum_scraper = CryptoPriceScraper("ethereum")
    print(ethereum_scraper.get_current_price())

if __name__ == "__main__":
    main()
