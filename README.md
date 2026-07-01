\# Sales Performance Analysis for an Industrial Automation Company



\## Overview



This project analyzes ERP order records from an industrial automation company to examine company-wide order trends, employee performance patterns, customer concentration, monthly order distribution, and dependence on large orders.



The initial business request was to create annual employee order-performance graphs. I expanded that request into a broader data analysis project using Python, pandas, matplotlib, and Excel.



Because the original dataset contains confidential business information, all public materials use anonymized labels, percentage shares, and indexed values instead of employee names, customer names, and actual financial amounts.



\---



\## Research Questions



1\. How did the company’s order performance change across years?

2\. How did employees differ in total order value, order count, and average order value?

3\. Were employee results distributed across many orders or concentrated in a few large orders?

4\. How concentrated was company order value among major customers?

5\. Did monthly order patterns show a consistent seasonal pattern?

6\. How did the first half of 2026 compare with the same period in 2024 and 2025?



\---



\## Dataset



The original dataset contained \*\*2,511 ERP order records\*\* covering January 2010 through June 2026.



The main variables included:



\- Order date

\- Order number

\- Employee

\- Customer

\- Product and product specification

\- Quantity

\- Order amount

\- Sales type

\- Business division

\- Expected delivery date

\- Completed delivery date

\- Record status



After data cleaning, \*\*1,933 records\*\* remained for analysis.



The original company dataset is not included in this repository because it contains confidential employee, customer, product, and financial information.



\---



\## Data Cleaning



The original ERP column names were renamed to clearer English names.



Dates stored in ERP formats such as `20260520` were converted into standard date values. Quantity and order-amount columns were converted into numeric variables.



Records were retained only when:



\- `record\_status` was 0

\- `order\_amount` was greater than 0

\- `order\_date` was valid

\- `order\_number` did not begin with `T`



No duplicated order numbers were found in the cleaned dataset.



The meanings of `record\_status = 1` and order numbers beginning with `T` should be confirmed with the company before the results are used for formal employee-performance evaluation.



\---



\## Methods



The analysis included:



\- Annual company order value

\- Annual company order count

\- Annual average order value

\- Employee order value by year

\- Employee order count

\- Employee average order value

\- January–June same-period comparisons

\- Employee share of company order value

\- Employee dependence on the largest one and three orders

\- Monthly order-value distribution

\- Customer concentration

\- Business-division comparison



For public visualizations, actual financial values were replaced with percentage shares or index values.



For long-term company comparisons, the 2020 result was set equal to an index value of 100.



\---



\## Key Findings



\### 1. Company performance declined sharply in 2024 and partially recovered in 2025



Using 2020 as the baseline of 100, the total order-value index was:



\- 2020: 100.0

\- 2021: 102.3

\- 2022: 122.8

\- 2023: 101.9

\- 2024: 49.3

\- 2025: 68.8



The company recorded its highest indexed order value in 2022. Order value declined sharply in 2024 and partially recovered in 2025.



\### 2. The decline was influenced more by average order size than by order count



In 2024, the order-count index was 83.2, while the average-order-value index was 59.3.



This suggests that the decline in total order value was not caused only by fewer orders. The decrease in average order size had a larger effect.



In 2025, the order-count index recovered to 92.3, while the average-order-value index recovered to 74.5.



\### 3. The first half of 2026 outperformed the same period in 2025



The company’s order value from January through June 2026 was \*\*16.6% higher\*\* than during the same period in 2025.



Because 2026 contains only six months of data, it was compared with the same January–June period in earlier years rather than with complete annual results.



\### 4. Employees showed different performance patterns



Some employees generated performance through many orders with moderate average values, while other employees handled fewer but much larger orders.



One anonymized employee accounted for \*\*53.5%\*\* of company order value during the first half of 2026.



This shows that total order value alone does not fully describe employee performance. Order count, average order value, and dependence on large orders should also be considered.



\### 5. Dependence on large orders varied substantially by employee



For the employee with the most diversified performance, the largest three orders represented only \*\*18.9%\*\* of total order value.



For several other employees, the largest three orders represented approximately \*\*80% or more\*\* of their total order value.



Some employee results were therefore distributed across many orders, while others depended heavily on a small number of large contracts.



\### 6. Customer concentration remained significant



During the first half of 2026:



\- The largest customer represented 29.4% of total order value.

\- The top three customers represented 49.4%.

\- The top five customers represented 65.1%.

\- The top ten customers represented 86.7%.



The company therefore remained meaningfully dependent on a limited number of major customers.



\### 7. The customer base became somewhat broader



The number of customers during the January–June period increased from:



\- 32 customers in 2024

\- 37 customers in 2025

\- 44 customers in 2026



The top-three customer concentration decreased slightly from 52.3% in 2024 to 49.4% in 2026.



This suggests that the company’s customer base became somewhat more diversified, although major customers still represented a large portion of total order value.



\### 8. No consistent monthly seasonal pattern was identified



The month with the highest share of first-half order value differed by year:



\- 2024: April

\- 2025: June

\- 2026: March



Because the peak month changed each year, the data did not show a stable seasonal pattern across the three periods.



A small number of large orders may have strongly influenced the monthly results.



\### 9. Business-division comparisons require caution



A comparison of 2025 and 2026 showed changes in the shares of current business divisions.



However, business-division names appear to have changed over time. Long-term comparisons should not be made until the company confirms whether the older and newer division names represent organizational restructuring or separate departments.



\---



\## Main Visualizations



\### Company Order Performance Indices



!\[Company Order Performance Indices](charts/company\_order\_performance\_indices.png)



This chart compares total order value, order count, and average order value using 2020 as the baseline of 100.



\### Employee Share of Company Order Value



!\[Employee Order Share](charts/employee\_order\_share.png)



This chart shows the percentage of company order value generated by each anonymized employee during the same January–June period.



\### Employee Order Frequency vs. Average Order Value



!\[Employee Order Frequency](charts/employee\_order\_frequency\_vs\_value\_index.png)



This chart distinguishes employees who handled many moderate-sized orders from employees who handled fewer but larger orders.



\### Employee Dependence on Large Orders



!\[Employee Large Order Concentration](charts/employee\_large\_order\_concentration.png)



This chart measures how much of each employee’s performance came from their largest one and three orders.



\### Customer Concentration Trend



!\[Customer Concentration Trend](charts/customer\_concentration\_trend.png)



This chart compares the shares of company order value generated by the largest one, three, and five customers.



\### Monthly Order-Value Distribution



!\[Monthly Order Distribution](charts/monthly\_order\_value\_distribution.png)



This chart shows how each year’s first-half order value was distributed across January through June.



\### Business-Division Order Share



!\[Business Division Order Share](charts/business\_division\_order\_share.png)



This chart compares the shares of company order value generated by anonymized business divisions during the same period in 2025 and 2026.



\---



\## Business Implications



The analysis suggests several ways the company could improve internal performance monitoring:



1\. Evaluate employees using multiple measures instead of total order value alone.

2\. Track order count and average order value separately.

3\. Monitor employee dependence on a small number of large orders.

4\. Monitor concentration among major customers.

5\. Compare incomplete years only with the same period in previous years.

6\. Record organizational changes so business-division performance can be compared consistently.

7\. Combine order records with employee targets to calculate target-achievement rates.

8\. Include profit or profit-margin data in future analyses.



\---



\## Limitations



This analysis has several limitations:



\- It uses order value rather than profit or profit margin.

\- A high order value does not necessarily indicate high profitability.

\- Individual large orders can strongly affect monthly and annual results.

\- Employee assignments may change during a project.

\- Shared or collaborative sales efforts are not identified.

\- Cancelled or modified orders may require additional company rules.

\- Business-division names appear to have changed over time.

\- 2026 data includes only January through June.

\- The analysis identifies patterns and associations, not causes.



\---



\## Privacy and Ethics



The original ERP data contains confidential company, employee, customer, product, and financial information.



The following materials are not included in the public repository:



\- Original ERP data

\- Cleaned data containing real identities

\- Employee names

\- Customer names

\- Detailed product information

\- Actual financial amounts

\- Internal SQL files

\- Internal Excel dashboards



Public materials use:



\- Employee labels such as `Employee A`

\- Customer labels such as `Customer A`

\- Business-division labels such as `Division A`

\- Percentage shares

\- Indexed financial values



\---



\## Project Structure



```text

industrial-automation-sales-analysis

├── README.md

├── data

│   ├── raw

│   └── clean

├── notebooks

│   ├── 01\_data\_cleaning\_and\_exploration.ipynb

│   └── 02\_sales\_performance\_analysis.ipynb

├── charts

│   ├── employee\_order\_share.png

│   ├── annual\_company\_order\_index.png

│   ├── annual\_company\_order\_count\_index.png

│   ├── annual\_average\_order\_value\_index.png

│   ├── company\_order\_performance\_indices.png

│   ├── employee\_order\_frequency\_vs\_value\_index.png

│   ├── employee\_large\_order\_concentration.png

│   ├── monthly\_order\_value\_distribution.png

│   ├── top\_customer\_order\_share.png

│   ├── customer\_concentration\_trend.png

│   └── business\_division\_order\_share.png

├── report

│   ├── project\_plan.txt

│   └── final\_report.md

├── reference

└── private\_output

```



The `data/raw`, `data/clean`, `reference`, and `private\_output` folders contain confidential internal materials and are not intended for public release.



\---



\## Tools Used



\- Python

\- pandas

\- NumPy

\- matplotlib

\- Google Colab

\- Microsoft Excel

\- Markdown



\---



\## Full Report



Read the complete project report here:



\[Final Report](report/final\_report.md)



\---



\## Reflection



This project taught me that analyzing real business data requires more than producing graphs.



I had to understand unfamiliar ERP variables, define defensible data-cleaning rules, compare partial-year data fairly, recognize misleading percentage changes, and protect confidential information.



I also learned that relying on a single performance measure can be misleading. Total order value, order count, average order size, dependence on large contracts, and customer concentration each reveal different parts of business performance.



The project strengthened my interest in data science because it required both technical analysis and careful interpretation of a real business problem.

