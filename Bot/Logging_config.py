import logging
import os
from datetime import datetime

def setup_logging() -> logging.Logger:
    """Initialize aesthetic logging for production use."""
    os.makedirs("logs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(message)s",
        datefmt="%H:%M:%S",
        handlers=[
            logging.FileHandler(f"logs/trading_bot_{timestamp}.log"),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger("TradingBot")
    logger.info("🚀 Binance Futures Testnet Trading Bot Started")
    return logger
