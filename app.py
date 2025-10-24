from flask import Flask # type: ignore
from core.aluno.aluno_controller import aluno_controller
from core.usuario.usuario_controller import usuario_controller
from core.professor.professor_controller import professor_controller
from core.materia.materia_controller import materia_controller

app = Flask(__name__)

app.register_blueprint(aluno_controller)
app.register_blueprint(usuario_controller)
app.register_blueprint(professor_controller)
app.register_blueprint(materia_controller)

@app.route('/bem-vindo')
def main():
    return """
<h1>Seja muito bem vindo a essa API escolar</h1>
<h2>Gabriel Gonçalves Christófano</h2>
"""

if __name__ == '__main__':
    app.run(debug=True)