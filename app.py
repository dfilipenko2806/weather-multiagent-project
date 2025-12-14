from fastapi import FastAPI, HTTPException
"city": req.city,
"weather_raw": weather_raw,
"weather_text": weather_text
}


return {"session_id": sid, "weather_summary": weather_text}


@app.post('/step')
async def step(choice: StepChoice):
sid = choice.session_id
if sid not in SESSIONS:
raise HTTPException(status_code=404, detail='Session not found')


if choice.step == 'leisure':
res = leisure_agent(
SESSIONS[sid]['weather_text'],
choice.payload.get('choice', ''),
style=choice.payload.get('style', 'friendly')
)
SESSIONS[sid]['last_leisure'] = res
return {"leisure": res}


if choice.step == 'food':
res = food_agent(
choice.payload.get('activity', ''),
choice.payload.get('dislikes', ''),
style=choice.payload.get('style', 'friendly')
)
SESSIONS[sid]['last_food'] = res
return {"food": res}


if choice.step == 'location':
res = location_agent(
SESSIONS[sid]['city'],
choice.payload.get('activity', ''),
style=choice.payload.get('style', 'neutral')
)
SESSIONS[sid]['last_location'] = res
return {"location": res}


if choice.step == 'outfit':
res = outfit_agent(
SESSIONS[sid]['weather_text'],
SESSIONS[sid].get('last_location', ''),
choice.payload.get('activity', ''),
style=choice.payload.get('style', 'romantic')
)
SESSIONS[sid]['last_outfit'] = res
return {"outfit": res}


raise HTTPException(status_code=400, detail='Unknown step')


if __name__ == '__main__':
import uvicorn
uvicorn.run(app, host='0.0.0.0', port=8000)