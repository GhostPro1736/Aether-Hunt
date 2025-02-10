# versão 0.1:
criação de pastas batalha, info, inicio e main.py
codigo base criado
# versão 0.2:
CRIADA EM 02/02/2025 AS 18:45
criação do readme.md e version.md
modificado pasta info para personagem e batalha para commands por enquanto
adicionado arte ascii para inicio
alterado inicio para commands
alterado decisão de aura, reroll para arquivo iniciar
criado comando para colocar um nome
variável iniciou criada dentro do info, fazendo identificar se o usuario iniciou ou não sua jornada
main.py extremamente reduzido
modificado seleção de aura de lista para tuplas em iniciar, types_aura
pesos alteradosnas seguintes ordens, (Bastion, Flux, Morphic, Forge, Puppet, Perspicaz)
peso anterior: (27,24,19,15,15,0.033), peso atual: (27,24,19,15,15,0.1)
adicionado uma mensagem especial quando o usuário consegue a aura perspicaz
## versão 0.21:
CRIADA EM 03/02/2025 AS 13:47
reorganizada a estrututa de pastas
adicionado classes, programação orientada
criado a classe gamestate e User
levado o título para ascii_arts
modificado o código iniciar, simplificando ele e adicionando classes
personagem 100% modificado, adicionado classes
## versão 0.22
CRIADA EM 04/02/2025 AS 00:36
criada a pasta inicialização
arquivo iniciar para pasta inicialização
dividido o arquivo iniciar em 4 arquivos py para maior controle
aura_decision, iniciar, name_selector e titulo
criado a classe roll para guardar tentativas restantes e facilitar código futuramente
### versão 0.22.1
CRIADA EM 04/02/2025 AS 00:51
modificado nome de pastas e arquivos
apagado o arquivo titulo
### versão 0.22.2:
CRIADA EM 05/02/2025 AS 14:07
refatorado partes do código
agora a mudança de funções é feita pelo main
criado pasta tutorial
adicionado __init__.py para pastas core e inicialização para facil acesso de funções dentro do main
## versão 0.23:
CRIADA EM 05/02/2025 AS 23:58
criado habilidades únicas com suas descrições para batalha
criado seleção de habilidades especiais
criado arquivo Ability em battle
seleção de habilidades no inicio
criado novos atributos para user e classe enemy
### versão 0.23.1:
CRIADA EM 06/02/2025 AS 22:13
criado novas classes em player, como character e etc
agora criado o arquivo battle
### versão 0.23.2:
CRIADA EM 08/02/2025 AS 1:40
criado nova classe ability
refeito todo código em Ability.py, mudando defs(agora show_ability, choose_ability), utilizando for loop e adicionando mensagem de erro caso valor de habilidade seja incorreto
## versão 0.24:
CRIADA EM 08/02/2025 AS 16:10
criado valid input
agora inputs são validados lá, comandos adicionados a pasta command é automaticamente aceito pelo valid
requisitos: nome do comando = nome do arquivo.py
### versão 0.24.1:
CRIADA EM 09/02/2025 as 01:59
criado comando addexp e criado aumento de level com xp, formula para aumento de quantidade de xp gradual por nível
quanto maior o nível, maior o custo de xp
addexp é o primeiro comando de debug
## versão 0.25:
CRIADA EM 09/02/2025 as 17:13
alterado ascii de iniciar: agora feito com pyfiglet
agora ascii inicial tem cor: utilizado módulo colorama
novos comandos: status, adminstats para poder ter acesso ao poder de admin
ability agora é controlado por user também
### versão 0.25.1:
CRIADA EM 09/02/2025 as 17:58
agora foi criada a função random_color dentro do arquivo random_letter_color
ela permite fazer com que uma mensagem fique colorida, somente retornando a mensagem que deseja como parâmetro da função
### versão 0.25.2:
CRIADA EM 09/02/2025 as 23:26
modificação de bibliotecas, de colorama para rich
modificação geral(onde havia partes da biblioteca colorama, agora é feito pelo rich)
criado um painel(um frame) para o ascii art de título