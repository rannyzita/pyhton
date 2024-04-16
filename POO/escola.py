#Abstração e Encapsulamento:
#Crie uma classe abstrata chamada Funcionario que contenha os atributos comuns a todos os funcionários 
#(nome e salário) e um método abstrato calcular_salario_anual().
#Encapsule os atributos da classe Funcionario para garantir que eles só possam ser acessados e #modificados por métodos da própria classe.

class Funcionario:
    def __init__(self, nome = '', salario = 0):
        self._nome = nome
        self._salario = salario
        
    def calcular_salario_anual(self):
        pass
        
    def set_nome(self, nome):
        self._nome = nome

    def set_salario(self, salario):
        self._salario = salario
    
    def get_nome(self):
        return self._nome
    
    def get_salario(self):
        return self._salario

#Herança:
#Crie duas subclasses de Funcionario: Professor e FuncionarioAdministrativo.
#A classe Professor deve ter um atributo adicional para armazenar a disciplina que leciona.
#A classe FuncionarioAdministrativo deve ter um atributo adicional para armazenar o cargo do funcionário.

#Polimorfismo:
#Implemente o método calcular_salario_anual() nas subclasses Professor e FuncionarioAdministrativo de forma que cada uma calcule o salário anual de acordo com regras específicas para cada tipo de funcionário.

class Professor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.disciplina = ''

    def calcular_salario_anual(self):
        valor_anual = self._salario*12
        return valor_anual
    
    def set_disciplina(self, disciplina):
        self.disciplina = disciplina

    def get_disciplina(self):
        return self.disciplina

class Funcionario_administrativo(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)
        self.cargo = ''

    def calcular_salario_anual(self):
        percentual = self._salario * 0.12
        salario_anual = (self._salario+percentual)*12
        return salario_anual 
       
    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo
    
Professor = Professor('Alexzin do mal', 4500)
Professor.set_disciplina('IED')

Funcionario_administrativo = Funcionario_administrativo('Ranny', 5000)
Funcionario_administrativo.set_cargo('Consultoria') 

salario_Professor = Professor.calcular_salario_anual()
Salario_Funcionario_administrativo = Funcionario_administrativo.calcular_salario_anual()

print(f'Professor: {Professor.get_nome()}')
print(f'Salário do Professor Anual: {salario_Professor}')
print(f'Disciplina: {Professor.get_disciplina()}')

print(f'\nFuncionário administrativo: {Funcionario_administrativo.get_nome()}')
print(f'Salário do Funcionário Administrativo: {Salario_Funcionario_administrativo}')
print(f'Cargo: {Funcionario_administrativo.get_cargo()}')
