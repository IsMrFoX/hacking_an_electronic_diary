from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from datacenter.models import Schoolkid, Mark
from db_utils import get_student


def fix_marks(student):
    marks = Mark.objects.filter(schoolkid=student, points__in=[2, 3]).update(points=5)


def hack_marks(student_name):
    try:
        student = get_student(student_name)
    except (SyntaxError, AttributeError):
        print('Ошибка ввода, необходимо ввести имя ученика в кавычках, например: "Петров Максим".')
        return
    else:
        fix_marks(student)


if __name__ == "__main__":
    hack_marks()
