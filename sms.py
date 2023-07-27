import requests
import os

from termcolor import colored

print ("")
print (colored("   _____                _    _____ __  __  _____  ", "light_red"))
print (colored("  / ____|              | |  / ____|  \/  |/ ____| ", "light_red"))
print (colored(" | (___   ___ _ __   __| | | (___ | \  / | (___   ", "light_red"))
print (colored("  \___ \ / _ \ '_ \ / _` |  \___ \| |\/| |\___ \  ", "light_red"))
print (colored("  ____) |  __/ | | | (_| |  ____) | |  | |____) | ", "light_red"))
print (colored(" |_____/ \___|_| |_|\__,_| |_____/|_|  |_|_____/  ", "light_red"))
print (colored("                                 Created by JuanK ", "light_magenta"))
print ("")

number = input(colored("[+] Número: ", "light_green"))
message = input(colored("[+] Mensaje: ", "light_green"))

# CHECK CONNECTION
try:
    request = requests.get("https://www.google.com", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    print ("")
    print (colored("[!] Sin conexión a internet.", "light_red"))
    print ("")
else:
    
    # ENVÍO DE DATOS
    resp = requests.post('https://textbelt.com/text', {

      'phone': number,
      'message': message,
      'key': 'textbelt',

    })
    
    # RESPUESTA JSON
    response = resp.json()

    print ("")

    if response["success"] == True:
       print (colored("[+] El mensaje se ha enviado con éxito.\n", "light_green"))

       # CREA UN ARCHIVO CON LOS DATOS ENVIADOS
       if not os.path.isfile('record.txt'):
           f = open('record.txt', 'w')
           f.write('Número: ' + str(number) + '\nMensaje: ' + str(message) + '\n\n')
           f.close()
       else:
           with open('record.txt', 'a') as f:
               f.write('Número: ' + str(number) + '\nMensaje: ' + str(message) + '\n\n')
    else:
       print (colored("[!] No se pudo enviar el mensaje por la siguiente razón:\n", "light_red"))
       print (colored(response["error"], "light_red"))
