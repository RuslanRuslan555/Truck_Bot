from fastapi import FastAPI

app = FastAPI()


drivers = [
    {"id": 1, "name": "Ali", "status": "ready", "location": "Texas", "truck": "Volvo"},
    {"id": 2, "name": "Tom", "status": "intransit", "location": "Nevada", "truck": "Freightliner"},
    {"id": 3, "name": "Sara", "status": "offduty", "location": "Utah", "truck": "Kenworth"},
    {"id": 4, "name": "John", "status": "ready", "location": "California", "truck": "Peterbilt"},
    {"id": 5, "name": "Ivan", "status": "upcoming", "location": "New York", "truck": "International"}
]

@app.get("/")
def welcome_message():
    return{"message":"Так по приколу пусть будет"}

@app.get("/drivers")
def get_average():
    filtered = [
        d for d in drivers if d['status'] in ['ready', 'upcoming']]
    result = [f"Driver: {d['name']} - {d['status']} - {d['location']} - {d['truck']}" for d in filtered
              ]
    return{"drivers": result}
