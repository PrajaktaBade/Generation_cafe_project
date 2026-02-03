# Cafe Sales ETL & Visualisation Pilot

## Project Overview
This project is a local pilot analytics solution built for a cafe business to help visualise sales performance, profit, and customer purchasing habits.

The solution ingests raw sales data provided as a text file, cleans and anonymises the data, applies business logic to calculate profit, and generates visual insights using Python and Matplotlib.

This pilot is designed to be simple, reproducible, and easily scalable for future expansion to multiple branches or cloud-based infrastructure.

---

## Business Context
The client wanted to understand:
- Sales performance by branch
- Profit by branch (using a 50% markup for cafe products)
- Customer payment preferences (Cash vs Card)
- Popular products and buying patterns

All personally identifiable information (PII), such as customer names and card numbers, must be removed at the earliest stage of data ingestion.

---

## Tools & Technologies Used
- **Python** – Data extraction, transformation, and loading (ETL)
- **Pandas** – Data manipulation and aggregation
- **Matplotlib** – Data visualisation
- **CSV files** – Lightweight local data storage
- **Git & GitHub** – Version control and project documentation
- **VS Code** – Development environment

---

## Project Structure
```
cafe-sales-pilot/
│
├── data/
│ ├── raw/ # Raw TXT input data
│ └── processed/ # Cleaned CSV output
│
├── src/
│ ├── app.py # ETL pipeline
│ └── visualize.py # Data visualisations
│
├── outputs/ # Saved charts (PNG)
├── requirements.txt
└── README.md
```


---

## Data Pipeline (ETL)
### Extract
- Raw sales data is read from a `.txt` file.
- Each record contains customer name, product, price, branch, payment type, card number, and date.

### Transform
- Customer names and card numbers are removed to anonymise the data.
- Prices are cleaned by removing the currency symbol.
- Profit is calculated using a fixed 50% markup.
- Data is structured into a clean tabular format.

### Load
- The cleaned and transformed data is saved as a CSV file.
- This CSV is used directly for visualisation.

---

## Visualisations
The following visualisations are generated using Matplotlib and saved to the `outputs/` folder:

1. **Total Sales by Branch**  
   Helps identify which branches generate the most revenue.

2. **Total Profit by Branch**  
   Highlights the most profitable locations, not just highest sales.

3. **Payment Method Distribution**  
   Shows customer preference between cash and card payments.

4. **Product Popularity**  
   Identifies best-selling products to support stock and pricing decisions.

All charts are displayed during execution and also saved as image files for reporting and presentations.

---

## How to Run the Project

### 1. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Run the ETL Pipeline
```bash
python src/app.py
```

### 3. Generate Visualization
```bash
python src/visualize.py
```
## Scalability & Future Improvements
- The current solution uses CSV files for simplicity and speed.
- The same ETL pipeline can be extended to load data into a local database such as MySQL or PostgreSQL.
- With minimal changes, the solution can be migrated to cloud services such as AWS (S3, RDS).
- Additional branches and larger datasets can be supported without redesigning the pipeline.






