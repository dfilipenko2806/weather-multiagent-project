# Weather Multi-Agent System Проект демонстрирует многошаговый LLM-пайплайн с погодными агентами и интеграцией с OpenWeather API. ## Функционал * Получение погоды по городу * Интерпретация погоды агентом * Выбор вечернего досуга * Подбор еды для пикника с учётом ограничений * Рекомендации мест в городе * Рекомендации по одежде ## Установка 1. Клонируем репозиторий:
bash
git clone https://github.com/dfilipenko2806/weather-multiagent-project.git
cd weather-multiagent-project
2. Создаём виртуальное окружение:
bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
3. Устанавливаем зависимости:
bash
pip install -r requirements.txt
4. Создаём файл .env в корне проекта с ключами:
text
OPENWEATHER_KEY=ваш_ключ_OpenWeather
OPENAI_API_KEY=ваш_ключ_OpenAI
## Запуск сервера
bash
uvicorn app:app --reload
Сервер будет доступен по адресу: http://127.0.0.1:8000 ## Примеры API-запросов ### 1. Начало сессии
http
POST /start
Content-Type: application/json

{
  "city": "Minsk",
  "style_profile": "friendly"
}
Ответ:
json
{
  "session_id": "abc123",
  "weather_summary": "Солнечно, можно сходить на пикник..."
}
### 2. Выбор активности и дальнейшие шаги
http
POST /step
Content-Type: application/json

{
  "session_id": "abc123",
  "step": "food",
  "payload": {
    "activity": "пикник",
    "dislikes": "не люблю помидоры"
  }
}
Ответ: список еды и блюд для пикника. ## Docker (опционально) Собрать и запустить:
bash
docker build -t weather-agent .
docker run -p 8000:8000 --env-file .env weather-agent
## Переменные окружения * OPENWEATHER_KEY — ключ для OpenWeather API * OPENAI_API_KEY — ключ для OpenAI API ## Примечания * Для работы LLM-агентов нужен интернет и действующий OpenAI API ключ. * Можно выбрать разные стили общения агентов через параметр style_profile.