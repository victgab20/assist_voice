# Assistente de Voz com LLaMA 3.1

Este projeto implementa um assistente de voz interativo utilizando Streamlit como interface, Whisper para transcrição de áudio, LLaMA 3.1 para processamento de linguagem natural e pyttsx3 para síntese de voz. O assistente permite gravar áudio, transcrevê-lo, enviar a transcrição para o modelo LLaMA e reproduzir a resposta em áudio.

## Estrutura do Projeto

```
.
├── .venv/                     # Ambiente virtual Python
├── modules/                   # Módulos personalizados
│   ├── __pycache__/          # Cache de compilação Python
│   ├── audio_utils.py        # Utilitários de áudio (vazio no momento)
│   ├── llama_interface.py    # Interface com o modelo LLaMA
│   ├── tts.py               # Funções de síntese de voz (text-to-speech)
│   ├── whisper_stt.py       # Funções de transcrição de áudio (speech-to-text)
├── .gitignore                # Arquivo de configuração do Git
├── app.py                   # Script principal do Streamlit
├── requirements.txt         # Dependências do projeto
```

## Pré-requisitos

- Python 3.8 ou superior
- Ambiente virtual (recomendado)
- Servidor Ollama rodando localmente na porta padrão (11434)
- Placa GPU compatível com CUDA (opcional, para acelerar Whisper)

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure o Ollama**:
   - Certifique-se de que o servidor Ollama está rodando localmente:
     ```bash
     ollama run llama3
     ```

## Uso

1. **Execute o aplicativo**:
   ```bash
   streamlit run app.py
   ```

2. **Interaja com o assistente**:
   - Acesse a interface no navegador (geralmente em `http://localhost:8501`).
   - Clique no botão "Gravar e Perguntar" para gravar sua pergunta.
   - O áudio será gravado por 5 segundos, transcrito, processado pelo LLaMA 3.1, e a resposta será exibida e reproduzida em áudio.

## Funcionalidades

- **Gravação de áudio**: Grava áudio de 5 segundos usando `sounddevice`.
- **Transcrição**: Utiliza o modelo Whisper (`base`) para transcrever áudio em português.
- **Processamento de linguagem**: Envia a transcrição ao modelo LLaMA 3.1 via Ollama.
- **Síntese de voz**: Reproduz a resposta usando `pyttsx3`.

## Dependências

As dependências estão listadas em `requirements.txt`. Principais bibliotecas:
- `streamlit`: Interface web interativa
- `whisper`: Transcrição de áudio
- `ollama`: Interface com o modelo LLaMA
- `pyttsx3`: Síntese de voz
- `sounddevice`, `numpy`, `scipy`: Manipulação de áudio
- `torch`: Backend para Whisper (suporte a CUDA, se disponível)

## Notas

- O modelo Whisper é configurado para transcrição em português (`language="pt"`).
- A transcrição e o processamento podem ser acelerados se uma GPU compatível com CUDA estiver disponível.
- O arquivo `audio_utils.py` está vazio e pode ser usado para adicionar funcionalidades futuras.

