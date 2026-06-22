from extract import extract_data
from transform import transform_data
from load import load_data
from validation import validate_and_clean
from logger import log


try:
    log("ETL Pipeline Started")

    customers, products, orders, sales = extract_data()
    log("Data Extracted Successfully")

    customers = validate_and_clean(customers, "Customers")
    products = validate_and_clean(products, "Products")
    orders = validate_and_clean(orders, "Orders")
    sales = validate_and_clean(sales, "Sales")

    log("Validation Completed")

    final_df = transform_data(customers, products, orders, sales)
    log("Transformation Completed")

    load_data(final_df)
    log("Data Loaded Successfully")

    log("ETL Pipeline Finished Successfully")

except Exception as e:
    log(f"Pipeline Failed: {str(e)}")