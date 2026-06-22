import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def extract_data():
    customers = pd.read_csv(os.path.join(DATA_DIR, "customers.csv"))
    products = pd.read_csv(os.path.join(DATA_DIR, "products.csv"))
    orders = pd.read_csv(os.path.join(DATA_DIR, "orders.csv"))
    sales = pd.read_csv(os.path.join(DATA_DIR, "sales.csv"))

    print("Data Extracted Successfully")

    return customers, products, orders, sales