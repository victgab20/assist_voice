from ollama import Client

client = Client(host='http://localhost:11434')  # Porta padrão do Ollama

def chamar_llama(mensagem_usuario: str) -> str:
    resposta = client.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": "Você é um assistente útil chamado Skywalker."},
            {"role": "user", "content": mensagem_usuario}
        ]
    )
    return resposta['message']['content'].strip()
