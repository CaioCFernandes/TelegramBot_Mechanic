import os
import google.generativeai as genai
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, MessageHandler

# Carrega variáveis
load_dotenv(".env")

# Configura a IA (Google Gemini)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Configuração do Modelo
generation_config = {
    "temperature": 0.4, # Baixa temperatura para ele ser mais "técnico" e menos "criativo/alucinado"
}

# Escolhendo o modelo que vimos na sua lista que funciona bem
model = genai.GenerativeModel(
    model_name="models/gemini-2.5-flash", 
    generation_config=generation_config
)

async def consultor_automotivo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_msg = update.message.text
    
    # Feedback visual ("escrevendo...")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

    try:
        # --- O CÉREBRO: PROMPT DE SISTEMA ---
        # Aqui definimos que ele é um especialista em carros
        prompt_sistema = (
            "Você é um Consultor Automotivo Sênior e Especialista em Mercado Brasileiro. "
            "Sua função é ajudar o usuário a escolher ou conhecer carros. "
            "Seja direto, educado e use formatação bonita (Markdown/Emojis). "
            
            "MODO 1: SE O USUÁRIO PERGUNTAR DE UM CARRO ESPECÍFICO (Ex: 'Civic 2010')"
            "Retorne uma ficha técnica RESUMIDA contendo obrigatoriamente:"
            "- 🚗 Nome Completo e Motorização provável"
            "- ⚙️ Câmbio (Automático/Manual)"
            "- ⛽ Consumo Médio (Cidade/Estrada)"
            "- 🛠️ Manutenção (Barata/Média/Cara)"
            "- ✅ Pontos Positivos"
            "- ⚠️ Pontos de Atenção (Defeitos crônicos conhecidos)"
            "- 💰 Preço Médio de Mercado (Estimativa Brasil)"
            
            "MODO 2: SE O USUÁRIO PEDIR RECOMENDAÇÃO (Ex: 'Carro pra família até 50k')"
            "Analise o orçamento e o uso. Sugira 3 opções de carros bons de mercado."
            "Para cada opção, diga o modelo, ano aproximado e por que ele é bom para aquele uso."
            
            "MODO 3: DADOS INCOMPLETOS"
            "Se o usuário falar apenas 'Civic', pergunte educadamente: 'Qual o ano e versão aproximada? Isso muda o motor e o preço.' "
            
            "IMPORTANTE: Baseie-se no mercado brasileiro (carros nacionais ou importados vendidos no Brasil)."
        )

        # Montamos a conversa para enviar a IA
        # O Gemini aceita o contexto dentro do prompt ou como histórico.
        # Vamos mandar tudo junto para garantir a instrução.
        full_prompt = f"{prompt_sistema}\n\n--- MENSAGEM DO USUÁRIO: {user_msg} ---"

        response = model.generate_content(full_prompt)
        
        # TENTATIVA SEGURA DE ENVIO
        try:
            # Tenta enviar com formatação bonita (Markdown)
            await update.message.reply_text(response.text, parse_mode='Markdown')
        except Exception as e_telegram:
            print(f"Erro de formatação Markdown ({e_telegram}). Enviando texto puro...")
            # Se falhar (por causa de um _ ou * solto), envia o texto puro
            await update.message.reply_text(response.text)

    except Exception as e:
        print(f"Erro geral: {e}")
        await update.message.reply_text("Desculpe, estou com uma falha no motor agora (Erro técnico).")

# Configuração do Bot
application = ApplicationBuilder().token(str(os.getenv("token"))).build()

# Handler único: O bot lê tudo e a IA decide o que fazer
handler = MessageHandler(filters.TEXT & (~filters.COMMAND), callback=consultor_automotivo)
application.add_handler(handler)

print("Consultor Automotivo IA iniciado! 🚗")
application.run_polling()