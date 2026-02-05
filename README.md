# 🇩🇪 Data Analytics Job Market in Germany (2023)

## Project Overview

This project provides a comprehensive, data-driven analysis of the **German Data Analytics job market in 2023**, using job posting data provided by **Luke Barousse**. The analysis focuses on the three most popular data roles:

* **Data Analyst**
* **Data Scientist**
* **Data Engineer**

The project consists of **five Jupyter Notebooks**, each examining a different dimension of the market: overall demand, skill requirements, skill trends, salary insights, and optimal skill combinations. All insights are supported by **interactive Plotly visualizations** to enable intuitive and impactful exploration of the data.

---

## Project Goals

The main objectives of this project are to:

* Understand which data roles are most in demand in Germany
* Identify key hiring cities and geographic concentration
* Analyze job characteristics such as contract type, remote work, degree requirements, and salary transparency
* Explore in-demand skills, their evolution over time, and their relationship with salaries
* Provide actionable insights for aspiring and experienced data professionals targeting the German market

---

## Dataset

* **Source:** Luke Barousse – Data Jobs Dataset
* **Region:** Germany
* **Year:** 2023
* **Total Job Postings:** 27,694
* **Primary Roles Analyzed:** Data Analyst, Data Scientist, Data Engineer

---

## Notebook Structure & Key Insights

### 1️⃣ EDA Intro – German Data Job Market Overview

**Research Questions**

* What are the most popular data jobs in Germany?
* Which cities have the highest number of data job offers?
* What are the defining characteristics of the German data job market?

**Scope**
A high-level exploratory analysis focused on the three most popular roles: Data Analyst, Data Scientist, and Data Engineer.

**Key Insights**

* **Top Hiring Cities:** Berlin, Munich, and Hamburg
  A significant share of postings list the location as *unspecified*, likely reflecting companies with multiple offices or flexible location policies.

* **Employment Type:**

  * 93.7% of positions are offered as full-time
  * Many roles allow later adjustment to part-time
  
### 📊 1.2. Distribution Of Job Contract Types In Germany

![1.2. Distribution of Job Contract Types in Germany](Germany_Data_Market_notebooks/docs/images/1.2.%20Distribution%20of%20Job%20Contract%20Types%20in%20Germany_preview.png)
*Click image to view full size*

[📥 Download full resolution PNG](Germany_Data_Market_notebooks/docs/images/1.2.%20Distribution%20of%20Job%20Contract%20Types%20in%20Germany.png) | 
[🔗 View interactive HTML](Germany_Data_Market_notebooks/docs/images/1.2.%20Distribution%20of%20Job%20Contract%20Types%20in%20Germany.html)

* **Remote Work:**

  * Only 4.4% of roles are fully remote
  * Strong preference for on-site or hybrid work models

* **Education Requirements:**

  * 55.2% of roles require a university degree
  * Nearly 45% of jobs are accessible without a degree, given the right skills

* **Salary Transparency:**

  * Only 0.6% of job postings disclose a salary range

* **Top Hiring Companies:**

  * Workwise
  * Deutsche Bahn
  * E.ON Energie Deutschland

**Candidate Profile – Best Market Fit**
The strongest candidates in 2023 are those who:

* Live in or are willing to relocate to Berlin, Munich, or Hamburg
* Are open to hybrid or fully on-site work
* Proactively research and negotiate salaries
* Hold a university degree (beneficial but not mandatory)
* Value contract flexibility, including part-time options

---

### 2️⃣ In-Demand Skills – Role-Based Skill Demand

This notebook analyzes how often specific skills appear in job postings, segmented by role.

**Data Analyst – Top Skills**

* SQL: 2,947 postings (41.3%)
* Python: 2,309 postings (32.4%)
* Tableau: 1,366 postings (19.2%)

**Data Engineer – Top Skills**

* Python: 3,524 postings (52.8%)
* SQL: 3,145 postings (47.1%)
* Azure: 1,961 postings (29.4%)

**Data Scientist – Top Skills**

* Python: 4,157 postings (61.6%)
* SQL: 2,137 postings (31.7%)
* R: 1,795 postings (26.6%)

### 📊 2.2. Likelihood Of Top Data Skills In Job Postings In Germany

![2.2. Likelihood of Top Data Skills in Job Postings in Germany](Germany_Data_Market_notebooks/docs/images/2.2.%20Likelihood%20of%20Top%20Data%20Skills%20in%20Job%20Postings%20in%20Germany_preview.png)
*Click image to view full size*

[📥 Download full resolution PNG](Germany_Data_Market_notebooks/docs/images/2.2.%20Likelihood%20of%20Top%20Data%20Skills%20in%20Job%20Postings%20in%20Germany.png) | 
[🔗 View interactive HTML](Germany_Data_Market_notebooks/docs/images/2.2.%20Likelihood%20of%20Top%20Data%20Skills%20in%20Job%20Postings%20in%20Germany.html)

**Conclusion**

* Python and SQL dominate across all roles
* Python is especially critical for Data Engineers and Data Scientists
* SQL is particularly important for Data Analysts

**Role Differentiators**

* **Data Scientist:** R, machine learning, cloud skills
* **Data Engineer:** cloud platforms and infrastructure tools
* **Data Analyst:** visualization tools (Tableau, Power BI) and Excel

---

### 3️⃣ Skills Trend – Demand Evolution Over 2023

This notebook examines monthly changes in skill demand percentages throughout 2023.

**Key Findings**

* Python remained the most in-demand skill throughout the year

  * Lowest demand: 54.7% (September)
  * Highest demand: 66.7% (July)

* SQL ranked second

  * Highest demand: 36.8% (May)
  * Lowest demand: 23.9% (December)

### 📊 3.1. Data Jobs Germany - Top Skills Trends.Png

![3.1. Data Jobs Germany - Top Skills Trends.png](Germany_Data_Market_notebooks/docs/images/3.1.%20Data%20Jobs%20Germany%20-%20Top%20Skills%20Trends.png_preview.png)
*Click image to view full size*

[📥 Download full resolution PNG](Germany_Data_Market_notebooks/docs/images/3.1.%20Data%20Jobs%20Germany%20-%20Top%20Skills%20Trends.png.png) | 
[🔗 View interactive HTML](Germany_Data_Market_notebooks/docs/images/3.1.%20Data%20Jobs%20Germany%20-%20Top%20Skills%20Trends.png.html)

**Insight**
These trends further confirm Python and SQL as core entry skills for breaking into the German data job market.

---

### 4️⃣ Salary Analysis – Limited but Insightful

**Disclaimer**
Salary data availability in Germany is extremely limited and should not be interpreted as a full market trend.

**Salary Data Coverage**

* Total job postings: 27,694
* Job postings with salary data: 257 (0.93%)
* Missing salary data: 99.07%

**Roles Included**

* Data Analyst
* Data Scientist
* Data Engineer
* Senior Data Analyst
* Senior Data Scientist
* Senior Data Engineer
* Machine Learning Engineer

**Key Findings**

* Highest median salary: **Senior Data Scientist – €157,500/year**
* Lowest median salary: **Machine Learning Engineer – €89,100/year**
* Data Scientist shows the widest salary range:

  * From ~€50,000 to nearly €180,000
  
### 📊 4.1. Salary Distribution By Job Title In Germany.Png

![4.1. Salary Distribution by Job Title in Germany.png](Germany_Data_Market_notebooks/docs/images/4.1.%20Salary%20Distribution%20by%20Job%20Title520in%20Germany.png_preview.png)
*Click image to view full size*

[📥 Download full resolution PNG](Germany_Data_Market_notebooks/docs/images/4.1.%20Salary%20Distribution%20by%20Job%20Title520in%20Germany.png.png) | 
[🔗 View interactive HTML](Germany_Data_Market_notebooks/docs/images/4.1.%20Salary%20Distribution%20by%20Job%20Title520in%20Germany.png.html)

**Interpretation**
The wide salary range reflects varying job complexity—from Excel-focused roles to positions requiring deep expertise in machine learning and neural networks. The Machine Learning Engineer role remains relatively new and is expected to evolve significantly with the rise of AI.

---

### 5️⃣ Optimal Skills – Salary vs Demand

This notebook combines skill demand with salary data to identify high-value skills.

**Key Insights**

* **Programming languages dominate higher-paying roles:**

  * Python: appears in 53.7% of jobs with salary data (median ~€115,883)
  * SQL: appears in 41.2% (median ~€111,175)

* **Excel:**

  * Appears in only 7.4% of salaried postings
  * Median salary ~€89,100

* **High-paying niche skills:**

  * Snowflake and Kubernetes appear in <8% of postings
  * Median salaries exceed €140,000

### 📊 5.1. Optimal Skills For Data Jobs In Germany.Png

![5.1. Optimal Skills for Data Jobs in Germany.png](Germany_Data_Market_notebooks/docs/images/5.1.%20Optimal%20Skills%20for%20Data%20Jobs%20in%20Germany.png_preview.png)
*Click image to view full size*

[📥 Download full resolution PNG](Germany_Data_Market_notebooks/docs/images/5.1.%20Optimal%20Skills%20for%20Data%20Jobs%20in%20Germany.png.png) | 
[🔗 View interactive HTML](Germany_Data_Market_notebooks/docs/images/5.1.%20Optimal%20Skills%20for%20Data%20Jobs%20in%20Germany.png.html)

**Conclusion**
Advanced programming and cloud skills offer a higher return on investment compared to traditional tools like Excel.

---

## Selected Code Snippets (Portfolio Highlights)

The following snippets are selected examples from the notebooks that illustrate the core analytical logic behind the insights.

### 1️⃣ Market Overview – Top Hiring Cities

```python
# Count job postings by location for top data roles

top_cities = (
    df_germany
    .query("job_title_short in ['Data Analyst', 'Data Scientist', 'Data Engineer']")
    .groupby('job_location')
    .size()
    .sort_values(ascending=False)
    .head(10)
    .reset_index(name='job_count')
)
```

This aggregation forms the basis for identifying Berlin, Munich, and Hamburg as the dominant hiring hubs.

---

### 2️⃣ In-Demand Skills – Exploding Skill Lists

```python
# Explode skill lists and count frequency by role

df_skills_exploded = (
    df_germany
    .explode('job_skills')
    .drop_duplicates(['job_key', 'job_skills'])
)

skills_by_role = (
    df_skills_exploded
    .groupby(['job_title_short', 'job_skills'])
    .size()
    .reset_index(name='skill_count')
    .sort_values('skill_count', ascending=False)
)
```

This transformation enables a role-specific comparison of skill demand, revealing Python and SQL as universal core skills.

---

### 3️⃣ Skill Demand Trends – Monthly Percentages

```python
# Extract posting month and calculate skill demand over time

df_germany['posted_month'] = df_germany['job_posted_date'].dt.month

monthly_skill_trends = (
    df_skills_exploded
    .groupby(['posted_month', 'job_skills'])
    .size()
    .groupby(level=0)
    .apply(lambda x: x / x.sum() * 100)
    .reset_index(name='skill_percentage')
)
```

This logic supports the trend analysis showing Python peaking at 66.7% demand during mid-2023.

---

### 4️⃣ Interactive Visualization – Plotly Example

```python
fig = px.line(
    monthly_skill_trends.query("job_skills in ['Python', 'SQL']"),
    x='posted_month',
    y='skill_percentage',
    color='job_skills',
    title='Monthly Demand for Core Data Skills (Germany, 2023)',
)
fig.update_layout(yaxis_title='Percentage of Job Postings')
fig.show()
```

Plotly is used throughout the project to deliver interactive, recruiter-friendly visuals that clearly communicate trends and comparisons.

---

## Tools & Technologies

* Python
* Pandas & NumPy – data processing
* Plotly – interactive visualizations
* Jupyter Notebook – exploratory analysis

---

## Final Takeaway

Germany’s 2023 data job market is highly concentrated in major cities, strongly office-oriented, and low in salary transparency. However, it remains accessible to skilled professionals without formal degrees and offers strong long-term potential—especially for those investing in Python, SQL, and cloud technologies.

This project provides a structured, evidence-based overview to help data professionals make informed career decisions in the German market.
