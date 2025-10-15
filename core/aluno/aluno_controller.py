from flask import Blueprint, request, jsonify # type: ignore
from core.aluno.aluno_service import AlunoService
from core.aluno.aluno import Aluno

aluno_service = AlunoService()

aluno_controller = Blueprint('aluno', __name__, url_prefix='/alunos')

@aluno_controller.route('/', methods=['GET'])
def listar_alunos():
    alunos = aluno_service.listar_alunos()
    return jsonify(alunos)

@aluno_controller.route('/', methods=['POST'])
def add_aluno():
    dados = request.get_json()
    obj_aluno = Aluno(id=0, nome=dados["nome"])
    aluno_service.add_aluno(obj_aluno)