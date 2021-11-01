<h1 align="center">Teste de unidade com Pytest</h1>

## Tópicos

- [O Projeto](#o-projeto-)
- [Equipe](#equipe)
- [Instalação](#instalação-)
   - [Pré-requisitos](#pré-requisitos)
   - [Versão e atualização do PIP](#versão-e-atualização)
   - [Instalação do Pytest](#instalando-o-pytest)
- [Testes](#testes)
- [Arquivos](#arquivos-open_file_folder)

# O Projeto 📈
Projeto desenvolvido para o seminário de Frameworks da matéria de Engenharia de Software (C214), ministrada pelo professor **Phyllipe Lima**.<br>
A atividade consiste em apresentar alguns testes de unidade feitos com uma ferramenta de testes, a qual, para nosso grupo foi a ***Pytest***. Para isso desenvolvemos uma simples calculadora em ***python***.

## Equipe
* 👧 Ana Terra
* 👦 Paulo Eduardo
* 👦 Paulo Rotundaro
* 👦 Pedro Abritta

## Instalação ⚙💻
Se você entende um pouco de inglês e gostaria de saber todas as informações sobre essa ferramenta de teste, você pode acessar a documentação oficial do <a href="https://docs.pytest.org/en/stable/index.html">Pytest</a>.
Mas não se preocupe, o processo de instalação é super simples! Vou te passar o passo a baixo aqui em baixo:

### Pré-requisitos
#### Para instalar o Pytest é preciso ter também em sua máquina o <a href="https://pypi.org/project/pip/">PIP</a>, gerenciador de pacotes do Python.<br>
#### Normalmente, o PIP é instalado automaticamente se você:
- Está usando Python baixado de <a href="https://www.python.org/">python.org</a>

Antes de tudo, abra um console com permissão de administrador no seu computador.
Após aberto, siga os seguintes passos:
- 1º Rode o seguinte comando para baixar o arquivo "get-pip.py":
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
- 2º Instalando PIP no windows:
```bash
python(ou py) get-pip.py
```
- 3º Adicione PIP nas suas <a href="https://www.noticiastecnicas.com/variaveis-de-ambiente-do-sistema-e-do-usuario-no-windows-explicadas/">variáveis de ambiente</a> do Windows, para poder rodar o comando de qualquer lugar.

### Versão e atualização
- Para verificar se instalou corretamente e saber sua versão, rode o seguinte comando:
```bash
pip --version
```

- Para atualizar sua versão do PIP, rode o seguinte comando:
```bash
python -m pip install --upgrade pip
```

### Instalando o Pytest
- 1º Com um simples comando você já instala o Pytest:
```bash
pip install -U pytest
```

- 2º Para saber a versão do Pytest, também é simples:
```bash
pytest --version
```

## Testes
### Para realização dos testes, 3 comandos podem ser feitos:
- 1º (Rodar todos os arquivos de teste):
```bash
pytest
```

- 2º (Rodar um arquivo de teste específico):
```bash
pytest nome_do_arquivo.py
```

- 3º (Rodar os testes, até encontrar um erro):
```bash
pytest -x ou pytest nome_do_arquivo.py -x
```

## Arquivos :open_file_folder:
<!--ts-->
  * :file_folder: calculadora
    * :file_folder: test
        * :page_facing_up: __init__.py
        * :page_facing_up: [test_multiplicacao_divisao.py](#teste-multiplicaçãodivisão)
        * :page_facing_up: [test_soma_subtracao.py](#teste-adiçãosubtração)
     * :page_facing_up: __init__.py
     * :page_facing_up: [calculadora.py](#calculadora)
<!--te-->

## Calculadora
![image](https://user-images.githubusercontent.com/73140691/139708100-b411dcec-753f-46ff-931c-5f01a6965640.png)

## Teste multiplicação/divisão
![image](https://user-images.githubusercontent.com/73140691/139708238-1ba0f584-af3f-416e-8759-e8320d4e14cb.png)

## Teste adição/subtração
![image](https://user-images.githubusercontent.com/73140691/139708280-9f5f391f-7802-4c33-a0ad-a0faf8abd680.png)
