# Define a imagem
FROM python:3.13.5-alpine3.22   

# Criando diretório onde os comandos posteriores serão executados
WORKDIR /api-avaliaplay

# Copiando tudo da aplicação para o conteiner
COPY . /api-avaliaplay/

# Instala as dependências da aplicação, esse --no-cache-dir é importante!!
RUN pip install --no-cache-dir -r requirements.txt

# Definindo a porta de acesso
EXPOSE 8000

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
