students = {
    'Alice': {
        'Mathematiques': 90,
        'Francais': 80,
        'Histoire': 95
    },
    'Bob': {
        'Mathematiques': 75,
        'Francais': 85,
        'Histoire': 70
    },
    'Charlie': {
        'Mathematiques': 88,
        'Francais': 92,
        'Histoire': 78
    }
}

average = 0
student_name = input("Entrez le nom de l’étudiant:  ")
if student_name in students:
    for classroom, note in students[student_name].items():
        print(f"Notes de <nom de l’étudiant> : {classroom} : {note}")
        average = note + average
    print(f"Moyenne de {student_name} : {round(average / 3, 2)}")
else:
    print(f"L'étudiant {student_name} n'existe pas dans la liste.")
