# 🎮 Aether Hunt

# 🎮 Sobre o Jogo

Este Jogo é um tipo de RPG baseado em gráficos de terminal que traz uma abordagem fresca para este formato clássico de jogo. Combinando elementos tradicionais de RPGs por turnos com um sistema único de aura e habilidades especiais, este TRPG oferece uma experiência de jogo distinta.

O Aether Hunt tem diversos destaques, misturando diversos conceitos como:
- Um sistema de aura inovador com seis tipos únicos
- Mecânicas de batalha que equilibram estratégia e gerenciamento de recursos
- Uma interface que mescla a nostalgia dos jogos de texto com elementos modernos de RPG

Este projeto não apenas homenageia as raízes dos jogos de computador, mas também serve como um exercício de aprendizado em desenvolvimento de jogos e programação Python.

## 💡 Inspiração e Originalidade

Como muitos jogos contemporâneos, O Aether Hunt se inspira na rica tradição de RPGs e animes. No entanto, sua implementação como um jogo de terminal o torna único no cenário atual de jogos. Esta abordagem não apenas homenageia as raízes dos jogos de computador, mas também oferece uma nova perspectiva sobre como RPGs modernos podem ser apresentados.

O desenvolvimento do TRPG é um exercício de criatividade, combinando elementos familiares do gênero RPG com a originalidade de sua interface e mecânicas únicas. Todo o código foi desenvolvido do zero, com algumas contribuições da comunidade de IA para aprendizado, resultando em um projeto que é ao mesmo tempo nostálgico e inovador.

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
- Python 3.11 ou superior
- json(futuramente em desenvolvimento)

## 📦 Como Executar
1. Clone o repositório
2. Execute `python main.py`
## 📦 Requisitos

Para executar o Aether Hunt, você precisará ter instalado:

- Python 3.11 ou superior
- Bibliotecas:
  - rich
  - pyfiglet
  - random (biblioteca padrão)
  - os (biblioteca padrão)
  - importlib (biblioteca padrão)

Você pode instalar as bibliotecas necessárias usando o comando pip: pip install rich pyfiglet
## 🔮 Planos Futuros

Embora não haja um roadmap específico, algumas ideias para o futuro do TRPG incluem:

- Expandir o sistema de batalha
- Implementar um sistema de salvamento usando JSON
- Criar uma história mais elaborada para o jogo
- criar um site web para o jogo
- aplicar pygamelib para gráficos melhorados, mantendo a essência do jogo
- implementar javascript futuramente com o site web

## 📞 Contato

Sou um desenvolvedor em aprendizado e adoraria receber seu feedback ou responder suas perguntas sobre o Aether Hunt!

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
Sistema gráfico

## 🔄 Versão Atual
v0.26.1
CRIADA EM 12/02/2025 as 19:16
consertado bugs em classe attacks e effects.
agora o atributo é criado dentro do proprio ataque, fazendo com que o efeito principal não seja modificado com o ataque, agora o ataque tem um atributo proprio para cada efeito.
criado a função get_attribute que retorna o valor de todos os atributos quando não é digitado um atributo específico.
caso seja adicionado um atributo específico, ele retorna o atributo específicado.
os efeitos de um ataque agora criam um dicionario, pegando o nome do efeito(colocado no nome do efeito) com getattr e adicionando o efeito especificamente como o valor da chave.
melhorado tratamento de erros em attacks.
criado um arquivo debug.py que é iniciado com todo o necessário, pulando a seleção de nome(GhostPro como base), aura e habilidade com comandos de debug na seleção de habilidades.
criado arquivo effects.py que ficará armazenado todos os efeitos.
