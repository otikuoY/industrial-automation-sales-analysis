# Final Report: Industrial Automation Sales Analysis

## 1. Objective

The objective of this project was to analyze ERP order data from an industrial automation company and convert the results into a privacy-safe public portfolio project.

The internal business request focused on:

- identifying the top five customers by final KRW order value,
- analyzing monthly order trends,
- comparing domestic and overseas activity,
- and visualizing employee order performance by year.

The public version preserves the analytical structure while removing confidential names and monetary values.

---

## 2. Data Preparation

The source dataset contained 2,511 historical ERP order records.

The analysis applied the following filters:

- date range: January 2024 through June 2026,
- formal order types: A and B,
- excluded order type: T,
- valid domestic or overseas classification,
- positive calculated order value,
- nonmissing customer and employee information.

The final private analytical dataset contained 569 records:

- 468 domestic orders,
- 101 overseas orders,
- 88 standardized customers,
- 10 employees.

### Currency Treatment

Domestic order value was calculated using `Amt`.

Overseas order value was calculated using `Amt × Mny`.

The calculated overseas KRW values were compared against `wAmt` as a validation check.

---

## 3. Privacy Protection

The public dataset does not contain company names, customer names, employee names, original order numbers, actual monetary values, private mapping tables, or the original ERP file.

Customers and employees were replaced with stable anonymous identifiers such as `Customer_01` and `Employee_01`.

Actual monetary values were converted into relative indices.

---

## 4. Customer Analysis

The highest-value customer was assigned an order value index of 100.

The next four customers had indices of approximately 89.0, 79.6, 75.7, and 73.6.

Three of the top five customers were fully domestic. One was fully overseas, and one generated approximately 86.5% of its order value from overseas activity.

The monthly trend revealed that customer activity was not evenly distributed. Instead, the largest customers often had one or two major order months that created sharp spikes.

---

## 5. Employee Analysis

Employee performance was analyzed using anonymized ERP `PostName` attribution.

Two comparisons were created:

1. yearly performance for 2024, 2025, and 2026 YTD,
2. January-June performance for 2024, 2025, and 2026.

The second comparison was necessary because 2026 includes only six months of data.

Employee_01 recorded the highest employee-year index in 2025 and the highest January-June index in 2026.

The analysis should not be interpreted as a complete employee evaluation because it measures order attribution rather than profit, workload, collaboration, or sales difficulty.

---

## 6. Domestic and Overseas Mix

| Period | Domestic Share | Overseas Share |
|---|---:|---:|
| 2024 | 85.3% | 14.7% |
| 2025 | 74.9% | 25.1% |
| 2026 YTD | 90.9% | 9.1% |

Overseas activity became more important in 2025, then declined in the first half of 2026.

Because the 2026 period is incomplete, the result should be treated as a YTD observation rather than a full-year conclusion.

---

## 7. Main Conclusions

1. The company relied on several similarly important high-value customers.
2. The top customer portfolio included both fully domestic and strongly overseas-oriented accounts.
3. Large individual orders caused strong monthly volatility.
4. Employee_01 led the indexed employee results in 2025 and in the 2026 January-June comparison.
5. Overseas order share peaked in 2025 among the three analyzed periods.
6. Same-period comparisons are more reliable than comparing full-year 2024 and 2025 results directly with 2026 YTD.

---

## 8. Limitations

- 2026 includes only January through June.
- Actual monetary values are not shown publicly.
- Order value does not equal recognized revenue or profit.
- Monthly spikes may reflect a small number of large projects.
- ERP employee attribution may not capture shared work.
- The public dataset is aggregated, so transaction-level modeling is intentionally limited.

---

## 9. Future Improvements

Future versions could include customer concentration metrics, rolling averages, order-frequency analysis, average order-size comparisons, department-level trends, repeat-customer analysis, forecast intervals, and scenario analysis for overseas growth.
