from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import Schoolkid, Mark

def fix_marks(student):
    marks = Mark.objects.filter(schoolkid=student, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()

def hack_marks(student_name):
    try:
        student = Schoolkid.objects.get(full_name__contains=student_name.title())
    except MultipleObjectsReturned:
        print(f'Найдено более одного ученика с таким именем - "{student_name}", введите полное имя: ФИО')
        return
    except ObjectDoesNotExist:
        print('Ученика с таким именем нет в базе данных')
        return
    except (SyntaxError, AttributeError):
        print('Ошибка ввода, необходимо ввести имя ученика в кавычках, например: "Петров Максим".')
        return
    else:
        fix_marks(student)


if __name__ == "__main__":
    hack_marks()
