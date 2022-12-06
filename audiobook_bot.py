from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from voice import save_file

TOKEN = "5769881258:AAGEeU4o5fYVbQEqDu2oP5yByme14jQSfHA"


async def hello(update, context):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def help_handler(update, context):
    mes = "Я озвучу отправленный вами текст! Попробуйте меня в деле ;)"
    await update.message.reply_text(mes)


async def reply(update, context):
    file_name = save_file(update.message.text)
    await update.message.reply_text('Your entering text is: ' + file_name)
    await update.message.reply_voice(voice=open(file_name, "rb"))


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help_handler))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
