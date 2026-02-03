import csv

INPUT_FILE = "../data/raw/cafe_sales.txt"
OUTPUT_FILE = "../data/processed/clean_sales.csv"

MARKUP = 0.5  # 50% cafe markup

clean_rows = []

with open(INPUT_FILE, "r") as file:
    for line in file:
        parts = line.strip().split()

        customer_name = parts[0]          # PII (REMOVE)
        product = parts[1]
        price = float(parts[2].replace("£", ""))
        branch = parts[3]
        payment_type = parts[4]
        card_number = parts[5]            # PII (REMOVE)
        date = parts[6]

        profit = round(price * MARKUP, 2)

        clean_rows.append([
            product,
            price,
            profit,
            branch,
            payment_type,
            date
        ])

with open(OUTPUT_FILE, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Product",
        "Price",
        "Profit",
        "Branch",
        "Payment_Type",
        "Date"
    ])
    writer.writerows(clean_rows)

print("ETL pipeline completed. Clean data saved.")
