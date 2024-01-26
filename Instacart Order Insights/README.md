### Background

This project is part of the Data Science program at TripleTen. More info in the link below:
[https://tripleten.com/data-science/](https://tripleten.com/data-science/)

### Project Setup

Instacart is a grocery delivery platform where customers can place a grocery order and have it delivered to them, similar to how Uber Eats and DoorDash work. This particular dataset was publicly released by Instacart in 2017 for a Kaggle competition. Although the original dataset is no longer available on the Instacart website, we’ve created CSV files that contain a modified version of that data. Download these files and use them for this project. 

### Project Instructions

The goal is to clean up the data and prepare a report that gives insight into the shopping habits of Instacart customers.

## Data Analysis Steps

### Step 1: Open and Review Data Files

1. Open the following data files:
   - `instacart_orders.csv`
   - `products.csv`
   - `aisles.csv`
   - `departments.csv`
   - `order_products.csv`
2. Review the contents of each table. 
   - Note: Files have nonstandard formatting.
   - Use appropriate arguments in `pd.read_csv()` to read the data correctly.
   - Inspect the CSV files to determine necessary arguments.

### Step 2: Preprocess the Data

1. **Verify and Fix Data Types**
   - Ensure ID columns are integers.
2. **Identify and Fill Missing Values**
3. **Identify and Remove Duplicate Values**
4. **Documentation**
   - Explain the types of missing and duplicate values encountered.
   - Describe methods used for filling/removing these values.
   - Justify your approach and hypotheses about why these issues were present.

### Step 3: Data Analysis and Visualization

#### [A] Mandatory Analysis

1. Verify sensible values in `order_hour_of_day` (0-23) and `order_dow` (0-6) in orders table.
2. Create plots:
   - Distribution of orders by hour of the day.
   - Distribution of orders by day of the week.
   - Time intervals between orders, noting minimum and maximum values.

#### [B] Mandatory Analysis

1. Compare `order_hour_of_day` distributions on Wednesdays and Saturdays.
   - Plot histograms for both days on a single plot.
   - Describe observed differences.
2. Plot the distribution of the number of orders per customer.
3. Identify top 20 most frequently ordered products (display ID and name).

#### [C] Optional Analysis (Complete at least two)

1. Analyze typical item count per order and its distribution.
2. Identify top 20 items reordered most frequently (display names and product IDs).
3. Calculate reorder proportion for each product (table with product ID, name, reorder proportion).
4. For each customer, determine the proportion of reordered products.
5. Identify top 20 items most often added first to the cart (display product IDs, names, and counts).

### Data Description

There are five tables in the dataset. Below is a data dictionary that lists the columns in each table and describes the data that holds.

#### instacart_orders.csv: each row corresponds to one order on the Instacart app

- 'order_id': ID number that uniquely identifies each order
- 'user_id': ID number that uniquely identifies each customer account
- 'order_number': the number of times this customer has placed an order
- 'order_dow': day of the week that the order placed (which day is 0 is uncertain)
- 'order_hour_of_day': hour of the day that the order was placed
- 'days_since_prior_order': number of days since this customer placed their previous order

#### products.csv: each row corresponds to a unique product that customers can buy

- 'product_id': ID number that uniquely identifies each product
- 'product_name': name of the product
- 'aisle_id': ID number that uniquely identifies each grocery aisle category
- 'department_id': ID number that uniquely identifies each grocery department category

#### order_products.csv: each row corresponds to one item placed in an order

- 'order_id': ID number that uniquely identifies each order
- 'product_id': ID number that uniquely identifies each product
- 'add_to_cart_order': the sequential order in which each item was placed in the cart
- 'reordered': 0 if the customer has never ordered this product before, 1 if they have

#### aisles.csv

- 'aisle_id': ID number that uniquely identifies each grocery aisle category
- 'aisle': name of the aisle

#### departments.csv

- 'department_id': ID number that uniquely identifies each grocery department category
- 'department': name of the department

### Conclusion

Analysis of the Instacart dataset reveals the following insights:

- **Shopping Patterns**: Customers shop at all hours, with a **peak between 9 am and 3 pm**. This pattern remains consistent throughout the week.

- **Reordering Trends**: A significant trend in reordering occurs within a **30-day interval**, with the most common reorder day being the 30th.

- **Customer Order Frequency**: 
  - The **majority of customers place 10 or fewer orders**.
  - There is a notable decrease in the number of customers placing more than 10 orders.

- **Variation in Shopping Times**:
  - **Between 11 am and 2 pm**, a distinct variation in `order_hour_of_day` is observed.
  - This variation is particularly evident when comparing shopping patterns on **Wednesdays and Saturdays**.

- **Popular Products**:
  - The analysis identified the **top 20 popular products**, shedding light on customer preferences.

- **Order Composition**:
  - Most orders **contain just one product**.
  - **Half of the orders consist of eight or fewer items**.

- **First Item in Cart**:
  - **Bananas (regular and organic)** are the most frequently first-added items to carts, indicating their high popularity.

These findings offer valuable insights into customer behaviors and preferences, which are crucial for developing **targeted marketing strategies and effective inventory management**.

### Technologies Used

- Python (Pandas, NumPy, Matplotlib)
