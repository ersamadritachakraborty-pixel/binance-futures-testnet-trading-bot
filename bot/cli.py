import argparse
from bot.client import BinanceFuturesClient
from bot.validators import validate_order
from bot.logging_config import setup_logging

logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(
        description="🚀 Binance Futures Testnet Trading Bot",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required only for LIMIT orders")
    
    args = parser.parse_args()
    
    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)
        
        client = BinanceFuturesClient()
        logger.info(f"Placing {args.type} {args.side} order for {args.quantity} {args.symbol}")
        
        order = client.place_order(
            args.symbol, args.side, args.type, args.quantity, args.price
        )
        
        print("\n" + "="*60)
        print("📊 ORDER SUMMARY")
        print("="*60)
        print(f"Symbol     : {args.symbol}")
        print(f"Side       : {args.side}")
        print(f"Type       : {args.type}")
        print(f"Quantity   : {args.quantity}")
        if args.price:
            print(f"Price      : {args.price}")
        print(f"Order ID   : {order.get('orderId')}")
        print("="*60)
        
        logger.info(f"✅ Success - Order ID: {order.get('orderId')}")
        
    except Exception as e:
        logger.error(f"💥 Error: {e}")

if __name__ == "__main__":
    main()
