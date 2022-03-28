import os

TOKEN ="1270834205:AAGJZWSvUDn5B70tn6mV8SoyzKs3tu9YwJQ"
URL = "https://strangerchat.azurewebsites.net"
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
