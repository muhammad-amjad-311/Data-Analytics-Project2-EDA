# Data-Analytics-Project2-EDA
This is my Second project as a data analyst as an internee at the Decodelabs.

# Data Analytics Internship — Project 2: Exploratory Data Analysis

This is my second project as a Data Analytics Intern at DecodeLabs. After cleaning a dataset in Project 1, this one focuses on actually digging into clean data to find patterns, trends, and outliers — the part of analysis that turns numbers into a story.

## About the Dataset

The dataset contains 1,200 e-commerce order records with details like quantity, unit price, items in cart, payment method, and total price.

## What I Did

**1. Calculated basic statistics**
Used `df.describe()` to get the mean, median, min, max, and quartiles for all numeric columns.

**2. Investigated missing data**
309 orders had no CouponCode listed. Instead of assuming this was bad data and deleting those rows, I checked it first — it turned out these were simply customers who didn't use a coupon. I filled those values with "No Coupon" rather than dropping the rows, since the order data itself was still valid.

**3. Compared mean vs. median**
The average order value came out to $1,053.97, while the median was $823.62. That gap was a clue — it meant a handful of large orders were pulling the average up, so the median gives a more honest picture of what a "typical" order looks like.

**4. Detected outliers using the IQR method**
Using Q1, Q3, and the standard 1.5×IQR rule, I found 8 orders sitting outside the expected range (all above $3,334).

**5. Investigated the outliers instead of just removing them**
Rather than assuming these were errors, I checked the underlying data and found that every single outlier had a Quantity of 5 — the maximum quantity in the entire dataset. That told me these weren't mistakes; they were genuine bulk purchases. I kept them in the dataset.

**6. Ran a correlation analysis**
Checked how Quantity, UnitPrice, ItemsInCart, and TotalPrice relate to each other. UnitPrice and TotalPrice showed the strongest relationship (0.72), which makes sense. Interestingly, Quantity and UnitPrice showed almost no correlation (0.015) — meaning there's no bulk-pricing discount built into this dataset, unlike what you'd typically see on a retail site.

**7. Built a correlation heatmap**
Visualized the correlation matrix using Seaborn to make the relationships easier to read at a glance.

## Key Takeaways

- The data is right-skewed, so median is a more reliable measure of "typical" order value than mean.
- Missing values aren't always a problem — sometimes they're just telling you something didn't happen (in this case, no coupon was used).
- Outliers shouldn't be deleted automatically. Investigating *why* a value is unusual matters more than the fact that it's unusual.
- This dataset doesn't reward bulk orders with lower unit prices, which could be a gap worth flagging for the business.

## Tools Used

Python, Pandas, Matplotlib, Seaborn, VS Code

## Files in This Repository

- `code.py` — full analysis script
- `Dataset for Data Analytics.xlsx` — source dataset
- `correlation_heatmap.png` — visualization output

---
*Part of the Data Analytics Internship Industrial Training Kit — DecodeLabs*
