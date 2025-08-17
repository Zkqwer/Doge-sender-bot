import aiohttp


async def get_doge_pic():
    async with aiohttp.ClientSession() as session:
        id_url = 'https://dog.ceo/api/breeds/image/random'
        async with session.get(id_url) as request:
            response = await request.json()
            pic_url = response.get('message')
            breeds = pic_url.split('/')
            breeds = breeds[4]
        return pic_url, breeds