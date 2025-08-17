from aiogram import Router, types
from main import get_doge_pic

router = Router(name=__name__)

@router.message()
async def echo_handler(message: types.Message):
    try:
        if message.text == 'woof':
            pic_url, breeds = await get_doge_pic()
            await message.answer_photo(photo=pic_url, caption=breeds)
        else:
            await message.answer("Sorry, bro, but I don't know how to do anything else but throw doge...")
            await message.answer_sticker('CAACAgQAAxkBAAENqetnmna2yveoBoqErzSjrtOJyZcsHQACnRUAAtKA0VIkyAO50FdLtTYE')
    except exception as e:
        print(e)
        await message.answer('Sorry, bro, something went wrong')
        await message.answer_sticker('CAACAgQAAxkBAAENqetnmna2yveoBoqErzSjrtOJyZcsHQACnRUAAtKA0VIkyAO50FdLtTYE')