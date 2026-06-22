import mysql.connector

def load_data(df):

 
    
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce_dw",
    auth_plugin="mysql_native_password"
    )

    cursor = conn.cursor()

    # insert query
    query = """
    INSERT INTO sales_fact
    (sale_id, customer_name, city, product_name, category, quantity, price, revenue)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    for _, row in df.iterrows():
        cursor.execute(query, (
            row["sale_id"],
            row["name"],
            row["city"],
            row["product_name"],
            row["category"],
            row["quantity"],
            row["price"],
            row["revenue"]
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded into MySQL successfully")