def computegrade(score):
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    return grade


marks = float(input('Enter score: '))
print(f'GRADE: {computegrade(marks)}')


