from core.usuario.usuario_repository import UsuarioRepository
from core.usuario.usuario import Usuario

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def listar(self):
        return self.repository.listar()
    
    def add_usuario(self, obj_usu):
        if isinstance(obj_usu, Usuario):
            return self.repository.adicionar(obj_usu)
        else:
            return None
    
    def atualizar_usuario(self, obj_usu):
        if isinstance(obj_usu, Usuario):
            if obj_usu.id > 0:
                return self.repository.atualizar(obj_usu)
            else:
                return "ID obrigatório não informado"
        else:
            return None
        
    def remover_usuario(self, id):
        sucesso = self.repository.remover(id)
        if not sucesso:
            return None
        else:
            return {
                "id": id,
                "removido": True
            }
        
    def obter_usuario_id(self, id):
        aluno = self.repository.obter_por_id(id)
        if not aluno:
            return None
        else:
            return aluno
        
    def obter_usuario_por_usuario_senha(self, usu, senha):
        return self.repository.buscar_usuario_por_usuario_senha(usu, senha)