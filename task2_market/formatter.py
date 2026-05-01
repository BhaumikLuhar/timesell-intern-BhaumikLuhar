from tabulate import tabulate


def print_price_table(results: list):
    """
    Prints formatted table of asset prices
    """
    if not results:
        print("No data to display.")
        return

    table_data = []

    for r in results:
        table_data.append([
            r["asset"],
            f"{r['price']:.2f}",
            r["currency"],
            r["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        ])

    headers = ["Asset", "Price", "Currency", "Timestamp"]

    print("\nAsset Prices\n")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))