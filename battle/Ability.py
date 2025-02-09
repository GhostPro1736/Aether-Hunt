from core import user
Abilities = {
"Bastion": {"Escudo Espectral": {"Custo": "100% aura", "Efeito": "Bloqueia o próximo ataque e devolve 150% do dano.", "Descrição": "A melhor defesa é um contra-ataque esmagador!"}, "Égide de Retribuição": {"Custo": "80% aura", "Efeito": "Ignora dano por 1 turno e próximo ataque causa 200% de dano.", "Descrição": "Aproveite a invulnerabilidade para preparar o golpe decisivo."}, "Fúria da Carapaça": {"Custo": "30% HP", "Efeito": "ATK dobrado e DEF zerada por 3 turnos.", "Descrição": "Troque proteção por poder bruto!"}}, 
"Flux": {"Raio de Plasma": {"Custo": "100% aura", "Efeito": "Ataque único de 300% ATK que ignora 50% da DEF.", "Descrição": "Um único disparo para terminar o combate."}, "Vórtice de Sobrecarga": {"Custo": "70% aura + 10% HP", "Efeito": "Causa 200% dano e paralisa inimigo por 1 turno.", "Descrição": "Congele o oponente para dominar o ritmo."}, "Modo Overdrive": {"Custo": "40% aura/turno", "Efeito": "+50% velocidade e +25% dano enquanto ativo.", "Descrição": "Acelere gradualmente para sobrepujar o inimigo."}},
"Morphic": {"Garras de Quimera": {"Custo": "100% aura", "Efeito": "ATK 250% por 4 turnos. Não pode defender.", "Descrição": "Agressão total sem espaço para defesa."}, "Exoesqueleto Adaptativo": {"Custo": "60% aura", "Efeito": "30% do dano recebido vira cura (2x abaixo de 50% HP).", "Descrição": "Transforme sofrimento em resiliência."}, "Metabolismo de Emergência": {"Custo": "20% HP", "Efeito": "Recupera 50% da aura. Usos: 1x/combate.", "Descrição": "Sacrifício vital por uma segunda chance."}}, 
"Forge": {"Lâmina de Quark": {"Custo": "100% aura", "Efeito": "Arma com 2x ATK que ignora armaduras. Quebra ao errar.", "Descrição": "Precisão letal com risco calculado."}, "Barreira de Energia": {"Custo": "90% aura", "Efeito": "Escudo que bloqueia 3 ataques ou dura 3 turnos.", "Descrição": "Proteção versátil para estratégias prolongadas."}, "Canhão de Reciclagem": {"Custo": "1 item", "Efeito": "250% dano + efeito do item consumido.", "Descrição": "Use seu inventário como arma!"}}, 
"Puppet": {"Marionete de Dor": {"Custo": "100% aura", "Efeito": "Inimigo se ataca com 120% ATK por 1 turno.", "Descrição": "Faça o oponente virar contra si mesmo."}, "Fantoche de Retaliação": {"Custo": "50% aura", "Efeito": "Clone que absorve 1 ataque e explode com 100% dano recebido.", "Descrição": "Proteja-se e revide simultaneamente."}, "Paralisia Sináptica": {"Custo": "30% HP", "Efeito": "Inimigo perde 1 turno.", "Descrição": "Comande o fluxo da batalha com custo vital."}}, 
"Perspicaz": {"Mira da Morte": {"Custo": "100% aura", "Efeito": "Próximo ataque é crítico e ignora defesas.", "Descrição": "Um único tiro, uma única morte."}, "Foco de Batalha": {"Custo": "80% aura", "Efeito": "Dobra precisão e +40% dano crítico por 3 turnos.", "Descrição": "Ameaça crescente com foco tático."}, "Estratégia Suprema": {"Custo": "100% aura + 15% HP", "Efeito": "100% acerto e +25% dano por 2 turnos.", "Descrição": "Domine o campo com recursos totais."}}}
def show_abilities():
    print(f"Suas habilidades disponíveis para {user.aura} são:")
    for x, (Ability, description) in enumerate(Abilities[user.aura].items()):
        print(f"\nHabilidade {x+1}: {Ability} \nCusto: {description['Custo']} \nEfeito: {description['Efeito']} \nDescrição: {description['Descrição']}", end="\n")
def choose_ability():
    show_abilities()
    while True:
        try:
            choice = int(input("Coloque o valor da habilidade desejada: "))
            abilities = list(Abilities[user.aura].items())
            if choice in range(1, len(abilities)+1):
                chosen_ability, description = abilities[choice - 1]
                user.ability.cost, user.ability.effect, user.ability.name, user.ability.description = (description['Custo'], description["Efeito"], chosen_ability, description["Descrição"])
                description = f"\nCusto: {user.ability.cost} \nEfeito: {user.ability.effect} \nDescrição: {user.ability.description}"
                return print(f"\nÓtima escolha, agora sua habilidade permanente é: {chosen_ability}")
            else:
                print("\nPor favor coloque o número de sua habilidade desejada:\n", end="\n")
                show_abilities()
        except ValueError:
            print("Valor inválido, por favor digite somente números")
