# CRUD-django
aprendendo django


# Como preparar o ambiente Django

O Django é um framework web Python que permite criar aplicativos web de alta qualidade de maneira rápida e fácil. Para começar a desenvolver com Django, você precisa preparar o ambiente. Neste tutorial, mostraremos como fazer isso passo a passo.

## Passo 1: Instale o Python

### 1.1 Verifique se você tem o Python instalado digitando o seguinte comando no terminal:
```
python --version
```
Se você não tiver o Python instalado, você pode baixá-lo do site oficial do [Python](https://www.python.org/downloads/)


## Passo 2: Instale o pip

O pip é o gerenciador de pacotes padrão para Python. Ele é usado para instalar e gerenciar pacotes Python.

### 2.1 Verifique se você tem o pip instalado digitando o seguinte comando no terminal: pip --version


Se você não tiver o pip instalado, você pode instalar usando o seguinte comando:
  ```
    python -m ensurepip --default-pip
  ```
### passo 3 Criando uma venv em um projeto Python
#### venv
   é uma abreviação para "virtual environment" ou "ambiente virtual". Em termos simples, uma venv é uma ferramenta do Python que permite isolar um ambiente de desenvolvimento Python do ambiente global do seu sistema. Isso significa que você pode instalar pacotes e bibliotecas Python específicas para um projeto sem interferir nas outras instalações de pacotes e bibliotecas em seu sistema.

3.1. Abra o terminal e navegue até o diretório raiz do seu projeto.
3.2. Digite o seguinte comando para criar uma nova venv no diretório atual:
  ```
   python -m venv nome_da_venv
  ```

   Substitua `nome_da_venv` pelo nome que você deseja dar à sua `venv`.

3.3. Ative a sua `venv` com o comando:<br/>
#### Linux
  ```
   source nome_da_venv/bin/activate
  ```
    
#### windows
   ```
    nome_da_venv\Scripts\activate.bat
   ```

3.4. Agora você pode instalar as dependências do seu projeto dentro da `venv` usando o `pip`. Por exemplo:

  ```
    pip install pacote
  ```

3.5. Quando terminar de trabalhar no seu projeto, você pode desativar a `venv` com o comando:

  ```
    deactivate
  ```
## Passo 4: Instale o Django

### 4.1 Use o seguinte comando para instalar a versão mais recente do Django:

```
pip install Django
```
Se você deseja instalar uma versão específica do Django, use o seguinte comando:
```
pip install Django==<versão>
```

Substitua `<versão>` pela versão específica que deseja instalar.

## Passo 5: Verifique se o Django foi instalado corretamente

### 5.1 digite o seguinte comando no terminal:
```
django-admin --version
```


Se o Django foi instalado corretamente, você deve ver a versão do Django instalada.




