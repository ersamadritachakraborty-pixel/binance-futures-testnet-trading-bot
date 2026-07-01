import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print as rprint

from bot.client import BinanceFuturesClient
from bot.validators import validate_order
from bot.logging_config import setup_logging

console = Console()
logger = setup_logging()

def main():
    parser = argparse.ArgumentParser(
        description="🚀 Binance Futures Testnet Trading Bot",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Built for Primetrade.ai Python Developer Internship"
    )
    
    parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order direction")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--price", type=float, help="Price (required for LIMIT orders)")
    
    args = parser.parse_args()
    
    try:
        validate_order(args.symbol, args.side, args.type, args.quantity, args.price)
        
        console.print(Panel.fit("[bold cyan]🚀 Binance Futures Testnet Trading Bot[/bold cyan]", border_style="blue"))
        
        client = BinanceFuturesClient()
        logger.info(f"Placing {args.type} {args.side} order → {args.quantity} {args.symbol}")
        
        order = client.place_order(
            args.symbol, args.side, args.type, args.quantity, args.price
        )
        
        # Premium Summary Table
        table = Table(title="📊 Order Execution Summary", style="green", title_style="bold magenta")
        table.add_column("Parameter", style="cyan", no_wrap=True)
        table.add_column("Value", style="green")
        
        table.add_row("Symbol", f"[bold]{args.symbol}[/bold]")
        table.add_row("Side", args.side)
        table.add_row("Type", args.type)
        table.add_row("Quantity", str(args.quantity))
        if args.price:
            table.add_row("Limit Price", str(args.price))
        table.add_row("Order ID", str(order.get('orderId')))
        table.add_row("Status", f"[bold green]{order.get('status', 'FILLED')}[/bold green]")
        
        console.print(table)
        rprint("\n[bold green]✅ Order Successfully Placed on Testnet![/bold green]")
        
        logger.info(f"✅ Success → Order ID: {order.get('orderId')}")
        
    except ValueError as ve:
        console.print(f"[bold red]❌ Validation Error:[/bold red] {ve}")
        logger.error(f"Validation Error: {ve}")
    except Exception as e:
        console.print(f"[bold red]💥 Critical Error:[/bold red] {e}")
        logger.error(f"Critical Error: {e}")

if __name__ == "__main__":
    main()
