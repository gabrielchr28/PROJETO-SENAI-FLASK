from flask import Blueprint, jsonify, request # type: ignore
from core.usuario.usuario_service import UsuarioService
from core.usuario.usuario import Usuario

usuario_service = UsuarioService()

usuario_controller = Blueprint('usuario', __name__, url_prefix="/usuarios")

@usuario_controller.route('/', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_service.listar()
    return jsonify(usuarios)

@usuario_controller.route('/', methods=['POST'])
def add_usuario():
    dados = request.get_json()
    obj_usuario = Usuario(dados['usuario'], dados['senha'], dados['ativo'], id=0)
    usuario = usuario_service.add_usuario(obj_usuario)
    return jsonify(usuario), 201

@usuario_controller.route('/<int:id>', methods=['GET'])
def obter_usu_por_id(id):
    usuario = usuario_service.obter_usuario_id(id)
    if usuario:
        return jsonify(usuario)
    else:
        return jsonify({'erro': '404 not found'}), 404
    
@usuario_controller.route('/<int:id>', methods=['DELETE'])
def remover_usuario(id):
    sucesso = usuario_service.remover_usuario(id)
    return jsonify(sucesso)

@usuario_controller.route('/', methods=['PUT'])
def atualizar_usuario():
    dados = request.get_json()
    obj_usuario = Usuario(dados['usuario'], dados['senha'], dados['ativo'], id=dados['id'])
    usuario = usuario_service.atualizar_usuario(obj_usuario)
    return jsonify(usuario)