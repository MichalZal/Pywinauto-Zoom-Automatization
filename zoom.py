from pywinauto import Application
import time
from pynput import keyboard
import zoom_connect

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
    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran')
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
    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran')
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
    udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran')
    udostepnij_ekran_przycisk.click_input()
  except ValueError: 
    print("error: " + ValueError)

def zatrzymaj_udostepnianie(): 
  sterowniki_spotkania = Application(backend='uia').connect(title='Sterowniki spotkania', timeout=10)
  # sterowniki_spotkania.Sterownikispotkania.print_control_identifiers()

  zatrzymaj_udostepnianie_przycisk = sterowniki_spotkania.Sterownikispotkania.child_window(title="Zatrzymaj udostępnianie (Alt+S)", control_type="Button")
  zatrzymaj_udostepnianie_przycisk.click_input()
# ==================koniec funkcji zoomowych====================



# while True:
#   dzialanie = input(
#       "Co chcesz zrobic?: \n"
#       "1. Udostepnij ekran z dziwekiem \n"
#       "2. Udostepnij ekran bez dzwieku \n"
#       "3. Udostepnij pod kątem wideoklipu \n"
#       "4. Zatrzymaj udostępnianie ekranu \n"
#       "5. Wyłącz program \n"
#       "\nWybieraj: "
#     )


def on_press(key):
  try:
    wybor = format(key.char)
    print('wybor: ' + wybor)

    if wybor == '1':
      udostepnij_ekran_z_dziwekiem()
    elif wybor == '2':
      udostepnij_ekran_bez_dzwieku()
    elif wybor == '3':
      udostepnij_ekran_jako_wideoklip()
    elif wybor == '4':
      zatrzymaj_udostepnianie()
    elif wybor == '5':
      exit
  except ValueError1:
    print('błąd')



def on_release(key):
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
    
listener.start()
