import os
]
resp = openai.ChatCompletion.create(
model="gpt-4o-mini",
messages=messages,
temperature=temperature,
max_tokens=max_tokens,
)
return resp.choices[0].message.content.strip()


SYSTEM_TEMPLATES = {
"weather": {
"friendly": "Ты — дружелюбный погодный ассистент. Кратко интерпретируй погоду и предложи варианты вечернего досуга.",
"business": "Ты — формальный погодный аналитик. Дай точную сводку и варианты активности."
},
"leisure": {
"friendly": "Ты — советчик по досугу. Опиши выбранную активность подробнее и дай советы.",
},
"food": {
"friendly": "Ты — кулинарный ассистент. Дай список еды и блюд для пикника с учётом ограничений.",
},
"location": {
"neutral": "Ты — локальный гид. Дай 3 места для пикника в указанном городе.",
},
"outfit": {
"romantic": "Ты — стилист. Дай рекомендации по одежде в романтичном стиле.",
}
}


def weather_agent(weather_raw: dict, style: str = "friendly") -> str:
sys = SYSTEM_TEMPLATES["weather"].get(style, SYSTEM_TEMPLATES["weather"]["friendly"])
user = f"Вот данные погоды: {weather_raw}. Дай интерпретацию и предложи 5 вариантов досуга."
return llm_call(sys, user)


def leisure_agent(weather_summary: str, chosen: str, style: str = "friendly") -> str:
sys = SYSTEM_TEMPLATES["leisure"][style]
user = f"Погода: {weather_summary}. Пользователь выбрал: {chosen}. Дай расширенные рекомендации."
return llm_call(sys, user)


def food_agent(activity: str, dislikes: str, style: str = "friendly") -> str:
sys = SYSTEM_TEMPLATES["food"][style]
user = f"Активность: {activity}. Ограничения: {dislikes}. Дай список еды."
return llm_call(sys, user)


def location_agent(city: str, activity: str, style: str = "neutral") -> str:
sys = SYSTEM_TEMPLATES["location"][style]
user = f"Город: {city}. Активность: {activity}. Предложи места."
return llm_call(sys, user)


def outfit_agent(weather_summary: str, place_summary: str, activity: str, style: str = "romantic") -> str:
sys = SYSTEM_TEMPLATES["outfit"][style]
user = f"Погода: {weather_summary}. Место: {place_summary}. Активность: {activity}. Дай рекомендации по одежде."
return llm_call(sys, user)