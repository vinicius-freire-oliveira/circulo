# Importa o módulo circulo
import circulo 

# Acesso ao valor de Pi e funções do módulo circulo
# Comentado para evitar erro ao tentar acessar membros de um módulo não importado diretamente
#print(circulo.Pi)
#print(circulo.area(5))
#print(circulo.comprimento_circunferencia(5))

# Importa apenas a função 'area' do módulo circulo
from circulo import area

# Como o módulo circulo não foi importado diretamente, o acesso ao valor de Pi não é possível
# Para acessar o valor de Pi, o módulo deve ser importado diretamente ou o valor de Pi deve ser exportado
# como um membro da função 'area' ou de outro membro do módulo

# Como a função 'area' foi importada, pode ser acessada diretamente
print(circulo.Pi)  # Erro, Pi não está definido
print(circulo.area(5))  # Erro, circulo não está definido, use 'area(5)' diretamente
