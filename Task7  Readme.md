This project demonstrates how to use Python to interact with a SQLite database, perform basic SQL queries, and visualize sales data using pandas and matplotlib. It's designed as a beginner-friendly exercise to help you understand database operations and data visualization.

Task Objective

- Create a small SQLite database with product and sales data
- Run SQL queries to calculate total quantity sold and revenue per product
- Display results using pandas and plot a simple bar chart with matplotlib

Tools & Libraries

- Python 3.x
- SQLite3
- pandas
- matplotlib

Project Structure
├── create_db.py      
#Script to create and populate the SQLite database 
├─ analyze_sales.py     
#Script to query and visualize sales data
├── sales_data.db         
#SQLite database file (auto-generated) 
├── sales_chart.png    
#Output chart image (auto-generated)
└── README.md           
#Project documentation

1. Clone the repository
   git clone https://github.com/yourusername/sales-summary-sqlite.git
   cd sales-summary-sqlite
2. Create a database
   python create_db.py
3. Analyze and visualize sales
   python analyze_sales.py
4. View the output
   - The terminal will display a summary table with product, total quantity sold, and revenue.
   - A bar chart image (sales_chart.png) will be saved in the project folder.

