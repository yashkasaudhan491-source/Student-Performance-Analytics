import numpy as np

def calculate_total_and_average(marks_array):
    """Calculates the total and average marks using NumPy[span_5](start_span)[span_5](end_span)."""
    total = np.sum(marks_array)
    average = np.mean(marks_array)
    return total, average

def assign_grade(average):
    """Assigns a grade based on clearly defined average thresholds[span_6](start_span)[span_6](end_span)."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def check_pass_fail(marks_array, passing_mark=40):
    """Uses a loop to check if a student passed all subjects[span_7](start_span)[span_7](end_span)."""
    for mark in marks_array:
        if mark < passing_mark:
            return 'Fail'
    return 'Pass'