"""Given N products with their total sales, find which product sold the most. Read N, then N lines 'product,sales'. Print the name of the top-selling product. Assume no ties."""
    """Example

Input:
3
Pen,50
Book,120
Bag,90

Expected:
Book
    """
n = int(input())
top_product = None
top_sales = float("-inf")

for _ in range(n):
    product, sales = input().split(",")
    sales = float(sales)
    if sales > top_sales:
        top_product = product
        top_sales = sales

print(top_product)
