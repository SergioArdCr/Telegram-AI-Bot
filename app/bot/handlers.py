from telegram import Update
from telegram.ext import ContextTypes
from app.agent.agent import ejecutar_agente

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text("⏳ Consultando...")

    try:
        respuesta = ejecutar_agente(texto)
        await update.message.reply_text(respuesta)
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")