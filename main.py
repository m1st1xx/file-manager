from backend import app
from database import init_db
from database import init_new_db



if __name__ == "__main__":
    init_db()
    init_new_db()
    app.run(debug=False,host="0.0.0.0",port=5000)