from flask import Blueprint, request, jsonify # type: ignore
from core.materia.materia import Materia
from core.materia.materia_service import MateriaService
from core.autenticacao.autenticacao import autenticacao

materia_service = MateriaService()

materia_controller = Blueprint('materia', __name__, url_prefix='/materias')

@materia_controller.route('/', methods=['GET'])
@autenticacao
def listar():
    return materia_service.listar_materias()

@materia_controller.route('/', methods=['POST'])
@autenticacao
def add_materia():
    dados = request.get_json()
    obj_materia = Materia(nome=dados['nome'], id=0, sigla=dados['sigla'], descricao=dados['descricao'])
    materia = materia_service.add_materia(obj_materia)
    return jsonify(materia)

@materia_controller.route('/<int:id>', methods=['GET'])
@autenticacao
def obter_por_id(id):
    materia = materia_service.obter_materia_id(id)
    if materia:
        return jsonify(materia)
    else:
        return jsonify({'erro': '404 not found'}), 404
    
@materia_controller.route('/<int:id>', methods=['DELETE'])
@autenticacao
def remover_materia(id):
    sucesso = materia_service.remover_materia(id)
    return jsonify(sucesso)

@materia_controller.route('/', methods=['PUT'])
@autenticacao
def atualizar_materia():
    dados = request.get_json()
    obj_materia = Materia(nome=dados['nome'], id=dados['id'], sigla=dados['sigla'], descricao=dados['descricao'])
    materia = materia_service.atualizar_materia(obj_materia)
    return jsonify(materia)