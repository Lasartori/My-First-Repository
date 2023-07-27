class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registrahoras(self,horas):
        print("Horas Registradas...")

    def mostrar_tarefas(self):
        print("Fez muita coisa...")

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, Caelumer!!")

    def busca_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos  - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print("Fez muita coisa, Alurete!!")

    def busca_pergunta_sem_resposta(self):
        print("Mostrando perguntas não respondidas do Fórum")

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

luan = Senior('Luan')
print(luan)