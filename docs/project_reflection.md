# Project Reflection

## Why I Worked on This Project

I wanted to explore how data analysis can be used in a real business environment. Instead of working only with sample datasets, I had the opportunity to analyze internal ERP data from an industrial automation company.

The project helped me understand how companies use data to track orders, revenue, costs, and profitability. It also showed me that real-world data is often messy, incomplete, and dependent on business-specific rules.

## What I Did

I analyzed order, revenue, planned material cost, and actual material cost data.

At the beginning, I focused on order data. I cleaned the records, filtered formal domestic and overseas orders, converted overseas order amounts into KRW, and identified major customers by total order amount.

Then, I connected order data with revenue data using order numbers. This allowed me to compare ordered amounts with billed revenue and identify unbilled order amounts.

In the final stage, I connected order data with planned and actual material cost data. I calculated material-cost-based margins and analyzed profitability by project, employee, customer, and department.

## Challenges

One of the biggest challenges was understanding the company’s internal data structure. The same business concept could appear in different files, and the meaning of certain columns was not always obvious at first.

For example, I had to clarify how to distinguish formal orders from other purchase records, how domestic and overseas orders were coded, and how overseas amounts should be converted into KRW.

Another challenge was making sure the profitability analysis was interpreted correctly. Since labor cost and overhead cost were excluded due to data sensitivity, the margin analysis had to be clearly described as material-cost-based profitability, not full operating profit margin.

## What I Learned

This project taught me that data analysis is not only about writing code or making graphs. It also requires asking the right questions, understanding business definitions, checking assumptions, and validating results.

I learned how different datasets can be connected through shared keys such as order numbers. I also learned that a useful analysis needs to be understandable to people who work with the data in real business settings.

Most importantly, this project helped me see why data science is valuable. By connecting order, revenue, and cost data, I could turn raw ERP records into insights about customer contribution, unbilled revenue, cost differences, and profitability.

## How This Project Connected to My Interests

I am interested in data science because I like using numbers and patterns to understand complex situations. This project gave me a practical example of how data can support decision-making in a company.

It also strengthened my interest in business analytics and quantitative problem-solving. I saw how data can help answer questions that are difficult to understand from raw spreadsheets alone.

## Limitations

The project used confidential company data, so the raw data cannot be shared publicly. Any public version of the project must use anonymized or summarized data.

The profitability analysis was also limited because it only included material costs. Labor cost and overhead cost were excluded, so the results should not be interpreted as full company profit.

## Next Steps

If I continue developing this project, I would like to create a fully anonymized public version with sample data, clean visualizations, and a clear explanation of the analysis process.

I would also like to improve the analysis by adding order-to-revenue conversion speed, unbilled aging, and more detailed cost variance analysis if appropriate data is available.
