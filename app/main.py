from flask import Flask, render_template, request

app = Flask(__name__)

# Список вопросов и ответов
questions = (
    [
        {
            "question": "Какой ваш любимый язык программирования?",
            "answers": [
                "Python",
                "C++",
                "Java",
                "JavaScript",
            ],
        },
        {
            "question": "Почему вам нравится программировать?",
            "answers": [
                "Для развития",
                "Для работы",
                "Для удовольствия",
            ],
        },
        {
            "question": "Вы любите животных?",
            "answers": [
                "Да",
                "Нет",
            ],
        },
    ],
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_answers = request.form.to_dict()
        return render_template("result.html", user_answers=user_answers)

    for idx, question in enumerate(questions):
        question["id"] = idx + 1  # Индексация с 1

    return render_template("index.html", questions=questions)


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
