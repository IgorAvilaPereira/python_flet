# python_flet

## Criando Projeto e o virtualenv

```sh
mkdir first-flet-app
cd first-flet-app
python3 -m venv .venv
source .venv/bin/activate
```

## Instalando o Flet

```sh
pip install flet[all]
```

## Criando um projeto

```sh
flet create
```

## Exemplo

```python
import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
```

## Rodando

```sh
flet run [script]
```

### Web

```sh
flet run --web [script]
```

## Diretório - Projeto Padrão Flet

```
├── README.md
├── pyproject.toml
├── src
│   ├── assets
│   │   └── icon.png
│   └── main.py
└── storage
    ├── data
    └── temp
```

### Desktop

```sh
flet run
```

### Web

```sh
flet run --web
```

### App Android

https://play.google.com/store/apps/details?id=com.appveyor.flet

```sh
flet run --android
```

### App IOs

https://apps.apple.com/app/flet/id1624979699

```sh
flet run --ios
```

## Build

* https://flet.dev/docs/publish/android

```sh
sudo snap install flutter --classic
sudo snap install android-studio --classic
flet build apk
```

* https://flet.dev/docs/publish/ios

* https://flet.dev/docs/publish/linux

* https://flet.dev/docs/publish/windows

* https://flet.dev/docs/publish/web

### Sqlite

https://docs.python.org/pt-br/3.9/library/sqlite3.html

```sh
sqlite3 my_database.db
```

```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price REAL
);
```

```python
    import sqlite3

    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
        conn.commit()

    with sqlite3.connect('my_database.db') as conn:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
```

### API Pokemon

https://github.com/PokeAPI/pokebase

### OFF-TOPIC:

https://console.groq.com/docs/quickstart
```sh
pip install groq
```

<!--
#### 🔍 Modelos bons gratuitos


| Modelo                          | Tamanho / Parâmetros / Bits / Quantização                                                           | Pontos fortes                                                                                                                                          | Restrições / O que você precisa considerar                                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Llama-3 (8B ou 70B)** da Meta | Versão open-source, com quantizações disponíveis (ex: GGUF, bits menores). ([GIGAZINE][1])          | É um dos mais recentes da Meta; bom equilíbrio entre desempenho e custo computacional, especialmente o de 8 bilhões de parâmetros. Boa para uso geral. | O modelo de 70B exige bastante memória; usar quantizações é quase obrigatório para rodar localmente com bom desempenho. ([Reddit][2]) |
| **Llama-2 (7B / 13B / 70B)**    | Modelos bem conhecidos, versões base e ajustadas. Versões em GGUF também disponíveis. ([MyGGUF][3]) | Estável, bem estudado, muitos recursos e bibliotecas/pacotes já suportam. Boa escolha se quiser compatibilidade e documentação.                        | Também o de maior porte consome muito; para tarefas simples, talvez o 7B já seja suficiente.                                          |
| **Mistral-7B (Instruct)**       | Um modelo “menor”, bom custo computacional. ([localaimaster.com][4])                                | Excelente para criatividade / geração de texto quando não se precisa de algo extremamente grande. Carrega mais rápido, uso de RAM menor.               | Pode perder em tarefas que requeiram muito contexto ou “raciocínio” mais pesado comparado aos maiores.                                |
| **TinyLlama**                   | \~1.1B parâmetros. ([arXiv][5])                                                                     | Muito leve, roda fácil mesmo em máquinas modestas; bom para protótipos, testagens rápidas, tarefas simples.                                            | Com desempenho menor, respostas menos refinadas se comparar com modelos grandes. Não é ideal para uso “pesado”.                       |



---

#### Llama

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install llama-cpp-python
```

```python
from llama_cpp import Llama

# Carregue um modelo LLaMA (precisa ter o arquivo .gguf baixado antes)
llm = Llama(model_path="models/llama-2-7b-chat.Q4_K_M.gguf")

# Fazendo uma pergunta ao modelo
output = llm(
    "Explique em poucas palavras o que é aprendizado de máquina.",
    max_tokens=100,
    temperature=0.7,
)

print(output["choices"][0]["text"])
```


python3 Llama.py


