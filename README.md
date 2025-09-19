# Sendwich
Minimal GET-only HTTP server with basic auth

## Описание проекта
Легкий локальный HTTP сервер для однонаправленной передачи файлов
 - Только GET: файлы можно только забирать, ничего не загружается
 - Минимум зависимостей, работает на python3
 - Базовая авторизация: логин и пароль генерируются при запуске
 - Трафик **не шифруется**, используйте только на localhost/host-only

## Запуск программы 

```bash
python3 server.py [порт]
```
<img width="383" height="103" alt="{C74279FB-264D-4F8F-AFDD-5B7F1A546EA2}" src="https://github.com/user-attachments/assets/36fc2b1d-2313-4678-a116-4f94389ebd04" />

<img width="302" height="184" alt="{FE642E59-BDD9-4BB0-BF42-BE5BAFE5B220}" src="https://github.com/user-attachments/assets/504cbb78-04ab-4ea1-9b94-c5b03076e016" />

По умолчанию порт **17032**

После запуска сервер доступен через браузер. IP и порт зависят от машины и аргумента запуска, поэтому используйте их напрямую (например, http://127.0.0.1:17032/)
