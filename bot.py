import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

banca = 0.0

async def inicio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Bot de Gestão de Banca\n\n"
        "Comandos:\n"
        "/banca 100\n"
        "/saldo"
    )

async def definir_banca(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global banca

    if not context.args:
        await update.message.reply_text("Use: /banca 100")
        return

    try:
        banca = float(context.args[0])
        await update.message.reply_text(f"✅ Banca definida em R${banca:.2f}")
    except ValueError:
        await update.message.reply_text("Digite um número válido.")

async def saldo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"💰 Saldo atual: R${banca:.2f}")

def main():
    token = os.environ["BOT_TOKEN"]

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("inicio", inicio))
    app.add_handler(CommandHandler("banca", definir_banca))
    app.add_handler(CommandHandler("saldo", saldo))

    app.run_polling()

if __name__ == "__main__":
    main()
