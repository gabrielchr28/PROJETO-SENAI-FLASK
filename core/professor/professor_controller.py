from flask import Blueprint, request, jsonify # type: ignore
from core.professor.professor import Professor
from core.professor.professor_service import ProfessorService

professor_service = ProfessorService()
professor_controller = Blueprint('professor', __name__, url_prefix='/professores')

@professor_controller.route('/', methods=['GET'])
def listar():
    return professor_service.listar_professores()

@professor_controller.route('/', methods=['POST'])
def add_prof():
    dados = request.get_json()
    obj_professor = Professor(nome=dados['nome'], id=0, formacao=dados['formacao'], idade=dados['idade'])
    professor = professor_service.add_professor(obj_professor)
    return jsonify(professor)

@professor_controller.route('/', methods=['PUT'])
def atualizar_prof():
    dados = request.get_json()
    obj_pro = Professor(nome=dados['nome'], id=dados['id'], formacao=dados['formacao'], idade=dados['idade'])
    professor = professor_service.atualizar_professor(obj_pro)
    if professor:
        return jsonify(professor)
    else:
        return jsonify({"erro": "404 not found"}), 404
    
@professor_controller.route('/<int:id>', methods=['DELETE'])
def remover_prof(id):
    sucesso = professor_service.remover_professor(id)
    return sucesso

@professor_controller.route('/<int:id>', methods=['GET'])
def obter_prof_id(id):
    prof = professor_service.obter_prof_id(id)
    if prof:
        return jsonify(prof)
    else:
        return jsonify({"erro": "404 not found"}), 404