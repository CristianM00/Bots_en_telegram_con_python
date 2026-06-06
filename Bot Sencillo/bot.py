from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
from Controllers.TodoController import TodoController



app = ApplicationBuilder().token(Token).build()

app.add_handler(CommandHandler("add", TodoController.add_todo))
app.add_handler(CommandHandler("list", TodoController.list_todo))
app.add_handler(CommandHandler("check", TodoController.checkear_todo))
app.add_handler(CommandHandler("clear", TodoController.clear_todo))

app.run_polling(allowed_updates=Update.ALL_TYPES)