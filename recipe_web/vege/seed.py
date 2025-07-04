from faker import Faker
from django.db.models import Count
from vege.models import *
import random
fake = Faker()

def create_subject_marks():
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subjects = Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0,100)
                )
    except Exception as e:
        print(e)

def seed_db(n=10) -> None:
    try:
        for  i in range(0 , n):
            department_objs = Department.objects.all()
            random_index = random.randint(0,len(department_objs)-1)
            student_id = f'STU-0{random.randint(100 , 999)}'
            department = department_objs[random_index]
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id = student_id)

            student_obj = Student.objects.create(
                department = department,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)



def check_for_duplicate_student_ids():
    duplicates = Student.objects.values('student_id').annotate(id_count=Count('student_id')).filter(id_count__gt=1)
    if duplicates:
        print("Duplicate student IDs found:")
        for entry in duplicates:
            print(f"student_id: {entry['student_id']}, Count: {entry['id_count']}")
    else:
        print("No duplicate student IDs found.")

# check_for_duplicate_student_ids()
