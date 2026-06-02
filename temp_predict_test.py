from app import create_app
from app.services.predictor_service import model, symptom_columns, MODEL_PATH, SYMPTOM_PATH

print('MODEL_PATH', MODEL_PATH)
print('SYMPTOM_PATH', SYMPTOM_PATH)
print('model loaded', model is not None)
print('symptom_columns len', len(symptom_columns) if symptom_columns is not None else None)

app = create_app()
client = app.test_client()
resp = client.post('/api/predict', json={
    'age': '30',
    'gender': 'Male',
    'city': 'Dehradun',
    'symptoms': 'fever, cough',
    'stress': 'Low',
    'anxiety': 'Low',
    'sleep': 'Normal'
})
print('status', resp.status_code)
print(resp.get_data(as_text=True))
