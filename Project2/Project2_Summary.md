# Project 2: Exploratory Data Analysis — Summary

**Intern:** Ali Ghous | **Company:** DecodeLabs | **Dataset:** Orders Data (1,200 records)

---

## Key Statistics

| Metric | Value |
|--------|-------|
| Total Orders | 1,200 |
| Average Order Value | $1,053.97 |
| Median Order Value | $823.62 |
| Highest Order | $3,456.40 |
| Lowest Order | $11.39 |

---

## Key Observations

**1. Distribution is right-skewed**
The mean order value ($1,053.97) is noticeably higher than the median ($823.62). This gap tells us a handful of large orders are pulling the average up — most customers are actually spending closer to the median figure.

**2. Missing CouponCode values are expected, not an error**
309 out of 1,200 orders had no coupon code recorded. After reviewing the data, this isn't a data quality issue — it simply means those customers checked out without applying a coupon. These were labeled "No Coupon" instead of being deleted, since removing them would have meant losing valid order data.

**3. Eight outliers identified using the IQR method**
Using Q1, Q3, and the 1.5×IQR rule, 8 orders fell outside the expected range, with values between $3,334 and $3,456.

**4. Outliers turned out to be legitimate bulk orders**
On closer inspection, every single outlier order had a Quantity of 5 — the maximum quantity in the entire dataset. This confirms these aren't data entry errors; they're genuine high-value purchases from customers buying in bulk. They were kept in the dataset rather than removed.

**5. Strong correlation between UnitPrice and TotalPrice**
A correlation analysis showed UnitPrice and TotalPrice are strongly related (0.72), which lines up with basic logic — pricier items lead to higher order totals.

**6. No bulk-pricing discount in this dataset**
Quantity and UnitPrice showed almost no correlation (0.015). In most retail platforms, ordering more units usually brings the per-unit price down, but that pattern doesn't exist here — worth flagging as a possible gap in pricing strategy.

---

## Business Takeaway

The 8 customers placing maximum-quantity orders represent a high-value segment worth identifying separately — they could be strong candidates for a loyalty program or bulk-order discount strategy. Additionally, the absence of a quantity-based pricing discount is something the business may want to revisit.

---

## Tools Used

Python, Pandas, Matplotlib, Seaborn, VS Code
