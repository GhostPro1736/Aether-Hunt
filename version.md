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
#### versão 0.25.21:
CRIADA EM 10/02/2025 as 15:35
adicionado mais cores aos textos
#### versão 0.25.22:
CRIADA EM 11/02/2025 as 00:28
adicionado mais cores aos textos deo ability choice(arquivo ability)
agora é renderizado as 3 opções ao mesmo tempo
é criado um layout com um painel totalmente personalizado
## versão 0.26 
CRIADA EM 11/02/2025 as 21:49
adicionado criação de ataques e efeitos via classe
ataques tem seus próprios nomes, efeitos, durações, danos, defesa e etc.
efeitos tem seus próprios tipos, buff, debuff, em quem será aplicado o efeito, nomes e etc
efeitos tem função atribute para adicionar personalização no ataque, como duração do efeito e dano ou buff concedido
ataques podem ter multiplos efeitos
para criar um efeito é só criar uma variavel com o nome do efeito desejado com Effect(parametros)
parametros em Effect(name=Obrigatório, effect_type=Obrigatório, buff_type=Opcional, stackable=Opcional, target=Obrigatório, priority=Opcional, max_duration=Opcional)
para adicionar atributos específicos ao efeito é só usar, variavel_de_ataque.effect[indice, em qual posição ele está].atributes(parametros)
parametros em Effect.atributes(duration=Obrigatório, value=Opcional, caso tenha efeitos de buff/debuff, damage=Opcional, caso tenha efeitos de dano, trigger_condition=Opcional)
para criar ataques é só criar uma variavel com Attacks(parametros)
parametros em Attacks(isDef=Opcional, damage=Opcional, type=Opcional, defense=Opcional, hasEffect=Opcional, name=Obrigatório, counter=Opcional, counter_attack=Opcional, counts=Opcional, effects=Obrigatório(caso usado hasEffect=True), min_level=Opcional)
### versão 0.26.1
CRIADA EM 12/02/2025 as 19:16
consertado bugs em classe attacks e effects
agora o atributo é criado dentro do proprio ataque, fazendo com que o efeito principal não seja modificado com o ataque, mas agora o ataque tem um atributo proprio para cada efeito
criado a função get_attribute que retorna o valor de todos os atributos quando não é digitado um atributo específico e retorna o atributo específico caso seja especificado
os efeitos do ataque agora criam um dicionario pegando o nome do efeito(colocado no nome do efeito) com getattr e adicionando o efeito especificamente como o valor da chave
melhorado tratamento de erros em attacks
criado um arquivo debug.py que é iniciado com todo o inicio necessário, pulando sõ de nome, aura e habilidade com comandos de debug na seleção de habilidades
criado arquivo effects.py que ficará armazenado todos os efeitos
#### v0.26.11
CRIADA EM 25/02/2025 as 22:06
modificado área de seleção de habilidades
* bugs conhecidos:
área de seleção de habilidades está utilizando memória excessiva, área de seleção de habilidades está utilizando time.sleep para atualizar o painel, o que acaba ocasionando bugs de delay, caso não seja utilizado time acaba nãoi atualizando corretamente o painel
* mudanças futuras:
irei retirar todo resquicio da biblioteca rich do front-end e retirar a biblioteca keyboard, irei alterar a licença de mit para GPLv3 para adicionar pygamelib, com ele a parte gráfica irá melhorar drasticamente além de diminuir dependencias, além de ter um sistema de captura de teclas mais robusto, melhorando a área da seleção de habilidades