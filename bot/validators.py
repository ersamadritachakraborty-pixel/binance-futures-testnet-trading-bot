def validate_order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Enterprise-grade input validation."""
    if not symbol or not symbol.endswith("USDT"):
        raise ValueError("❌ Symbol must be a valid USDT-M pair (e.g., BTCUSDT)")
    
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("❌ Side must be BUY or SELL")
    
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("❌ Order type must be MARKET or LIMIT")
    
    if quantity <= 0:
        raise ValueError("❌ Quantity must be greater than zero")
    
    if order_type.upper() == "LIMIT" and (not price or price <= 0):
        raise ValueError("❌ Price is required and must be positive for LIMIT orders")
    
    return True
