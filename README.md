# Взламываем электронный дневник


Cкрипты для правки электронного дневника из репозитория
[e-diary](https://github.com/devmanorg/e-diary/tree/master).

Позволяет исправить оценки, убрать замечания и добавить похвалу.

# Как установить

Установите проект из [e-diary](https://github.com/devmanorg/e-diary/tree/master).

Поместите файл db_hack.py в директорию с проектом рядом с файлом manage.py.



# Как использовать


Запустите из директории проекта оболочку:
```bash
$ python3 manage.py shell
```
Далее импортируем функции:

```python
>>> from db_hack import *
```
Получаем учетную запись ученика, например Фролова Ивана:
```python
>>> schoolkid = get_schoolkid('Фролов Иван')
```

Меняем оценки:
```python
>>> fix_marks(schoolkid)
```
Убираем замечания:
```python
>>> remove_chastisements(schoolkid)
```
Добавляем похвалу:
```python
>>> create_commendation(schoolkid, 'Математика')
```
Скрипт сообщит об ошибке, если указаны неполные данные ученика:
```python
>>> schoolkid = get_schoolkid('Фроло')
Учетная запись не найдена
```

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DVMN.ORG](https://dvmn.org).

