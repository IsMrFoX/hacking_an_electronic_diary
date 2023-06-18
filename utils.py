from datacenter.models import Schoolkid
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


def get_student(student_name):
    try:
        student = Schoolkid.objects.get(full_name__contains=student_name.title())
    except Schoolkid.MultipleObjectsReturned:
        print(f'Найдено более одного ученика с таким именем - "{student_name}", введите полное имя: ФИО')
        return
    except Schoolkid.ObjectDoesNotExist:
        print('Ученика с таким именем нет в базе данных')
        return
    return student