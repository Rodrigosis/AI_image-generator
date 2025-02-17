# Utiliza uma imagem leve com Java
FROM openjdk:8-jre-alpine

# Instala utilitários necessários (wget, unzip e bash)
RUN apk add --no-cache wget unzip bash

# Define o diretório de trabalho
WORKDIR /opt

# Baixa a distribuição do MaryTTS e a descompacta
RUN wget https://github.com/marytts/marytts/releases/download/v5.2/marytts-5.2.zip && \
    unzip marytts-5.2.zip && \
    rm marytts-5.2.zip

# Baixa e instala o pacote de voz para português (exemplo genérico)
RUN wget https://exemplo.com/marytts-pt.zip -O /opt/marytts-pt.zip && \
    unzip /opt/marytts-pt.zip -d /opt/marytts-5.2/lib/voices && \
    rm /opt/marytts-pt.zip \

# Entra no diretório extraído
WORKDIR /opt/marytts-5.2

# Garante que o script do servidor tenha permissão de execução
RUN chmod +x bin/marytts-server

# Expõe a porta padrão do MaryTTS
EXPOSE 59125

# Comando para iniciar o servidor MaryTTS
CMD ["./bin/marytts-server"]
