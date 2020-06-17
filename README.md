# dissertation
 My thesis

Информационная система мониторинга требований к IT-специалистам на примере программиста

Файл - предназначение:

1. db_standard.py - файл для работы с базой данных
2. parser_language.py - файл для соотнесения навыков из вакансий и видов деятельности из профессионального стандарта
3. pro.py - основной файл. Находит необходимые профессиональные стандарты и извлекает требования из них
4. server.py - файл для работы с вебом

В базе данных (standard.sql) есть таблицы по умолчанию:
1. prof_area - таблица для хранения данных о профессиональных областях профессиональных стандартов
2. professional_activity - таблица для хранения данных о видах деятельности со стороны вакансий
3. activityps_activityvac - таблица для хранения данных о соединениях между видами деятельности со стороны вакансий и видами деятельности профессионального стандарта
4. education - таблица для хранения данных об образовании