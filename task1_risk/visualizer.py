def print_allocation_chart(assets: list):
    """
    Prints a simple CLI bar chart for asset allocations.
    """
    print("\nPortfolio Allocation:\n")

    for asset in assets:
        name = asset["name"]
        allocation = asset["allocation_pct"]

        bar_length = int(allocation / 2)  # scale
        bar = "█" * bar_length

        print(f"{name:<10} | {bar:<50} {allocation:.1f}%")