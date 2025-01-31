# **imei-check-bot**

## **Описание проекта**

`imei-check-bot` — это Telegram-бот, предназначенный для проверки IMEI номеров устройств через интеграцию с сервисом [IMEICheck](https://imeicheck.net/). Бот предоставляет пользователям информацию о валидности IMEI, статусе гарантии, блокировках и других характеристиках устройства. Проект разработан с использованием библиотеки `aiogram 3.x` для взаимодействия с Telegram API и `FastAPI` для предоставления API внешним сервисам.

---

## **Установка**

### **1. Локальная установка**

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/melixz/imei-check-bot.git
   cd imei-check-bot
   ```

2. **Настройте переменные окружения** в файле `.env`:

   ```env
   TELEGRAM_BOT_TOKEN=
   ALLOWED_USER_IDS=
   API_AUTH_TOKEN=some_random_token
   IMEICHECK_API_TOKEN=
   IMEICHECK_API_URL=https://api.imeicheck.net
   ```

3. **Установите зависимости через Poetry:**

   ```bash
   poetry install
   ```

4. **Запустите приложение:**

   ```bash
   poetry run python app/app/main.py
   ```

5. **Запустите FastAPI:**

   ```bash
   poetry run python /app/app/api.py
   ```
   
---

### **2. Установка через Docker**

1. **Запустите контейнер с помощью Docker Compose:**

   ```bash
   docker-compose up --build -d
   ```

---

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
