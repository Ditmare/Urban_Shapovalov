grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3],
          [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(list(students)) #сортирую по алфавиту, перевожу в список, так как нужно упорядочить
student_grades = list(zip(students_list, grades)) #с помощью zip овместил 2 списка
sred_grades = {
    student_grades[0][0]: sum(student_grades[0][1]) / len(student_grades[0][1]),
    student_grades[1][0]: sum(student_grades[1][1]) / len(student_grades[1][1]),
    student_grades[2][0]: sum(student_grades[2][1]) / len(student_grades[2][1]),
    student_grades[3][0]: sum(student_grades[3][1]) / len(student_grades[3][1]),
    student_grades[4][0]: sum(student_grades[4][1]) / len(student_grades[4][1]),
}
print(sred_grades)