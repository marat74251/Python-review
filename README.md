Это моё ревью по python
Запускается всё при помощи команды ". build.sh" которая прописывается в консоли в соответствующей папке.
У бота есть такие команды:
    /start - приветствует пользователя
    create - создает талблицу(бд) если её ещё нет
    parse - парсит сайт(данная функция сейчас работает некорректно она просто возвращает 1 заголовок, но так и должно быть так как этот сайт отвечает на сложный запрос лишь единожды и потом перестаёт это делать и я пока не нашёл как это решить)
    /get - выдаёт всё что мы напарсили(часто этого бывает слишком много)
    /vget -выдаёт всё то же самое что и /get только без id
    /clear - удаляет все данные из таблицы
чтобы завершить работу, выйдите из докера(нажмите ctrl+z в терминале) и запустите команду (sudo) docker-compose down
Если у вас при запуске контейнера пишет что порт уже занят, то вероятно что у вас уже запущена postgresql на вашем компьютере и вам надо её выключить. Для этого пропишите в терминале следующую команду: sudo service postgresql stop, далее бот должен запускаться без проблем
Ссылка на бота: https://t.me/Ahm_M_R_Python_review_bot