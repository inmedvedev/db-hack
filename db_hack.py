from datacenter.models import Schoolkid, Chastisement, Commendation, Lesson, Mark
import random


def get_schoolkid(full_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=full_name)
        return child
    except (Schoolkid.MultipleObjectsReturned, Schoolkid.DoesNotExist):
        print (f"Учетная запись {full_name} не найдена, уточните имя")


def fix_marks(child):
    Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(points=4)


def remove_chastisements(child):
    Chastisement.objects.filter(schoolkid=child).delete()


def create_commendation(child, subject):
    lessons = Lesson.objects.filter(
        year_of_study=6,
        group_letter="А",
        subject__title__contains=subject
    )
    lesson = lessons.order_by('?').first()
    commendations = [
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!"
    ]
    Commendation.objects.create(
        teacher=lesson.teacher,
        subject=lesson.subject,
        schoolkid=child,
        created=lesson.date,
        text=random.choice(commendations)
    )
