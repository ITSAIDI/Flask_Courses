from main import app

app.run(host='0.0.0.0', port=5000)

# pip freeze > requirements.txt
# In render
# pip install -r requirements.txt && cd ../Frontend && npm install && npm run build
# gunicorn wsgi:app