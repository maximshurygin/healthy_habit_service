# Проект атомных привычек

## Модели

### Привычка
- **Пользователь:** Создатель привычки.
- **Место:** Место, в котором необходимо выполнять привычку.
- **Время:** Время, когда необходимо выполнять привычку.
- **Действие:** Действие, которое представляет из себя привычка.
- **Признак приятной привычки:** Привычка, которую можно привязать к выполнению полезной привычки.
- **Связанная привычка:** Привычка, которая связана с другой привычкой. Важно указывать для полезных привычек, но не для приятных.
- **Периодичность (по умолчанию ежедневная):** Периодичность выполнения привычки для напоминания в днях.
- **Вознаграждение:** Чем пользователь должен себя вознаградить после выполнения.
- **Время на выполнение:** Время, которое предположительно потратит пользователь на выполнение привычки.
- **Признак публичности:** Привычки можно публиковать в общий доступ.

## Валидаторы

- Исключить одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

## Пагинация

- Для вывода списка привычек реализована пагинация с выводом по 5 привычек на страницу.

## Права доступа

- Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
- Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.

## Эндпоинты

- **Регистрация**
- **Авторизация**
- **Список привычек текущего пользователя с пагинацией**
- **Список публичных привычек**
- **Создание привычки**
- **Редактирование привычки**
- **Удаление привычки**
