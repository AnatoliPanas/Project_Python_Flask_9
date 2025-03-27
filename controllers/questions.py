from models.questions import Question
from models import db
from schemas.quastions import QuestionCreate


def get_all_questions() -> list[dict[str, int | str]]:
    questions = Question.query.all()
    questions_data = [
        {
            "id": question.id,
            "text": question.text
        }
        for question in questions
    ]

    return questions_data

def create_new_question(raw_data: dict[str, str]) -> Question:
    validated_obj = QuestionCreate.model_validate(raw_data)

    new_obj = Question(text=validated_obj.text)

    db.session.add(new_obj)
    db.session.commit()

    return new_obj

def get_questions_by_id(id: int) -> Question:
    question = Question.query.get(id)
    return question

def update_question(obj, new_data):
    obj.text = new_data["text"]
    db.session.commit()

    return obj
