from pywinauto import Application
import time
from pynput import keyboard
import serial

# import zoom_connect
# cały kod jest w zoom_connect.py. Tam jest funkcja łącząca do spotkania

# Automatyzacja funkcjonowania
Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie')
Spotkanie.Zoomspotkanie.click_input()
# Spotkanie.ZoomSpotkanie.print_control_identifiers()

# funkcje:
def udostepnij_ekran_z_dziwekiem(): # działa
  try:
    # Łączymy się z oknem spotkania
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie')
    Spotkanie.Zoomspotkanie.click_input()
    #Spotkanie.ZoomSpotkanie.print_control_identifiers()

    #kliknięcie w przycisk udostępnij ekran
    udostepnij_ekran = Spotkanie.ZoomSpotkanie.child_window(title='Udostępnij ekran, Alt+S').wrapper_object()
    udostepnij_ekran.click_input()

    # łączymy się z oknem udostępniania ekranu
    udostepnij_ekran_okno = Application(backend='uia').connect(title='Wybierz okno lub aplikację, którą chcesz udostępnić')
    # udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

    # zapisujemy przycisk "z dźwiękiem" do zmiennej
    z_dzwiekiem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Udostępnij dźwięk", control_type="CheckBox").wrapper_object()
    z_wideoklipem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Zoptymalizuj pod kątem wideoklipu", control_type="CheckBox").wrapper_object()

    if (z_dzwiekiem.get_toggle_state() == 0): 
      z_dzwiekiem.toggle()
    elif (z_dzwiekiem.get_toggle_state() == 1):
      pass
    else:
      print("błąd")

    if (z_wideoklipem.get_toggle_state() == 1):
      z_wideoklipem.toggle()

    # ekran udostępniony
    # udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran 1')
    udostepnij_ekran_przycisk.click_input()
  except ValueError: 
    print("error: " + ValueError)

def udostepnij_ekran_bez_dzwieku():
  try:
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie')
    Spotkanie.Zoomspotkanie.click_input()

    udostepnij_ekran = Spotkanie.ZoomSpotkanie.child_window(title='Udostępnij ekran, Alt+S').wrapper_object()
    udostepnij_ekran.click_input()

    udostepnij_ekran_okno = Application(backend='uia').connect(title='Wybierz okno lub aplikację, którą chcesz udostępnić')
    # udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

    z_dzwiekiem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Udostępnij dźwięk", control_type="CheckBox").wrapper_object()
    z_wideoklipem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Zoptymalizuj pod kątem wideoklipu", control_type="CheckBox").wrapper_object()


    if (z_dzwiekiem.get_toggle_state() == 0): 
      pass
    elif (z_dzwiekiem.get_toggle_state() == 1):
      z_dzwiekiem.toggle()
    else:
      print("błąd")

    if (z_wideoklipem.get_toggle_state() == 1):
      z_wideoklipem.toggle()

    # ekran udostępniony
    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran 1')
    udostepnij_ekran_przycisk.click_input()
  except ValueError: 
    print("error: " + ValueError)

def udostepnij_ekran_jako_wideoklip():
  try:
    # Łączymy się z oknem spotkania
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()
    #Spotkanie.ZoomSpotkanie.print_control_identifiers()

    #kliknięcie w przycisk udostępnij ekran
    udostepnij_ekran = Spotkanie.ZoomSpotkanie.child_window(title='Udostępnij ekran, Alt+S').wrapper_object()
    udostepnij_ekran.click_input()

    # łączymy się z oknem udostępniania ekranu
    udostepnij_ekran_okno = Application(backend='uia').connect(title='Wybierz okno lub aplikację, którą chcesz udostępnić', timeout=5)
    # udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

    # zapisujemy przycisk "z dźwiękiem" do zmiennej
    z_dzwiekiem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Udostępnij dźwięk", control_type="CheckBox").wrapper_object()
    z_wideoklipem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Zoptymalizuj pod kątem wideoklipu", control_type="CheckBox").wrapper_object()

    if (z_dzwiekiem.get_toggle_state() == 0 ): 
      z_dzwiekiem.toggle()

    if (z_wideoklipem.get_toggle_state() == 0):
      z_wideoklipem.toggle()

    # ekran udostępniony
    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran 1')
    udostepnij_ekran_przycisk.click_input()
  except ValueError: 
    print("error: " + ValueError)

def zatrzymaj_udostepnianie(): 
  sterowniki_spotkania = Application(backend='uia').connect(title='Sterowniki spotkania', timeout=10)
  # sterowniki_spotkania.Sterownikispotkania.print_control_identifiers()

  zatrzymaj_udostepnianie_przycisk = sterowniki_spotkania.Sterownikispotkania.child_window(title="Zatrzymaj udostępnianie (Alt+S)", control_type="Button")
  zatrzymaj_udostepnianie_przycisk.click_input()

def mikrofon():
  print('mikrofon')
  # Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
  # Spotkanie.Zoomspotkanie.click_input()

  # mikrofon_wlacz = "Wyłącz wyciszenie, tymczasowo wyciszono, Alt+A"
  # mikrofon_wylacz = "Wycisz, tymczasowo wyłączono wyciszenie, Alt+A"

  # mikrofon_ikonka = Spotkanie.Zoomspotkanie.child_window(title="Wyłącz wyciszenie, tymczasowo wyciszono, Alt+A", control_type="Button")
  # mikrofon_ikonka.click_input()


def kamera():
  print("kamera")
  # Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
  # Spotkanie.Zoomspotkanie.click_input()

  # kamerka_ikonka_wlacz = Spotkanie.ZoomSpotkanie.child_window(title="rozpocznij moje wideo, Alt+V", control_type="Button")
  # kamerka_ikonka_wylacz = Spotkanie.ZoomSpotkanie.child_window(title="zatrzymaj moje wideo , Alt+V", control_type="Button")

  # if kamerka_ikonka_wylacz in locals():
  #   kamerka_ikonka_wylacz.click_input()

  # if kamerka_ikonka_wlacz in locals():
  #   kamerka_ikonka_wlacz.click_input()

  
# ==================koniec funkcji zoomowych====================

port = int(input('Podaj port byku: '))

ser = serial.Serial(
    port=f'COM{port}',\
    baudrate=74880,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0.5)

print("connected to: " + ser.portstr)

buttonState1 = 0
lastbuttonState_1 = 0

buttonState2 = 0
lastbuttonState_2 = 0

buttonState3 = 0
lastbuttonState_3 = 0

buttonState4 = 0
lastbuttonState_4 = 0

buttonState5 = 0
lastbuttonState_5 = 0

buttonState6 = 0
lastbuttonState_6 = 0

buttonState7 = 0
lastbuttonState_7 = 0

buttonState8 = 0
lastbuttonState_8 = 0

while True:
  line = str(ser.readline())
  # print(line)

  if line.find('S11') != -1:
    buttonState1 = 1
    if buttonState1 != lastbuttonState_1:
      udostepnij_ekran_jako_wideoklip()
  lastbuttonState_1 = buttonState1
  buttonState1 = 0

  if line.find('S2:1') != -1:
    buttonState2 = 1
    if buttonState2 != lastbuttonState_2:
      udostepnij_ekran_bez_dzwieku()
  lastbuttonState_2 = buttonState2
  buttonState2 = 0

  if line.find('S3:1') != -1:
    buttonState3 = 1
    if buttonState3 != lastbuttonState_3:
      mikrofon()
  lastbuttonState_3 = buttonState3
  buttonState3 = 0

  if line.find('S4:1') != -1:
    buttonState4 = 1
    if buttonState4 != lastbuttonState_4:
      kamera()
  lastbuttonState_4 = buttonState4
  buttonState4 = 0

  if line.find('S5:1') != -1:
    buttonState5 = 1
    if buttonState5 != lastbuttonState_5:
      zatrzymaj_udostepnianie()
  lastbuttonState_5 = buttonState5
  buttonState5 = 0

  if line.find('S6:1') != -1:
    buttonState6 = 1
    if buttonState6 != lastbuttonState_6:
      udostepnij_ekran_jako_wideoklip()
  lastbuttonState_6 = buttonState1
  buttonState6 = 0

  if line.find('S7:1') != -1:
    buttonState7 = 1
    if buttonState7 != lastbuttonState_7:
      udostepnij_ekran_jako_wideoklip()
  lastbuttonState_7 = buttonState7
  buttonState7 = 0

  if line.find('S8:1') != -1:
    buttonState8 = 1
    if buttonState8 != lastbuttonState_8:
      udostepnij_ekran_jako_wideoklip()
  lastbuttonState_8 = buttonState8
  buttonState8 = 0

ser.close() 