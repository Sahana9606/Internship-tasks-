Objective
Analyze monthly revenue and order volume from the `online_sales` dataset to understand sales performance trends over time.

Tools Used
- PostgreSQL / MySQL / SQLite (any relational SQL database)

Dataset Description
Table: `online_sales`  
| Column Name  | Description                     |
|--------------|---------------------------------|
| order_date   | Date when the order was placed |
| amount       | Order value / revenue          |
| product_id   | Product identifier             |
| order_id     | Unique order number            |


Interpretation
  Higher revenue & order counts indicate strong-performing months.
  Trends can help identify peak seasons and low periods.
  Useful for forecasting, marketing, and inventory strategies.

Deliverables
  SQL script
  Results table / exported result screenshot

Learning Outcome
   Understanding GROUP BY with time dimensions
   Using SUM() for aggregation
   Counting distinct orders for volume
  Sorting and analyzing time-series sales trends
