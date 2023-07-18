import requests

from termcolor import colored
from pyfiglet import figlet_format

text = figlet_format("Send SMS", font="big")
print(colored(text, "red"))

number = input(colored("[+] Número: ", "green"))
message = input(colored("[+] Mensaje: ", "green"))

resp = requests.post('https://textbelt.com/text', {

  'phone': number,
  'message': message,
  'key': 'textbelt',

})

response = resp.json()

print ("")

if response["success"] == "true":
   print (colored("El mensaje se ha enviado con éxito", "green"))
else:
   print (colored("No se pudo enviar el mensaje por la siguiente razón:", "red"))
   print ("")
   print (colored(response["error"], "red"))

