from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='начало работы'
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='cansel',
            description='Отмена'
        ),
        BotCommand(
            command='shut_down',
            description='Пока'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
