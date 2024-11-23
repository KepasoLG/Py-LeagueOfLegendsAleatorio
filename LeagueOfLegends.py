import random

# Dicionários com todas as opções de campeões, runas, itens e feitiços

# Lista completa de campeões por papel (Atualizada até a versão mais recente de LoL)
campeoes = {
    "atirador": [
        "Jinx", "Kai'Sa", "Miss Fortune", "Ezreal", "Aphelios", "Ashe", "Caitlyn", "Sivir", "Tristana", "Xayah",
        "Jhin", "Vayne", "Samira", "Draven", "Lucian", "Zeri"
    ],
    "mago": [
        "Ahri", "Zoe", "Orianna", "Lux", "Syndra", "Annie", "Viktor", "Karthus", "Vel'Koz", "Brand",
        "Kassadin", "Ryze", "Taliyah", "Swain", "Morgana", "Twisted Fate", "Seraphine"
    ],
    "tanque": [
        "Malphite", "Shen", "Ornn", "Sion", "Leona", "Amumu", "Alistar", "Tahm Kench", "Zac", "Singed",
        "Sejuani", "Rammus", "Braum", "Dr. Mundo", "Cho'Gath", "Illaoi", "Gragas"
    ],
    "lutador": [
        "Camille", "Kennen", "Renekton", "Jax", "Darius", "Fiora", "Riven", "Sett", "Gangplank", "Volibear",
        "Aatrox", "Olaf", "Kled", "Jayce", "Lee Sin"
    ],
    "assassino": [
        "Zed", "Katarina", "Akali", "Talon", "LeBlanc", "Evelynn", "Kha'Zix", "Rengar", "Shaco", "Pyke",
        "Fizz", "Nocturne", "Qiyana"
    ],
    "suporte": [
        "Thresh", "Lulu", "Nami", "Janna", "Seraphine", "Yuumi", "Bard", "Leona", "Alistar", "Morgana",
        "Karma", "Rakan", "Xerath", "Nautilus", "Amumu", "Senna"
    ]
}

# Lista completa de runas (comum para diferentes campeões)
runas = {
    "atirador": [
        "Conquistador", "Leve um de cada", "Pressione o Ataque", "Árvore do Inferno", "Agressor", "Chave da Trindade"
    ],
    "mago": [
        "Cometa Arcano", "Aery", "Feitiçaria", "Gênio Eterno", "Feitiçaria", "Explosão Eterna"
    ],
    "tanque": [
        "Demolir", "Inabalável", "Aprendizado Tático", "Combate Final", "Destruidor", "Resiliência"
    ],
    "lutador": [
        "Conquistador", "Agressor", "Guerreiro", "Destruidor", "Coração de Aço", "Fortaleza Eterna"
    ],
    "assassino": [
        "Conquistador", "Domínio", "Agressor", "Destruidor", "Frenesi"
    ],
    "suporte": [
        "Feitiçaria", "Aery", "Fonte da Vida", "Magia Escudo", "Feitiço de Recuperação", "Fonte da Vitalidade"
    ]
}

# Lista completa de itens para cada tipo de campeão (o básico e a filosofia do jogo)
itens = {
    "atirador": [
        "Essência Longínqua", "Gume do Infinito", "Dançarina Fantasma", "Canhão Fumegante", "Botas de Velocidade",
        "Lâmina da Morte", "Arco-Íris de Runas"
    ],
    "mago": [
        "Ampulheta de Zhonya", "Cajado do Vazio", "Capítulo Perdido", "Morellonomicon", "Rylai",
        "Cajado do Sol", "Tormento de Liandry"
    ],
    "tanque": [
        "Coração Congelado", "Armamento de Warmog", "Aegis da Legião", "Jaula de Ferro", "Cloak das Espinas"
    ],
    "lutador": [
        "Guerreiro de Rime", "Coração de Aço", "Sterak", "Fúria de Titã", "Dança da Morte"
    ],
    "assassino": [
        "Draktharr", "Dança da Morte", "Mercurial", "Lâmina Fantasma", "Golpe Fatal"
    ],
    "suporte": [
        "Redenção", "Armadura de Espinhos", "Solari", "Cadinho de Luden", "Medalhão de Ferro"
    ]
}

# Lista de feitiços
feitiços = [
    "Flash", "Curar", "Golpear", "Teleportar", "Barreira", "Ignite", "Exaustão", "Reviver"
]

# Função para selecionar campeões e outras opções com base no papel
def escolher_campeao(papel):
    campeao = random.choice(campeoes[papel])
    runa = random.choice(runas[papel])
    item = random.choice(itens[papel])
    feitiço = random.sample(feitiços, 2)  # Seleciona 2 feitiços aleatórios

    return campeao, runa, item, feitiço

# Função principal
def main():
    print("Bem-vindo ao simulador de campeões e build do League of Legends!")
    
    papel = input("Qual papel você quer jogar? (atirador, mago, tanque, lutador, assassino, suporte): ").lower()
    
    if papel in campeoes:
        campeao, runa, item, feitiço = escolher_campeao(papel)
        
        print(f"\nSua sugestão de jogo:")
        print(f"Campeão: {campeao}")
        print(f"Runas: {runa}")
        print(f"Item inicial: {item}")
        print(f"Feitiços: {feitiço[0]} e {feitiço[1]}")
    else:
        print("Papel inválido! Por favor, escolha um dos seguintes: atirador, mago, tanque, lutador, assassino, suporte.")

if __name__ == "__main__":
    main()
