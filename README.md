# Sales, Revenue, and Material Cost Profitability Analysis Using ERP Data

## Overview

This project analyzes ERP-based order, revenue, and material cost data from an industrial automation company. The goal was to understand how customer orders translated into revenue, how much revenue remained unbilled, and how planned and actual material costs affected project-level profitability.

The analysis connects order data, revenue data, planned material cost data, and actual material cost data using order numbers as the main key.

Because the original dataset contains confidential company information, this public version uses anonymized or summarized data only.

## Project Goals

- Analyze formal domestic and overseas orders from 2024 to 2026
- Convert overseas order amounts into KRW using exchange rates
- Identify major customers by total order amount
- Compare order amounts with billed revenue
- Analyze unbilled order amounts
- Compare planned material cost with actual material cost
- Analyze material-cost-based profitability by project, employee, customer, and department

## Key Analyses

- Top customer analysis by total order amount
- Monthly order and revenue trend analysis
- Order amount vs. billed revenue comparison
- Unbilled amount analysis
- Planned material cost vs. actual material cost comparison
- Project-level profitability quadrant analysis
- Employee-level material margin analysis
- Customer-level material profitability analysis
- Department-level material profitability analysis
- Item-level material cost difference analysis

## Tools Used

- Python
- pandas
- NumPy
- Matplotlib
- openpyxl
- Excel
- Google Colab
- GitHub

## Report

A more detailed explanation of the project is available here:

[Final Report](docs/final_report.md)

## Data Privacy

The original ERP data contains confidential company information, including customer names, employee names, order amounts, revenue records, and cost data.

For privacy reasons, raw company data and internal Excel files are not included in this repository. The public version only uses anonymized, summarized, or transformed data.

## Note

The profitability analysis in this project is based only on material costs. Labor cost and overhead cost were excluded because they contained sensitive information. Therefore, the margin analysis should be interpreted as material-cost-based profitability, not full operating profit margin.