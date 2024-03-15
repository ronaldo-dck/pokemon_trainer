from experta import *

class Clima(Fact):
    pass

class SistemaEspecialista(KnowledgeEngine):
    @Rule(Clima(clima='ensolarado'))
    def ensolarado(self):
        print("Vá fazer uma caminhada no parque.")

    @Rule(Clima(clima='chuvoso'))
    def chuvoso(self):
        print("Assista a um filme em casa.")

    @Rule(Clima(clima='nublado'))
    def nublado(self):
        print("Leia um livro enquanto relaxa.")

    @Rule(Clima(clima='neve'))
    def neve(self):
        print("Aproveite para fazer um boneco de neve.")

# Exemplo de uso do sistema especialista
engine = SistemaEspecialista()
engine.reset()
engine.declare(Clima(clima='ensolarado'))
engine.run()
