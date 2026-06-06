from turtle import update

from Models import TodoList
from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import ContextTypes

from Models.Todo import Todo
from Models.TodoList import todoList

class TodoController:

    @staticmethod
    async def add_todo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = "".join( update.message.text.split(command)[1] )
        todoList.append(Todo(title))
        await update.message.reply_text("Nota Agregada!")

    @staticmethod
    async def list_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        if(len(todoList) == 0):
            await update.message.reply_text("No hay notas.")
            return
        ans = ''
        for i, todo in enumerate(todoList):
            ans = ans+f"{i+1} - {'👍' if todo.is_completed else '✖️'} {todo.titulo} \n"
        await update.message.reply_text(ans)

    @staticmethod
    async def checkear_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if( index > len(todoList) or index <= 0 ) :
            await update.message.reply_text("Ese elemento no existe /list")
            return
        
        todoList[index-1].set_completed()
        await update.message.reply_text(f"Elemento {todoList[index-1].titulo} checked:")
        await TodoController.list_todo( update, context )

    @staticmethod
    async def clear_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        todoList.clear()
        await update.message.reply_text("Se borro la lista.")


