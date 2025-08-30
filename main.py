import asyncio
import time
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from better_profanity import profanity

# функция проверки
def checker(text) -> bool:
    return profanity.contains_profanity(text)

API_TOKEN = "8026079723:AAFXn7YfECmFjpL42dcCCJU8W6eKaFXNYAk"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(F.text)
async def filter_message(message: Message):
    if checker(message.text):
        try:
            await message.delete()  # Удаляем токсичный текст
            msg = await message.answer(f"@{message.from_user.username}, ваше сообщение нарушает правила сообщества.")
            time.sleep(3)
            await msg.delete()
        except Exception as e:
            print(f"Ошибка при удалении: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
