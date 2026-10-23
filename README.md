# 1. Project Title
**Student Performance Analytics System**
By: [YASH KASAUDHAN]

# 2. Objective
The objective of this project is to build a Python-based system that reads raw student data and processes it to generate meaningful insights. It solves the problem of manually calculating student metrics by automating total marks, averages, grading, pass/fail identification, and class-wide analytics.

# 3. Technologies Used
* **Python**: Core programming language.
* **NumPy**: Used for efficient numerical calculations (sums, means, maximums).
* **Pandas**: Used for loading the dataset, organizing it into a DataFrame, and tabular data manipulation.

# 4. Dataset Description
The dataset (`students.csv`) contains 15 records of fictitious students. 
Important columns include `StudentID`, `Name`, `Department`, `Math`, `Physics`, `Chemistry`, and `Attendance`.

# 5. Implementation
1. **Data Loading**: Pandas was used to read `students.csv` into a DataFrame.
2. **Processing & Iteration**: A `for` loop was used with `df.iterrows()` to iterate through each student. 
3. **NumPy Operations**: Subject marks were converted into NumPy arrays to calculate the total and average marks.
4. **Functions**: Custom functions in `functions.py` evaluated the passing condition (>=40 per subject) and assigned letter grades based on average thresholds.
5. **Analysis**: Pandas filtering (`idxmax`, `nlargest`) and NumPy aggregations were used to identify top performers and class averages.

# 6. Key Features
* Automated calculation of totals and averages for each student.
* Automated letter grading (A, B, C, D, F).
* Iterative Pass/Fail checking for individual subjects.
* Subject-wise performance tracking.
* Identification of the top-performing students in the class.

# 7. Final Outcome
The project successfully processes raw CSV data to output a clean, readable set of metrics. It successfully answers practical questions about the dataset, such as identifying the class average and finding the students with the best performance.

# 8. Challenges & Learning
* **Challenge**: Integrating standard Python loops with optimized Pandas DataFrames without causing performance issues.
* **Solution**: Separated modular logic into a separate `functions.py` file to keep the iteration loop clean and readable.
* **Learning**: Gained practical experience in combining basic Python fundamentals with Pandas and NumPy for real-world data analysis tasks.

# 9. GitHub Repository
https://github.com/yashkasaudhan491-source/Student-Performance-Analytics.git