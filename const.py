TOKEN = '5897936893:AAG8hB2weBOVZrLuF0fROqsBYa-jzeI4qMM'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'
MY_ID = 210944778
UPDATE_ID_FILE = 'update_id'
with open(UPDATE_ID_FILE) as file:
    UPDATE_ID = file.readline()

WEATHER_TOKEN = 'a272a152c1d896bc2c120e9ace22caae'

WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
# https://api.openweathermap.org/data/2.5/weather?q={London}&appid={a272a152c1d896bc2c120e9ace22caae}