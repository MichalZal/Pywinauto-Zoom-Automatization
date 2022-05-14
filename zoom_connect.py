from pywinauto import Application
import time

def connect():
  ipsoktania = input("Podaj id sptokania (bez spacji): ")

  # Jeśli okno zoom jest włączone to proces z automatycznym łączeniem jest pomijany
  if ipsoktania != '':
      #==============================Automatyczne Połączenie z Zoomem===============================================================================
      imie = input("Podaj imie i nazwisko (ze spacjami): ")
      haslo = input("Podaj haslo (bez spacji): ")

      # łączy się z zoomem. Tutaj trzeba podać scieżkę do aplikacji zoom na naszym komputerze. 
      zoom_okno = Application(backend='uia').start(r"C:\Users\User\AppData\Roaming\Zoom\bin\Zoom.exe").connect(title="Zoom",timeout=10)
      #zoomWin.Zoom.print_control_identifiers()

      #zakładka dom
      homeTab = zoom_okno.Zoom.child_window(title='Dom', control_type="TabItem").wrapper_object()
      homeTab.click_input()

      #przycisk dołącz
      joinBtn = zoom_okno.Zoom.child_window(title='Dołącz', control_type="Button").wrapper_object()
      joinBtn.click_input()

      #Nowe okno = Dołącz do spotkania
      joinWindow = Application(backend='uia').connect(title='Dołącz do spotkania', timeout=10)

      #podawanie id spotkania
      poleID = joinWindow.Dołączdospotkania.child_window(title="Wprowadź identyfikator spotkania lub nazwę osobistego linku", control_type="Edit").wrapper_object()
      poleID.type_keys(ipsoktania)

      #wpisywanie imienia
      poleImie = joinWindow.Dołączdospotkania.child_window(title="Wprowadź nazwę", control_type="Edit").wrapper_object()
      poleImie.click_input()
      poleImie.type_keys("^a{BACKSPACE}")
      poleImie.type_keys(imie, with_spaces=True)

      #klikanie dołąćz
      przycisk_dołącz = joinWindow.Dołączdospotkania.child_window(title="Dołącz", control_type="Button")
      przycisk_dołącz.click_input()

      #Wporwadzanie hasła = Wporowadź kod spotkania
      codewindow = Application(backend='uia').connect(title="Wprowadź kod spotkania", timeout=10)
      #Codewindow.Wpiszkodspotkania.print_control_identifiers()
      kod = codewindow.Wprowadźkodspotkania.child_window(title="Wprowadź kod dostępu do spotkania", control_type="Edit")
      kod.click_input()
      kod.type_keys(haslo)
      dolacz_kod = codewindow.Wprowadźkodspotkania.child_window(title="Dołącz do spotkania", control_type="Button")
      dolacz_kod.click_input()

      time.sleep(30) #opóźnienie, żeby dołączanie poprawnie działało.
  else:
      print('ok')
      pass
