from datacenter.models import Chastisement, Subject, Commendation, Lesson
from random import choice
from utils import get_student


EXAMPLES_OF_PRAISE = [
    'Молодец!',
    'Отлично',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!',
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def remove_chastisement(studunt):
    chastisements = Chastisement.objects.filter(schoolkid=studunt)
    chastisements.delete()


def create_commendation(student, subject, last_lesson):
    commendation = Commendation.objects.create(
        text=choice(EXAMPLES_OF_PRAISE),
        created=(Lesson.objects.filter(group_letter=student.group_letter, subject=subject).order_by("-date").first()).date,
        schoolkid=student,
        subject=subject,
        teacher=last_lesson.teacher
    )


def update_chastisements(student_name, lesson):
    try:
        student = get_student(student_name)
        if student is None:
            return
        subject = Subject.objects.filter(
            title=lesson.capitalize(),
            lesson__group_letter=student.group_letter,
            year_of_study=student.year_of_study).first()
        if subject is None:
            print(f'''Предмета с названием - "{lesson}" нет в базе данных, либо найдено более одного предмета с названием - "{lesson}", проверьте ваш ввод''')
            return
        last_lesson = Lesson.objects.filter(
            group_letter=student.group_letter,
            subject=subject
        ).order_by("-date").first()
        if last_lesson is None:
            print(f'Не найдено занятий по предмету - "{lesson}", проверьте ваш ввод')
            return
    except (SyntaxError, AttributeError):
        print('''Ошибка ввода, необходимо ввести имя ученика и название предмета через запятую в кавычках, пример: 
update("Петров Максим", "Математика")''')
        return
    remove_chastisement(student)
    create_commendation(student, subject, last_lesson)


if __name__ == "__main__":
    update_chastisements()
