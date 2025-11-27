````markdown
# 🚗 AI Car Consultant Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-orange)

[🇬🇧 English](#-english) | [🇧🇷 Português](#-português)

---

## 🇬🇧 English

### 📖 About the Project
**AI Car Consultant** is a Telegram bot powered by **Google Gemini AI**. Unlike traditional bots that only query static databases (like FIPE tables), this assistant uses Generative AI to provide context-aware information about the Brazilian automotive market.

It acts as a specialized consultant, capable of providing technical specifications, analyzing pros/cons, estimating maintenance costs, and suggesting vehicles based on the user's budget and usage profile.

### 🚀 Key Features
- **Detailed Specs:** Ask for any car (e.g., *"Honda Civic 2010"*) and get engine details, transmission type, and fuel consumption.
- **Pros & Cons Analysis:** The bot highlights the good points and warns about chronic defects or expensive maintenance.
- **Personalized Recommendations:** Ask for advice (e.g., *"Best car for Uber under R$ 40k"*) and get tailored suggestions.
- **Natural Language Processing:** No need for rigid commands. Just chat naturally.

### 🛠️ Tech Stack
- **Language:** Python
- **Interface:** [python-telegram-bot](https://python-telegram-bot.org/)
- **Intelligence:** Google Gemini API (`gemini-2.5-flash`)
- **Environment:** python-dotenv

### ⚙️ How to Run Locally

1. **Clone the repository**
   ```bash
   git clone [https://github.com/CaioCFernandes/TelegramBot_Mechanic.git](https://github.com/CaioCFernandes/TelegramBot_Mechanic.git)
   cd TelegramBot_Mechanic
````

2.  **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables**
    Create a `.env` file in the root folder (based on `.env.example`) and add your keys:

    ```env
    token=YOUR_TELEGRAM_BOT_TOKEN
    GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
    ```

4.  **Run the Bot**

    ```bash
    python main.py
    ```

-----

## 🇧🇷 Português

### 📖 Sobre o Projeto

**AI Car Consultant** é um bot de Telegram impulsionado pela IA **Google Gemini**. Diferente de bots tradicionais que apenas consultam bancos de dados estáticos (como a Tabela FIPE), este assistente utiliza IA Generativa para fornecer informações contextualizadas sobre o mercado automotivo brasileiro.

Ele atua como um consultor especializado, capaz de fornecer fichas técnicas, analisar prós/contras, estimar custos de manutenção e sugerir veículos baseados no orçamento e perfil de uso do usuário.

### 🚀 Funcionalidades Principais

  - **Ficha Técnica Detalhada:** Pergunte sobre qualquer carro (ex: *"Honda Civic 2010"*) e receba dados de motor, câmbio e consumo.
  - **Análise de Prós e Contras:** O bot destaca os pontos positivos e avisa sobre defeitos crônicos ou manutenção cara.
  - **Recomendações Personalizadas:** Peça conselhos (ex: *"Melhor carro para Uber até R$ 40 mil"*) e receba sugestões sob medida.
  - **Processamento de Linguagem Natural:** Sem necessidade de comandos rígidos. Converse naturalmente.

### 🛠️ Tecnologias Utilizadas

  - **Linguagem:** Python
  - **Interface:** [python-telegram-bot](https://python-telegram-bot.org/)
  - **Inteligência:** Google Gemini API (`gemini-2.5-flash`)
  - **Ambiente:** python-dotenv

### ⚙️ Como Rodar Localmente

1.  **Clone o repositório**

    ```bash
    git clone [https://github.com/CaioCFernandes/TelegramBot_Mechanic.git](https://github.com/CaioCFernandes/TelegramBot_Mechanic.git)
    cd TelegramBot_Mechanic
    ```

2.  **Instale as dependências**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure as Variáveis de Ambiente**
    Crie um arquivo `.env` na pasta raiz (baseado no `.env.example`) e adicione suas chaves:

    ```env
    token=SEU_TELEGRAM_BOT_TOKEN
    GOOGLE_API_KEY=SUA_GEMINI_API_KEY
    ```

4.  **Execute o Bot**

    ```bash
    python main.py
    ```

-----

### 📝 License

This project is licensed under the MIT License.

Developed by [Caio Fernandes](https://www.google.com/search?q=https://github.com/CaioCFernandes)

````