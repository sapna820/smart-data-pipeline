def validate_and_clean(df, name):

    print(f"Validating {name}...")

    if df is None or df.empty:
        raise Exception(f"{name} is empty")

    # missing values handling
    df = df.fillna(0)

    # remove duplicates
    df = df.drop_duplicates()

    print(f"{name} validation completed")

    return df