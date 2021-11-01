<h1 align="center">Teste de unidade com Pytest</h1>

# Tópicos

- [O Projeto](#-o-projeto)
- [Equipe](#-equipe")
- [Arquivos](#-arquivos)

# O Projeto 📈
Material desenvolvido para o seminário de Frameworks da matéria de Engenharia de Software (C214), ministrada pelo professor **Phyllipe Lima**.
Devemos apresentar alguns testes de unidade feitos com o ***Pytest***. Para isso desenvolvemos uma simples calculadora em ***python***.

## Equipe
* 👧 Ana Terra
* 👦 Paulo Eduardo
* 👦 Paulo Rotundaro
* 👦 Pedro Abritta

### Instalação ⚙💻
Se você entende um pouco de inglês e gostaria de saber todas as informações sobre essa ferramenta de teste, você pode acessar a documentação oficial do <a href="https://docs.pytest.org/en/stable/index.html">Pytest</a>.
Mas não se preocupe, o processo de instalação é super simples! Vou te passar o passo a baixo aqui em baixo:

Para instalar o Pytest é preciso ter também em sua máquina o <a href="https://pypi.org/project/pip/">PIP</a>, gerenciador de pacotes do Python.
Normalmente, o PIP é instalado automaticamente se você:
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
- 3º Adicione PIP nas suas variáveis de ambiente do Windows, para poder rodar o comando de qualquer lugar.

### Versão e atualização
- Para verificar se instalou corretamente e saber sua versão, rode o seguinte comando:
```bash
pip --version
```

- Para atualizar sua versão do PIP, rode o seguinte comando:
```bash
python -m pip install --upgrade pip
```

## Arquivos :open_file_folder:
<!--ts-->
  * :file_folder: calculadora
    * :file_folder: test
        * :page_facing_up: __init__.py
        * :page_facing_up: [test_multiplicacao_divisao.py](#test-multiplicacao-divisao)
        * :page_facing_up: [test_soma_subtracao.py](#test-soma-subtracao)
     * :page_facing_up: __init__.py
     * :page_facing_up: [calculadora.py](#calculadora)
<!--te-->

## calculadora
![image](https://user-images.githubusercontent.com/73140691/139708100-b411dcec-753f-46ff-931c-5f01a6965640.png)

## test-multiplicacao-divisao
![image](https://user-images.githubusercontent.com/73140691/139708238-1ba0f584-af3f-416e-8759-e8320d4e14cb.png)

## test-soma-subtracao
![image](https://user-images.githubusercontent.com/73140691/139708280-9f5f391f-7802-4c33-a0ad-a0faf8abd680.png)
