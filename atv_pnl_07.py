from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

frases = [
    "quero comprar produto",
    "desejo fazer compra",
    "quero adquirir",
    "gostaria de comprar",
    "quero cancelar pedido",
    "cancelar minha compra",
    "desejo cancelar",
    "como cancelo meu pedido",
    "qual horário funcionamento",
    "vocês abrem sábado",
    "quero saber horário",
    "qual o horário de atendimento",
    "que horas vocês abrem",
    "quero saber que horas são",
    "horário de funcionamento"
]

intencoes = [
    "comprar",
    "comprar",
    "comprar",
    "comprar",
    "cancelar",
    "cancelar",
    "cancelar",
    "cancelar",
    "horario",
    "horario",
    "horario",
    "horario",
    "horario",
    "horario",
    "horario"
]

# TODO criar vetorizador
vetorizador = CountVectorizer()

# TODO transformar frases em vetores
X = vetorizador.fit_transform(frases)

# TODO treinar modelo Naive Bayes
modelo = MultinomialNB()
modelo.fit(X, intencoes)

# TODO pedir frase do usuário
entrada = input("Digite sua mensagem: ")

# TODO transformar entrada em vetor
entrada_vetor = vetorizador.transform([entrada])

# TODO prever intenção
predicao = modelo.predict(entrada_vetor)

print("Intenção detectada:", predicao[0])

#Resultado esperado:
# Digite sua mensagem: quero saber horário
# Intenção detectada: horario
