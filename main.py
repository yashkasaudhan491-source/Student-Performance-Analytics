import pandas as pd
import numpy as np
import functions as fn

def main():
    # Step 2: Read the Data[span_9](start_span)[span_9](end_span)
    print("Loading dataset...")
    df = pd.read_csv('students.csv')
    
    # Check basic info[span_10](start_span)[span_10](end_span)
    print("\n--- Basic Dataset Information ---")
    print(f"Total Records: {len(df)}")
    print(f"Columns: {', '.join(df.columns)}")

    # Step 3: Process the Data[span_11](start_span)[span_11](end_span)
    totals = []
    averages = []
    grades = []
    statuses = []

    # Iterating through the DataFrame using a loop as required[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span)
    for index, row in df.iterrows():
        # Create a NumPy array for the subject marks
        marks = np.array([row['Math'], row['Physics'], row['Chemistry']])
        
        # Apply reusable functions
        total, avg = fn.calculate_total_and_average(marks)
        grade = fn.assign_grade(avg)
        status = fn.check_pass_fail(marks)
        
        totals.append(total)
        averages.append(avg)
        grades.append(grade)
        statuses.append(status)

    # Add processed data back to the Pandas DataFrame[span_14](start_span)[span_14](end_span)
    df['Total'] = totals
    df['Average'] = averages
    df['Grade'] = grades
    df['Status'] = statuses

    print("\n--- Sample Processed Data ---")
    print(df[['Name', 'Total', 'Average', 'Grade', 'Status']].head())

    # Step 4: Perform Analysis[span_15](start_span)[span_15](end_span)
    print("\n--- Practical Analysis Answers ---")
    
    # Which student has the highest average?[span_16](start_span)[span_16](end_span)
    top_student = df.loc[df['Average'].idxmax()]
    print(f"Highest Average: {top_student['Name']} with {top_student['Average']:.2f}")

    # Lowest performance[span_17](start_span)[span_17](end_span)
    lowest_student = df.loc[df['Average'].idxmin()]
    print(f"Lowest Average: {lowest_student['Name']} with {lowest_student['Average']:.2f}")

    # What is the overall class average?[span_18](start_span)[span_18](end_span)
    class_average = np.mean(df['Average'])
    print(f"Overall Class Average: {class_average:.2f}")

    # How many students passed?[span_19](start_span)[span_19](end_span)
    pass_count = len(df[df['Status'] == 'Pass'])
    fail_count = len(df[df['Status'] == 'Fail'])
    print(f"Pass/Fail Statistics: {pass_count} Passed, {fail_count} Failed")

    # Which subject has the best average? (Subject-wise performance)[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span)
    print("\n--- Subject-wise Performance ---")
    subjects = ['Math', 'Physics', 'Chemistry']
    for sub in subjects:
        sub_avg = np.mean(df[sub])
        sub_max = np.max(df[sub])
        print(f"{sub} -> Average: {sub_avg:.2f}, Highest: {sub_max}")

    # Identify top-performing students[span_22](start_span)[span_22](end_span)
    print("\n--- Top 3 Performing Students ---")
    top_3 = df.nlargest(3, 'Average')[['Name', 'Department', 'Average', 'Grade']]
    print(top_3.to_string(index=False))

if __name__ == "__main__":
    main()