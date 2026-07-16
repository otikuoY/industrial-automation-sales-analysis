# Sales, Revenue, and Material Cost Profitability Analysis Using ERP Data

## Project Overview

This project analyzed ERP-based order, revenue, and material cost data from an industrial automation company. The goal was to understand how customer orders translated into revenue, how much revenue remained unbilled, and how planned and actual material costs affected project-level profitability.

The analysis began with formal domestic and overseas order data from 2024 to 2026. I cleaned and filtered the raw order records, converted overseas order amounts into KRW using exchange rates, and identified major customers by total order amount. I then expanded the project by connecting order data with revenue data and material cost data using order numbers as the main key.

Because the original dataset contains confidential company information, the public version of this project uses anonymized or summarized data only.

## Business Problem

The company needed a clearer way to understand performance across orders, customers, employees, departments, revenue collection, and material cost structure.

The main questions were:

- Which customers contributed the most to total order amount?
- How did monthly order and revenue trends change from 2024 to 2026?
- How much ordered value had not yet been billed as revenue?
- How did planned material cost compare with actual material cost?
- Which projects had strong or weak material-cost-based profitability?
- How did profitability differ by employee, customer, and department?

## Data Used

The analysis used several internal ERP data sources:

1. **Order data**
   - Order number
   - Order date
   - Customer
   - Employee
   - Department
   - Domestic/overseas classification
   - Order amount
   - Exchange rate for overseas orders

2. **Revenue data**
   - Revenue date
   - Revenue number
   - Order number
   - Customer
   - Revenue amount

3. **Planned material cost data**
   - Order number
   - Item code
   - Item description
   - Planned material cost

4. **Actual material cost data**
   - Order number
   - Item code
   - Item description
   - Actual material cost
   - Material category

Labor cost and overhead cost were excluded because they contained sensitive information. Therefore, all profitability metrics in this project are material-cost-based margins, not full operating profit margins.

## Methods

### 1. Order Data Cleaning

I filtered the order data to include formal domestic and overseas orders from 2024 through June 2026. Non-formal purchase records were excluded based on the company’s order-number rules.

For overseas orders, I converted the order amount into KRW using the exchange rate in the ERP data.

### 2. Customer and Monthly Order Analysis

I aggregated order amounts by customer to identify the largest customers by total order value. I also created monthly trend tables and charts to show how order volume changed over time.

### 3. Order-to-Revenue Analysis

I connected order data with revenue data using order numbers. This made it possible to compare ordered amounts with billed revenue and calculate unbilled amounts.

This analysis helped identify:

- Total order amount
- Total billed revenue
- Unbilled amount
- Monthly revenue trends
- Orders with remaining unbilled balances

### 4. Planned vs. Actual Material Cost Analysis

I connected planned material cost and actual material cost data with the order data using order numbers.

For each order, I calculated:

- Planned material cost
- Actual material cost
- Difference between actual and planned material cost
- Planned material-cost-based profit
- Actual material-cost-based profit
- Planned material margin rate
- Actual material margin rate

The margin formula was:

```text
Material-cost-based margin rate =
(Order Amount - Material Cost) / Order Amount × 100
```

### 5. Profitability Segmentation

I summarized material-cost-based profitability by:

- Project / order
- Employee
- Customer
- Department

I also created an X-Y profitability quadrant chart:

- X-axis: actual material cost ratio
- Y-axis: material-cost-based profit amount
- Upper-left quadrant: lower material cost ratio and higher profit
- Upper-right quadrant: higher material cost ratio but still high profit
- Lower-right quadrant: higher material cost ratio and lower profit, suggesting improvement opportunities

## Key Analyses

The final analysis included:

- Top customer analysis by total order amount
- Monthly order trend analysis
- Monthly revenue trend comparison
- Order amount vs. billed revenue comparison
- Unbilled amount analysis
- Planned material cost vs. actual material cost comparison
- Project-level profitability quadrant analysis
- Employee-level material margin analysis
- Customer-level material profitability analysis
- Department-level material profitability analysis
- Item-level material cost difference analysis

## Key Findings

The analysis showed that ERP data can reveal meaningful patterns across sales, billing, and material cost structure.

Key observations included:

- A small number of customers accounted for a large share of total order amount.
- Connecting order data with revenue data made it possible to identify orders with remaining unbilled balances.
- Planned and actual material costs did not always match, showing the importance of monitoring cost differences after orders are received.
- Material-cost-based profitability varied across projects, customers, employees, and departments.
- The X-Y profitability quadrant helped separate projects that were both high-profit and cost-efficient from projects that may need cost improvement.
- Item-level cost analysis helped identify materials or items with large differences between planned and actual cost.

## Tools Used

- Python
- pandas
- NumPy
- Matplotlib
- openpyxl
- Excel
- Google Colab
- GitHub

## What I Learned

Through this project, I learned that data analysis is not just about making charts. It also requires understanding business definitions, asking clarification questions, validating data sources, and making sure the final results are useful to people inside the company.

I also learned how different business datasets are connected in practice. Order data, revenue data, and cost data are stored separately, but they can be combined through keys such as order numbers to create a more complete picture of business performance.

This project helped me better understand how data science can be applied to real business problems, especially in sales performance, revenue tracking, cost control, and profitability analysis.

## Limitations and Data Privacy

The original data contains confidential company information, including customer names, employee names, order amounts, and cost data. For that reason, raw data and internal Excel files are not included in the public version of this project.

The public version will only include anonymized, summarized, or transformed data. Customer and employee names will be removed or replaced with generic labels.

Another limitation is that the profitability analysis only includes material costs. Labor costs and overhead costs were excluded because they contained sensitive information. Therefore, the margin analysis should be interpreted as material-cost-based profitability, not full company profit.
