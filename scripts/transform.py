def transform_data(customers, products, orders, sales):

    df = sales.copy()

    df = df.merge(products, on="product_id", how="left")
    df = df.merge(orders, on="order_id", how="left")
    df = df.merge(customers, on="customer_id", how="left")

    df["revenue"] = df["price"] * df["quantity"]

    final_df = df[[
        "sale_id",
        "name",
        "city",
        "product_name",
        "category",
        "quantity",
        "price",
        "revenue"
    ]]

    return final_df
