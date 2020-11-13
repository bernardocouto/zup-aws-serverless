# Zup AWS Serverless

Compartilhando conhecimento referente à estrutura AWS Serverless

## Instruções

1. Instale o **[AWS Cli](https://aws.amazon.com/pt/cli/)** e o **[Python](https://www.python.org)**, se ainda não o tiver.

2. Agora clone o repositório:

    ```sh
    $ git clone git@github.com:bernardocouto/zup-aws-serverless.git
    ```

3. Em seguida, vá para o diretório do projeto:

    ```sh
    $ cd zup-aws-serverless
    ```

4. Crie um ambiente virtual do Python (Opcional):

    ```sh
    $ python3 -m venv venv
    ```

5. Ative o ambiente virtual:

    ```sh
    $ source venv/bin/activate
    ```

6. Instale todas as dependências:

    ```sh
    $ pip install -r requirements.txt
    ```

7. Execute localmente:

    ```sh
    $ python3 application.py
    ```

## Deploy

1. Configure a AWS Cli:

    ```sh
    $ aws configure
    ```

2. Deploy utilizando o Zappa:

    ```sh
    $ zappa deploy <stage>
    ```

3. Atualização da versão do código na AWS:

    ```sh
    $ zappa update <stage>
    ```

4. Deleção do ambiente na AWS:

    ```sh
    $ zappa undeploy
    ```
