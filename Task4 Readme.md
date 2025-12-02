Project Overview

This Power BI project analyzes the Superstore dataset to identify sales performance, customer trends, and profit-generating segments.
The dashboard includes key metrics, visualizations, and interactive filters to help stakeholders understand business performance and make data-driven decisions.

Dataset Information

The dataset includes the following fields:

Sales

Profit

Order Date

Customer Details

Category & Subcategory

Region & Segment

Ship Mode

Order ID

Objectives of the Dashboard

✔ Track Sales, Profit, Number of Orders, and Profit Margin
✔ Analyze sales trends over time
✔ Identify top and low-performing categories & subcategories
✔ Compare performance by region and customer segment
✔ Provide interactive filtering and drill-down analysis

Steps Followed
Phase 1: Data Loading & Cleaning

Imported dataset into Power BI.

Verified data types (Date, Text, Number).

Created hierarchy for Order Date (Year → Quarter → Month → Day).

Phase 2: Dashboard Building
KPIs Created (Cards):
KPI	Calculation
Total Sales	SUM(Sales)
Total Profit	SUM(Profit)
Total Orders	DISTINCTCOUNT(Order ID)
Profit Margin %	DIVIDE(SUM(Profit), SUM(Sales), 0)
Visuals Used:
Visual Type	Purpose
Line Chart	Sales trend by Order Date
Bar Chart	Sales & Profit by Category
Bar Chart	Sales by Sub-Category
Map / Filled Map	Regional Performance
Pie / Donut Chart	Customer Segment Share
Slicer	Order Date, Category, Region filters
Phase 3: Formatting & Final Touches

Added borders, shadows, and theme colors.

Applied consistent font style.

Organized layout for KPI → Trend → Category → Segment structure.

Tested slicers and interactions.

Final Dashboard Preview

(Insert screenshot here after exporting from Power BI)
Example:

 KPIs at the top  
 Trend chart in the middle  
 Category & regional charts at the bottom

 Insights Summary

Technology and Office Supplies generate the highest sales.

Some subcategories show high revenue but low profitability.

Certain regions perform better, indicating market expansion opportunities.

Profit margin varies by category and customer segment.

Tools Used

Power BI Desktop

DAX

Data Modeling

Visualization Design Principles
