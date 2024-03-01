import nltk
from nltk.chat.util import Chat, reflections

respostas_ordenadas = [
    [
        r"Oi|Olá|Hey",
        [
            "Olá",
            "Oi",
            "Hello"
        ]
    ],
    [
        r"Qual é o seu nome?",
        [
            "Meu nome é Tony Stark",
            "Eu sou o Homem de Ferro"
        ]
    ],
    [
        r"Como você está?|como voce esta?|como voce ta?|como vc ta?",
        [
            "Estou bem, obrigado! E você?",
            "Estou ótimo! E você?",
            "To bem",
            "Mais ou menos"
        ]
    ],
    [
        r"Adeus|tchau",
        [
            "Tchau!", "Até mais!",
            "Até a próxima!"
        ]
    ]
    
]

def chatbot():
    print("Olá, sou o Homem de Ferro, como posso te ajudar hoje?")
    chat = Chat(respostas_ordenadas, reflections)
    while True:
        try:
            resposta = chat.respond(input("Digite: "))
            
            if resposta == None:
                print("Desculpe, pode repetir?")
            else:
                print(resposta)
        except KeyboardInterrupt:
            break
        
chatbot()
