from app import app
from flask import send_file
@app.route('/books')
def download():
    try:
        path = "books.json"
        return send_file(path, as_attachment=True)
    except Exception as e:
        return str(e)
