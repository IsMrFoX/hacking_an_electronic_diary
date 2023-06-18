from datacenter.models import Schoolkid, Chastisement, Subject, Commendation, Lesson
from random import choice


def remove_chastisement(studunt):
    chastisements = Chastisement.objects.filter(schoolkid=studunt)
    chastisements.delete()


def create_commendation(student, subject, last_lesson):
    examples_of_praise = [
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
    commendation = Commendation.objects.create(
        text=choice(examples_of_praise),
        created=(Lesson.objects.filter(group_letter=student.group_letter, subject=subject).order_by("-date").first()).date,
        schoolkid=student,
        subject=subject,
        teacher=last_lesson.teacher
    )


def update_chastisements(student_name, lesson):
    try:
        student = Schoolkid.objects.get(full_name__contains=student_name.title())
        subject = Subject.objects.filter(
            title=lesson.capitalize(),
            lesson__group_letter=student.group_letter,
            year_of_study=student.year_of_study
        ).first()
        last_lesson = Lesson.objects.filter(
            group_letter=student.group_letter,
            subject=subject
        ).order_by("-date").first()
        if last_lesson is None:
            print(f'Не найдено занятий по предмету - "{lesson}", проверьте ваш ввод')
            return
    except Subject.DoesNotExist:
        print(f'Предмета с названием - "{lesson}" нет в базе данных, проверьте ваш ввод')
        return
    except Subject.MultipleObjectsReturned:
        print(f'Найдено более одного предмета с названием - "{lesson}", введите название предмета полностью')
        return
    except Lesson.DoesNotExist:
        print(f'Не найдено занятий по предмету - "{lesson}" для ученика "{student.full_name}"')
        return
    except (SyntaxError, AttributeError):
        print('''Ошибка ввода, необходимо ввести имя ученика и название предмета через запятую в кавычках, пример: 
update("Петров Максим", "Математика")''')
        return
    remove_chastisement(student)
    create_commendation(student, subject, last_lesson)


if __name__ == "__main__":
    update_chastisements()
