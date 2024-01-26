### Background

This project is part of the Data Science program at TripleTen. More info in the link below:  
[https://tripleten.com/data-science/](https://tripleten.com/data-science/)

## Project Overview

You work as an analyst for the telecom operator Megaline. The company offers two prepaid plans, **Surf** and **Ultimate**. The commercial department is interested in determining which of these plans brings in more revenue to adjust the advertising budget.

### Objective

Your task is to conduct a preliminary analysis of the plans based on data from 500 Megaline clients. This data includes client demographics, plan usage, and the number of calls and text messages sent in 2018. Your goal is to analyze client behavior and determine which prepaid plan generates more revenue.

## Description of the Plans

### General Policy

- **Rounding**: Megaline rounds seconds up to minutes, and megabytes to gigabytes.
  - For calls, each individual call is rounded up; a call lasting just one second will count as one minute.
  - For web traffic, individual sessions are not rounded up. Instead, the total for the month is rounded. If a user consumes 1025 megabytes in a month, they will be charged for 2 gigabytes.

### Surf Plan

- **Monthly Charge**: $20
- **Inclusions**:
  - 500 minutes
  - 50 text messages
  - 15 GB of data
- **Excess Charges**:
  - 1 minute: 3 cents
  - 1 text message: 3 cents
  - 1 GB of data: $10

### Ultimate Plan

- **Monthly Charge**: $70
- **Inclusions**:
  - 3000 minutes
  - 1000 text messages
  - 30 GB of data
- **Excess Charges**:
  - 1 minute: 1 cent
  - 1 text message: 1 cent
  - 1 GB of data: $7


## Project Instructions

### Step 1. Open the Data Files and Study the General Information

Open and review the general content of the following files:
- `megaline_calls.csv`
- `megaline_internet.csv`
- `megaline_messages.csv`
- `megaline_plans.csv`
- `megaline_users.csv`

### Step 2. Prepare the Data

1. **Convert Data Types**: Convert the data to the necessary types.
2. **Error Handling**: Find and eliminate errors in the data.
   - Document the errors found and describe the methods used for correcting them.
3. **User Data Analysis**: For each user, find:
   - The number of calls made and minutes used per month.
   - The number of text messages sent per month.
   - The volume of data per month.
   - The monthly revenue from each user (calculate by subtracting the free package limit from the total number of calls, text messages, and data; multiply the result by the calling plan value; add the monthly charge depending on the calling plan).

### Step 3. Analyze the Data

- Describe the customers' behavior.
- Find the minutes, texts, and volume of data required per month for users of each plan.
- Calculate and report the mean, variance, and standard deviation.
- Plot histograms and describe the distributions.

### Step 4. Test the Hypotheses

1. **Hypotheses**:
   - The average revenue from users of Ultimate and Surf calling plans differs.
   - The average revenue from users in the NY-NJ area is different from that of users from other regions.
2. **Hypothesis Testing**:
   - Choose an alpha value.
   - Formulate the null and alternative hypotheses.
   - Explain the criteria used to test the hypotheses and the rationale behind it.

### Step 5. Write an Overall Conclusion

- Summarize the findings of the analysis.
- Present conclusions based on the data analysis and hypothesis testing.

**Format**: Complete the task in a Jupyter Notebook. Include programming code in code cells and text explanations in markdown cells, applying appropriate formatting and headings.

### Data Description

**Megaline's Billing and Data Rounding Policy:**

- **Calls**: Megaline rounds seconds up to minutes. For calls, each individual call is rounded up; even if the call lasted just one second, it will be counted as one minute.
- **Web Traffic**: For web traffic, individual web sessions are not rounded up. Instead, the total for the month is rounded up. If someone uses 1025 megabytes in a month, they will be charged for 2 gigabytes.

**Data Tables Description:**

1. **The users table (data on users):**
   - `user_id` — unique user identifier
   - `first_name` — user's name
   - `last_name` — user's last name
   - `age` — user's age (years)
   - `reg_date` — subscription date (dd, mm, yy)
   - `churn_date` — the date the user stopped using the service (if missing, the plan was still active when the database was extracted)
   - `city` — user's city of residence
   - `plan` — calling plan name

2. **The calls table (data on calls):**
   - `id` — unique call identifier
   - `call_date` — call date
   - `duration` — call duration (in minutes)
   - `user_id` — the identifier of the user making the call

3. **The messages table (data on texts):**
   - `id` — unique text message identifier
   - `message_date` — text message date
   - `user_id` — the identifier of the user sending the text

4. **The internet table (data on web sessions):**
   - `id` — unique session identifier
   - `mb_used` — the volume of data spent during the session (in megabytes)
   - `session_date` — web session date
   - `user_id` — user identifier

5. **The plans table (data on the plans):**
   - `plan_name` — calling plan name
   - `usd_monthly_fee` — monthly charge in US dollars
   - `minutes_included` — monthly minute allowance
   - `messages_included` — monthly text allowance
   - `mb_per_month_included` — data volume allowance (in megabytes)
   - `usd_per_minute` — price per minute after exceeding the package limits
   - `usd_per_message` — price per text after exceeding the package limits
   - `usd_per_gb` — price per extra gigabyte of data after exceeding the package limits (1 GB = 1024 megabytes)

### Conclusion

Assumptions:
- Number of cancelled plans is negligible and won't skew data

Conclusions:
- Surf plan is almost twice as popular as Ultimate 
- Average revenue per user on Ultimate plan is more than Surf plan
- If price of additional 1gb for Surf is increased to $13 revenue from Surf will be almost equal to Ultimate (ttest p-value 0.6)

### Technologies Used
Python (Pandas, NumPy, SciPy, Matplotlib, Seaborn)
