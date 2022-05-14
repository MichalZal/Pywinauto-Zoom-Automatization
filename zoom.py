from pywinauto import Application
import time
import pyautogui
import zoom_connect

# cały kod jest w zoom_connect.py. Tam jest funkcja łącząca do spotkania
zoom_connect.connect()

# Automatyzacja funkcjonowania
Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
Spotkanie.Zoomspotkanie.click_input()
# Spotkanie.ZoomSpotkanie.print_control_identifiers()

# funkcje:
def udostepnij_ekran_z_dziwekiem(): # działa
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
        
        if (z_dzwiekiem.get_toggle_state() == 0): 
            z_dzwiekiem.toggle()
        elif (z_dzwiekiem.get_toggle_state() == 1):
            pass
        else:
            print("błąd")


        # ekran udostępniony
        udostepnij_ekran_przycisk = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title='Udostępnij Ekran')
        udostepnij_ekran_przycisk.click_input()
    except ValueError: 
        print("error: " + ValueError)


def udostepnij_ekran_bez_dzwieku():
    try:
        Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
        Spotkanie.Zoomspotkanie.click_input()

        udostepnij_ekran = Spotkanie.ZoomSpotkanie.child_window(title='Udostępnij ekran, Alt+S').wrapper_object()
        udostepnij_ekran.click_input()

        udostepnij_ekran_okno = Application(backend='uia').connect(title='Wybierz okno lub aplikację, którą chcesz udostępnić', timeout=5)
        # udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.print_control_identifiers()

        z_dzwiekiem = udostepnij_ekran_okno.Wybierzoknolubaplikacjęktórąchceszudostępnić.child_window(title="Udostępnij dźwięk", control_type="CheckBox").wrapper_object()

        if (z_dzwiekiem.get_toggle_state() == 0): 
            pass
        elif (z_dzwiekiem.get_toggle_state() == 1):
            z_dzwiekiem.toggle()
        else:
            print("błąd")

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


def wycisz_wszystkich_z_mozliwoscia_odciszenia():
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()

    uczestnicy = Spotkanie.ZoomSpotkanie.child_window(title="Zamknięto, otwórz panel z uczestnikami, uczestników: 2, Alt+U", control_type="Button")
    uczestnicy.click_input()


def wycisz_wszystkich_bez_mozliwosci_odciszenia():
    Spotkanie = Application(backend='uia').connect(title='Zoom Spotkanie', timeout=10)
    Spotkanie.Zoomspotkanie.click_input()

    uczestnicy = Spotkanie.ZoomSpotkanie.child_window(title="Zamknięto, otwórz panel z uczestnikami, uczestników: 2, Alt+U", control_type="Button")
    uczestnicy.click_input()


def podziel_na_pokoje_automatycznie():
    pass


# To powoduje, że program w nieskończoność pyta nas co chcemy zrobić. 
while True:
    dzialanie = input(
        "Co chcesz zrobic?: \n"
        "1. Udostepnij ekran z dziwekiem \n"
        "2. Udostepnij ekran bez dzwieku \n"
        "3. Wycisz wszystkich z możliwością odciszenia \n"
        "4. Wycisz wszystkich bez możliwości odciszenia \n"
        "5. Udostepnij pod kątem wideoklipu \n"
        "\nWybieraj: "
        )

    if dzialanie == '1':
        udostepnij_ekran_z_dziwekiem()
    elif dzialanie == '2':
        udostepnij_ekran_bez_dzwieku()
    elif dzialanie == '3':
        udostepnij_ekran_jako_wideoklip()
    elif dzialanie == '4':
        wycisz_wszystkich_bez_mozliwosci_odciszenia()
    elif dzialanie == '5':
        wycisz_wszystkich_z_mozliwoscia_odciszenia()
    elif dzialanie == '6':
        okej = False
