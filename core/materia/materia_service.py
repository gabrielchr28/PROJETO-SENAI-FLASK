from core.materia.materia_repository import MateriaRepository
from core.materia.materia import Materia

class MateriaService:
    def __init__(self):
        self.repository = MateriaRepository()

    def listar_materias(self):
        return self.repository.listar()
    
    def add_materia(self, materia):
        if isinstance(materia, Materia):
            return self.repository.adicionar(materia)
        else:
            return None
        
    def atualizar_materia(self, materia):
        if isinstance(materia, Materia):
            if materia.id > 0:
                return self.repository.atualizar(materia)
            else:
                return "ID obrigatório não informado"
        else:
            return None
        
    def remover_materia(self, id):
        sucesso = self.repository.remover(id)
        if not sucesso:
            return None
        else:
            return {
                "id": id,
                "removido": True
            }
        
    def obter_materia_id(self, id):
        materia = self.repository.obter_por_id(id)
        if not materia:
            return None
        else:
            return materia