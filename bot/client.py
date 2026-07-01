from binance.client import Client
from dotenv import load_dotenv
import os

load_dotenv()

class BinanceFuturesClient:
    """Elegant Binance Futures Testnet Client."""
    
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not api_key or not api_secret:
            raise ValueError("❌ Missing API credentials in .env file")
        
        self.client = Client(api_key, api_secret, testnet=True)
        print("✅ Connected successfully to Binance Futures Testnet")

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """Place order with rich response handling."""
        try:
            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": str(quantity)
            }
            
            if order_type.upper() == "LIMIT":
                params.update({
                    "price": str(price),
                    "timeInForce": "GTC"
                })

            order = self.client.futures_create_order(**params)
            print("🎉 Order executed successfully!")
            return order
            
        except Exception as e:
            print(f"❌ Failed to place order: {e}")
            raise
