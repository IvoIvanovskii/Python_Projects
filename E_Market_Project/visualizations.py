import matplotlib.pyplot as plt
import mysql.connector

def generate_market_visuals():
    # Connect to MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="",       # ← Replace with your MySQL username
        password="HOMEGROWN18ia!",   # ← Replace with your MySQL password
        database=""    # ← Replace with your database name
    )
    cursor = conn.cursor()

    # Histogram of Product Prices
    cursor.execute("SELECT price FROM products")
    prices = [row[0] for row in cursor.fetchall()]

    # Bar Chart of Product Quantities
    cursor.execute("SELECT name, quantity FROM products")
    products = cursor.fetchall()
    product_names = [row[0] for row in products]
    quantities = [row[1] for row in products]

    # Histogram of Total Spending per Customer
    cursor.execute("SELECT customer_id, SUM(total_amount) FROM orders GROUP BY customer_id")
    spending = [row[1] for row in cursor.fetchall()]

    # Bar Chart of Number of Orders per Customer
    cursor.execute("SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id")
    orders_count = cursor.fetchall()
    customer_ids = [str(row[0]) for row in orders_count]
    num_orders = [row[1] for row in orders_count]

    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('E-Market Analytics')

    # Plot 1: Product Price Distribution
    axs[0, 0].hist(prices, bins=10, color='skyblue', edgecolor='black')
    axs[0, 0].set_title('Product Price Distribution')
    axs[0, 0].set_xlabel('Price')
    axs[0, 0].set_ylabel('Frequency')

    # Plot 2: Product Quantities
    axs[0, 1].bar(product_names, quantities, color='orange')
    axs[0, 1].set_title('Product Quantities')
    axs[0, 1].set_xticklabels(product_names, rotation=45, ha='right')
    axs[0, 1].set_ylabel('Quantity')

    # Plot 3: Spending Distribution
    axs[1, 0].hist(spending, bins=10, color='green', edgecolor='black')
    axs[1, 0].set_title('Customer Spending Distribution')
    axs[1, 0].set_xlabel('Total Amount')
    axs[1, 0].set_ylabel('Frequency')

    # Plot 4: Orders Per Customer
    axs[1, 1].bar(customer_ids, num_orders, color='purple')
    axs[1, 1].set_title('Orders Per Customer')
    axs[1, 1].set_xlabel('Customer ID')
    axs[1, 1].set_ylabel('Orders')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    cursor.close()
    conn.close()
