Проект для автоматизации рутины в Ogame.
В первую очередь создавался для сейва флота в случае атаки.

# Что умеет
Сейчас реализован скрипт, который каждые N минут проверяет, не нападает ли кто-то на нас.
Если нападает и до момента прилёта вражеского флота осталось меньше M минут, то запускается сейв флота:
берутся все корабли на планете, загружаются все ресурсы, которые влазят, и флот отправляется на минимальной скорости к другой 
нашей планете или в экспедицию (если у нас только одна планета). После этого флот помещается в очередь на возврат. Если 
планета больше не в опасности, миссия сейва отменяется и отправленный флот возвращается на исходную планету.

Также реализована возможность отправки уведомлений в телеграм бот (нужно создать свой)

# Как работает
Взаимодействие с игрой реализовано через работу с selenium webdriver. Очередь сейвов и возвратов флотов записывается в локальный файл базы данных sqlite3.

# Как запустить
1. Установить python >=3.6.4 (в момент разработки именно этот у меня установлен, на других не проверял, но на более последних должно работать)
https://www.python.org/
2. Установить pip (для установки пакетов зависимостей)
3. Скачать репозиторий
4. В терминале, находясь в корне репозитория, выполнить `pip install -r ./requirements.txt` (установка пакетов)
5. Установить переменные окружения для скриптов. Вот список переменных, используемых скриптами:
EMAIL - имейл вашей учётной записи игры
PASSWORD - пароль учётной записи
UNIVERSE - имя вселенной, игру в которой будет продолжать скрипт. Опционально. Если не указано, продолжиться последняя игра
HEADLESS - режим браузера, создаваемого скриптом. (True или False). 
Если False, то можно наглядно посмотреть, куда тыкает скрипт. Опционально. Значение по-умолчанию False
TELEGRAM_TOKEN - токен вашего бота в телеге. Если не указан, оповещения отправляться не будут.
TELEGRAM_BOT_CHAT_ID - айди чата, в который бот будет отправлять уведомления. Если не указан, оповещения отправляться не будут.
6. Добавить путь к корню репозитория в переменную окружения PYTHONPATH
7. В терминале, находясь в корне репозитория, выполнить `python ./Tests/SaveFleetTest.py`

# Предупреждение
Скрипты в этом проекте не являются абсолютной защитой от атак, так что не нужно полагаться исключительно на них. 
Взаимодействие с UI элементами довольно нестабильный способ, поэтому часто бывают исключения, следить за которыми удобно с помощью бота в телеге.
По возможности будет проводиться работа по улучшению.
