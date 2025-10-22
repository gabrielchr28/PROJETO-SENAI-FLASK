from core.professor.professor_repository import ProfessorRepository
from core.professor.professor import Professor

class ProfessorService:
    def __init__(self):
        self.repository = ProfessorRepository()

    def listar_professores(self):
        return self.repository.listar()
    
    def add_professor(self, obj_pro):
        if isinstance(obj_pro, Professor):
            return self.repository.adicionar(obj_pro)
        else:
            return None
        
    def atualizar_professor(self, professor):
        if isinstance(professor, Professor):
            if professor.id > 0:
                return self.repository.atualizar(professor)
            else:
                return "ID obrigatório não informado"
        else:
            return None
        
    def remover_professor(self, id):
        sucesso = self.repository.remover(id)
        if not sucesso:
            return None
        else:
            return {
                "id": id,
                "removido": True
            }
        
    def obter_prof_id(self, id):
        professor = self.repository.obter_por_id(id)
        if not professor:
            return None
        else:
            return professor