# **Projeto de Otimização** 🎯

## 🎓 Projeto de Faculdade

O **Projeto de Otimização** é uma aplicação web simples e interativa, desenvolvida como parte de um projeto de faculdade, que permite otimizar funções objetivo e restrições matemáticas. Através de uma interface amigável, os usuários podem definir o número de variáveis, inserir coeficientes para a função objetivo e as restrições, e visualizar os resultados da otimização. 🌟

Este projeto utiliza **Flask**, **Jinja2** para proporcionar uma experiência dinâmica e otimizada.

## Funcionalidades 🌈

- **Função Objetivo**: Insira coeficientes das variáveis e defina a equação `Z = C1*X1 + C2*X2 + ... + Cn*Xn`. 🧮
- **Restrições**: Defina múltiplas restrições com coeficientes, operadores (≤ ou ≥) e valores. 🔒
- **Otimização**: Clique no botão **Otimizar** e veja os resultados! 🎯
- **Pós Otimização**: Realize uma análise de sensibilidade e verifique se é viável ou não essa alteração. 🎯

## 📋 Requisitos

- **Python 3.x**
- **Flask**
- **Jinja2**
- **Bootstrap**

## Estrutura do Projeto

```plaintext
Projeto de Otimização
│
├── app/
│    ├── templates/
│    │    ├── form.html
│    │    ├── post_optimization.html
│    │    └── result.html
│    │
│    ├── utils/
│    │    ├── form_utils.py
│    │    ├── post_optimization_utils.py
│    │    └── shadow_price_process.py
│    │
│    └── routes.py
│
├── config.py
├── README.md
├── requirements.txt
└── run.py
```

## Como Rodar o Projeto 🚀

### 1. Clone o repositório

```bash
git clone https://github.com/thmsVDC/projeto-otimizacao.git
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

