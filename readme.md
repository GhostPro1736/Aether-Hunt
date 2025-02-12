# 🎮 TRPG (Terminal RPG)

# 🎮 Sobre o TRPG

TRPG é um RPG baseado em terminal que traz uma abordagem fresca para este formato clássico de jogo. Combinando elementos tradicionais de RPGs por turnos com um sistema único de aura e habilidades especiais, TRPG oferece uma experiência de jogo distinta.

Enquanto RPGs de terminal têm uma rica história, TRPG se destaca por:
- Um sistema de aura inovador com seis tipos únicos
- Mecânicas de batalha que equilibram estratégia e gerenciamento de recursos
- Uma interface que mescla a nostalgia dos jogos de texto com elementos modernos de RPG

Este projeto não apenas homenageia as raízes dos jogos de computador, mas também serve como um exercício de aprendizado em desenvolvimento de jogos e programação Python.

## 💡 Inspiração e Originalidade

Como muitos jogos contemporâneos, TRPG se inspira na rica tradição de RPGs e animes. No entanto, sua implementação como um jogo de terminal o torna único no cenário atual de jogos. Esta abordagem não apenas homenageia as raízes dos jogos de computador, mas também oferece uma nova perspectiva sobre como RPGs modernos podem ser apresentados.

O desenvolvimento do TRPG é um exercício de criatividade, combinando elementos familiares do gênero RPG com a originalidade de sua interface e mecânicas únicas. Todo o código foi desenvolvido do zero, com algumas contribuições da comunidade de IA, resultando em um projeto que é ao mesmo tempo nostálgico e inovador.

## 🤝 Contribuição e Aprendizado

Este projeto é um esforço de aprendizado e espero que possa servir de inspiração ou referência para outros desenvolvedores iniciantes. Se você encontrar algo útil neste código ou tiver sugestões para melhorias, fique à vontade para abrir uma issue ou entrar em contato. Juntos, podemos aprender e crescer como desenvolvedores!

## 🚀 Funcionalidades
- Sistema de aura com decisões dinâmicas
- Mecânica de reroll para customização
- Interface via terminal com arte ASCII

## 📁 Estrutura do Projeto
TRPG/
├── battle/ # Funcionalidades de batalha
├── commands/ # Comandos e funcionalidades principais
├── core/ # Dados e gerenciamento do usuário
├── inicialização/ # Configurações e inicialização
├── inputs/ # Validação de inputs durante todo game
└── tutorial/ # Onde todo inicio do tutorial estará disponível
## 🛠️ Tecnologias Utilizadas
- Python 3.13
- json(futuramente em desenvolvimento)

## 📦 Como Executar
1. Clone o repositório
2. Execute `python main.py`
## 📦 Requisitos

Para executar o TRPG, você precisará ter instalado:

- Python 3.11 ou superior
- Bibliotecas:
  - rich
  - pyfiglet
  - random (biblioteca padrão)
  - os (biblioteca padrão)
  - importlib (biblioteca padrão)

Você pode instalar as bibliotecas necessárias usando o comando pip: pip install colorama pyfiglet
## 🔮 Planos Futuros

Embora não haja um roadmap específico, algumas ideias para o futuro do TRPG incluem:

- Expandir o sistema de batalha
- Implementar um sistema de salvamento usando JSON
- Criar uma história mais elaborada para o jogo
- criar um site web para o jogo
- criar um aplicativo com bibliotecas como pydroid, pyxel e etc
- implementar javascript futuramente com o site web

## 📞 Contato

Sou um desenvolvedor em aprendizado e adoraria receber seu feedback ou responder suas perguntas sobre o TRPG!

- Discord: .ghost_pro
- Email: jv2093809@gmail.com
- GitHub: [@GhostPro1736](https://github.com/GhostPro1736)

Fique à vontade para entrar em contato por qualquer um desses meios!

## 📄 Licença

Este projeto é licenciado sob a licença MIT. Se você usar este código em seu próprio projeto, por favor, inclua uma referência ao projeto original e ao desenvolvedor:

"Baseado no projeto TRPG por [Seu Nome/GhostPro1736](https://github.com/GhostPro1736/Aether-Hunt)"

## Observaçôes

Alguns sistemas atualmente ainda estão em desenvolvimento como:
Sistema de batalha base
Inimigos
Npcs
Saves/loads
Inventário
Ataques

## 🔄 Versão Atual
v0.26 
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