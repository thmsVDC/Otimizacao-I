# **Projeto de Otimização** 🎯

## 🎓 Projeto de Faculdade

O **Projeto de Otimização** é uma aplicação web simples e interativa, desenvolvida como parte de um projeto de faculdade, que permite otimizar funções objetivo e restrições matemáticas. Através de uma interface amigável, os usuários podem definir o número de variáveis, inserir coeficientes para a função objetivo e as restrições, e visualizar os resultados da otimização. 🌟

Este projeto utiliza **Flask**, **Jinja2**, **JavaScript** e **CSS Responsivo** para proporcionar uma experiência dinâmica e otimizada.

## Funcionalidades 🌈

- **Função Objetivo**: Insira coeficientes das variáveis e defina a equação `Z = C1*X1 + C2*X2 + ... + Cn*Xn`. 🧮
- **Restrições**: Defina múltiplas restrições com coeficientes, operadores (≤ ou ≥) e valores. 🔒
- **Otimização**: Clique no botão **Otimizar** e veja os resultados! (ainda em construção). 🎯

## 📋 Requisitos

- **Python 3.x**
- **Flask**
- **Jinja2**
- **Bootstrap**
- **JavaScript**
- **CSS Responsivo**

## Estrutura do Projeto 🛠️

/Projeto de Otimização
│
├── app/
│   ├── init.py
│   ├── routes.py
│   ├── models.py (se necessário)
│   └── templates/
│       ├── base.html
│       ├── home.html
│       └── result.html (página de resultados)
│   └── static/
│       ├── styles.css
│       ├── home_page_script.js
│       └── images/
│           └── background.jpg
├── run.py
├── requirements.txt
└── README.md

## Como Rodar o Projeto 🚀

### 1. Clone o repositório

```bash
git clone <URL_do_repositório>
cd Projeto-de-Otimização
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o servidor Flask
```bash
python run.py
```

### 5. Acesse o aplicativo
Abra seu navegador e vá para http://localhost:5000 para começar a usar o aplicativo.

