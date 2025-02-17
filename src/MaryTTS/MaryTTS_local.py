import PyPDF2
import requests


def extrair_texto_pdf(caminho_pdf):
    """
    Lê todas as páginas de um arquivo PDF e retorna o texto extraído.
    """
    texto = ""
    try:
        with open(caminho_pdf, 'rb') as arquivo:
            leitor = PyPDF2.PdfReader(arquivo)
            for pagina in leitor.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto += texto_pagina + "\n"
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
    return texto


def texto_para_audio_marytts(texto, caminho_audio_saida):
    """
    Envia o texto para o servidor MaryTTS e salva o áudio retornado em um arquivo.
    Certifique-se de que o servidor MaryTTS esteja rodando em http://localhost:59125.
    """
    url = "http://localhost:59125/process"
    parametros = {
        "INPUT_TYPE": "TEXT",
        "OUTPUT_TYPE": "AUDIO",
        "LOCALE": "pt_BR",
        "AUDIO": "WAVE",  # Formato de áudio desejado (WAVE, MP3, etc.)
        # Caso você possua uma voz específica instalada, pode especificá-la, por exemplo:
        # "VOICE": "nome_da_voz"
        "INPUT_TEXT": texto
    }

    try:
        resposta = requests.get(url, params=parametros)
        if resposta.status_code == 200:
            with open(caminho_audio_saida, "wb") as arquivo_audio:
                arquivo_audio.write(resposta.content)
            print(f"Áudio salvo com sucesso em: {caminho_audio_saida}")
        else:
            print(f"Erro na conversão. Código de status: {resposta.status_code}")
    except Exception as e:
        print(f"Erro na requisição para o MaryTTS: {e}")


def main():
    caminho_pdf = "entrada.pdf"  # Substitua pelo caminho do seu arquivo PDF
    caminho_audio_saida = "saida.wav"  # Nome do arquivo de áudio de saída

    print("Extraindo texto do PDF...")
    texto_extraido = extrair_texto_pdf(caminho_pdf)

    if texto_extraido.strip():
        print("Convertendo texto para áudio com MaryTTS...")
        texto_para_audio_marytts(texto_extraido, caminho_audio_saida)
    else:
        print("Nenhum texto foi extraído do PDF.")


if __name__ == "__main__":
    main()
