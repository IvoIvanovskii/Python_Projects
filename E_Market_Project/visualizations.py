import matplotlib.pyplot as plt
from db import connect  
from mysql.connector import Error

def generate_market_visuals():
    try:
        with connect() as conn:  
            with conn.cursor() as cursor:
                cursor.execute("SELECT price FROM products")
                prices = [row[0] for row in cursor.fetchall() if row[0] is not None]

                cursor.execute("SELECT product_name, quantity FROM products")
                products = cursor.fetchall()
                product_names = [row[0] for row in products]
                quantities = [row[1] for row in products]

                cursor.execute("SELECT customer_id, SUM(total_amount) FROM orders GROUP BY customer_id")
                spending = [row[1] for row in cursor.fetchall() if row[1] is not None]

                cursor.execute("SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id")
                orders_count = cursor.fetchall()
                customer_ids = [str(row[0]) for row in orders_count]
                num_orders = [row[1] for row in orders_count]

                fig, axs = plt.subplots(2, 2, figsize=(12, 10))
                fig.suptitle('E-Market Analytics')

                axs[0, 0].hist(prices, bins=10, color='skyblue', edgecolor='black')
                axs[0, 0].set_title('Product Price Distribution')
                axs[0, 0].set_xlabel('Price')
                axs[0, 0].set_ylabel('Frequency')

                axs[0, 1].bar(range(len(product_names)), quantities, color='orange')
                axs[0, 1].set_xticks(range(len(product_names)))
                axs[0, 1].set_xticklabels(product_names, rotation=45, ha='right')
                axs[0, 1].set_title('Product Quantities')
                axs[0, 1].set_ylabel('Quantity')

                axs[1, 0].hist(spending, bins=10, color='green', edgecolor='black')
                axs[1, 0].set_title('Customer Spending Distribution')
                axs[1, 0].set_xlabel('Total Amount')
                axs[1, 0].set_ylabel('Frequency')

                axs[1, 1].bar(customer_ids, num_orders, color='purple')
                axs[1, 1].set_title('Orders Per Customer')
                axs[1, 1].set_xlabel('Customer ID')
                axs[1, 1].set_ylabel('Orders')
                axs[1, 1].tick_params(axis='x', rotation=45)

                plt.tight_layout(rect=[0, 0.03, 1, 0.95])
                plt.show()

    except Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")