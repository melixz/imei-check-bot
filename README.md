# **imei-check-bot**

## **Описание проекта**

`imei-check-bot` — это Telegram-бот, предназначенный для проверки IMEI номеров устройств через интеграцию с сервисом [IMEICheck](https://imeicheck.net/). Бот предоставляет пользователям информацию о валидности IMEI, статусе гарантии, блокировках и других характеристиках устройства. Проект разработан с использованием библиотеки `aiogram 3.x` для взаимодействия с Telegram API и `FastAPI` для предоставления API внешним сервисам.

---

## **Установка**

## 1. Установка зависимостей

**Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/melixz/imei-check-bot.git
   cd imei-check-bot
   ```

Перед запуском убедитесь, что у вас установлен [Poetry](https://python-poetry.org/docs/#installation).

```sh
poetry install
```

Если вы используете Docker, зависимости будут установлены автоматически в контейнере.

---

## 2. Запуск FastAPI

### 2.1 Запуск напрямую с Poetry

```sh
poetry run uvicorn app.app.api:app --host 0.0.0.0 --port 8000 --reload
```

### 2.2 Запуск через Docker

```sh
docker-compose up -d api
```

После этого API будет доступен по адресу: [http://localhost:8000](http://localhost:8000)

---

## 3. Запуск бота

### 3.1 Запуск напрямую с Poetry

```sh
poetry run python app/app/main.py
```

### 3.2 Запуск через Docker

```sh
docker-compose up -d bot
```

Бот начнёт слушать обновления.

---

## 4. Полный запуск через Docker

```sh
docker-compose up -d
```

Это запустит и API, и бота.

---

## 5. Остановка

Остановить сервисы можно командой:

```sh
docker-compose down
```

Или только API:

```sh
docker-compose stop api
```

Или только бота:

```sh
docker-compose stop bot
```

---

## 6. Makefile

Также можно использовать короткие команды Make:

- `make install` – установить зависимости.
- `make up` – запустить весь проект в Docker.
- `make down` – остановить контейнеры.
- `make restart` – перезапустить контейнеры.
- `make logs` – просмотреть логи всех сервисов.
- `make api` – запустить только API.
- `make bot` – запустить только бота.

## **Технологии**

Проект разработан с использованием следующих технологий:

- **Python 3.12+**
- **aiogram 3.x**
- **FastAPI**
- **aiohttp**
- **Pydantic**
- **Docker и Docker Compose**

---

## **Возможности**

- **Проверка IMEI номеров** через Telegram-бот.
- **API для внешних сервисов** с авторизацией по токену.
- **Защита функционала бота** с использованием белого списка пользователей.

---

## **Использование**

### **Использование бота**

1. Запустите бота через Telegram. Попробуйте команду /start !
2. Отправьте IMEI номер для проверки:
   ```
   353272491542872
   ```
3. Бот ответит информацией о статусе устройства.

**Пример ответа:**

```
   Результат проверки IMEI:
IMEI: 353272491542872
MEID: 35327249154287
Serial: YN0OPHSXT0
Warranty Status: Out Of Warranty
Sim Lock: Yes
GSMA Blacklisted: No
```

---

### **Использование API**

**Эндпоинт:** `POST /api/check-imei`

**Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)

**Пример тела запроса:**

```json
{
  "imei": "353272491542872",
  "serviceId": 12
}
```

**Пример ответа:**

```json
{
  "id": "Ny3Gievp1alumCvk",
  "type": "api",
  "status": "successful",
  "service": {
    "id": 12,
    "title": "Mock service with only successful results"
  },
  "properties": {
    "deviceName": "POCO X3 Pro",
    "imei": "353272491542872",
    "serial": "XXB58K584VX",
    "gsmaBlacklisted": true,
    "simLock": false,
    "warrantyStatus": "AppleCare Protection Plan"
  }
}
```

## **Ссылки**

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---
