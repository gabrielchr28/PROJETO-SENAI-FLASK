from flask import Flask # type: ignore
from core.aluno.aluno_controller import aluno_controller

app = Flask(__name__)

app.register_blueprint(aluno_controller)

if __name__ == '__main__':
    app.run(debug=True)