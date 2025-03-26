from app_runner import create_app
from models.questions import Question, Statistic
from models.answers import Answer
from models.category import Category


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
