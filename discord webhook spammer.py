import time
from discord_webhook import DiscordWebhook

url=(input('url du webhook ?'))
print("webhook défini sur", url)

message=(input('message à envoyer ?'))
print("le message spammé sera :")
print(message)

Nmsg=int(input('combien de message seront envoyés ?'))

input("Appuyez sur entrée pour lancer le spam")

for i in range(0,Nmsg):
    webhook = DiscordWebhook(url=url, content=message)
    response = webhook.execute()

print("Le spam est terminé")