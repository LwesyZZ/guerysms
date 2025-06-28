from colorama import Fore, Style, Back
from time import sleep
from os import system
import urllib3
import time
import random

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from gueryf2f import SendSms

servisler_sms = []

for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

def banner(show_animation=True):
    if show_animation:
        system("cls||clear")
        text = "GUERYF2F"
        width = 56
        height = 16
        colors = [Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTBLUE_EX]
        for frame in range(height):
            system("cls||clear")
            for i in range(height):
                if i == frame:
                    color = random.choice(colors)
                    print(color + Style.BRIGHT + text.center(width) + Style.RESET_ALL)
                else:
                    print(" " * width)
            time.sleep(0.07)
        system("cls||clear")
    else:
        system("cls||clear")
        width = 56
    text = "GUERYF2F"
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + text.center(56) + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "╔" + "═"*(56-2) + "╗" + Style.RESET_ALL)
    box_text = "GUERYF2F SMS TESTER  |  Sorumluluk size aittir!"
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "║" + box_text.center(56-2) + "║" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "╚" + "═"*(56-2) + "╝" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + f"[!] Toplam SMS Servisi: " + Fore.LIGHTGREEN_EX + f"{len(servisler_sms)}" + Style.RESET_ALL)
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "{#} Yapımcı: GUERYF2F\n" + Style.RESET_ALL)

def menu_goster():
    print(Fore.LIGHTBLUE_EX + Style.BRIGHT + """
╭────────────────────────────────────────────────────────────╮
│                        ANA MENÜ                            │
├────────────────────────────────────────────────────────────┤
│  1  │  SMS Gönder                                          │
│  2  │  İletişim                                            │
│  3  │  Çıkış                                               │
╰────────────────────────────────────────────────────────────╯
""" + Style.RESET_ALL)

def iletisim_goster():
    print(Fore.LIGHTCYAN_EX + Style.BRIGHT + """
╭────────────────────────────────────────────────────────────╮
│                   İLETİŞİM BİLGİLERİ                       │
├────────────────────────────────────────────────────────────┤
""" + Style.RESET_ALL,
          Fore.LIGHTBLUE_EX + Style.BRIGHT + "│  Discord: gueryf2f".ljust(57) + "│" + Style.RESET_ALL,
          Fore.LIGHTRED_EX + Style.BRIGHT + "\n│  Youtube: https://www.youtube.com/@gueryf2f".ljust(57) + "│" + Style.RESET_ALL,
          Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n╰────────────────────────────────────────────────────────────╯" + Style.RESET_ALL,
          sep="")
    print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "Menüye dönmek için 'enter' tuşuna basınız.." + Style.RESET_ALL)
    input()

first_banner = True
while True:
    if first_banner:
        banner(show_animation=True)
        first_banner = False
    else:
        system("cls||clear")
    menu_goster()
    try:
        menu = int(input(Fore.LIGHTCYAN_EX + Style.BRIGHT + "Seçim: " + Style.RESET_ALL))
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + Back.LIGHTYELLOW_EX + Style.BRIGHT + "Hatalı giriş yaptınız. Tekrar deneyiniz." + Style.RESET_ALL)
        sleep(2)
        continue

    if menu == 1:
        system("cls||clear")
        tel_slots = ["[1] - (boş)", "[2] - (boş)", "[3] - (boş)", "[4] - (boş)", "[5] - (boş)"]
        tel_numbers = ["bos"] * 5
        while True:
            system("cls||clear")
            print(Fore.LIGHTBLUE_EX + Style.BRIGHT + """
╭────────────────────────────────────────────────────────────╮
│                TELEFON NUMARASI SLOTLARI                   │
├────────────────────────────────────────────────────────────┤""" + Style.RESET_ALL)
            for idx, slot in enumerate(tel_slots):
                slot_content = slot
                slot_line = f"│   {slot_content}{' ' * (46 - len(slot_content))}           │"
                if tel_numbers[idx] != "bos":
                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + slot_line + Style.RESET_ALL)
                else:
                    print(Fore.LIGHTBLACK_EX + slot_line + Style.RESET_ALL)
            print(Fore.LIGHTBLUE_EX + "╰────────────────────────────────────────────────────────────╯" + Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "\n[1-5]: Slot numarasına ekle  |  0: TXT'den yükle  |  ENTER: Devam" + Style.RESET_ALL)
            secim = input(Fore.LIGHTGREEN_EX + "Seçim: " + Style.RESET_ALL)
            if secim == "":
                break
            elif secim == "0":
                print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "TXT dosyasının yolunu giriniz: " + Fore.LIGHTGREEN_EX, end="")
                dosya_yolu = input()
                try:
                    with open(dosya_yolu, 'r') as file:
                        tel_list = file.readlines()
                        for i, number in enumerate(tel_list):
                            if i < 5:
                                num = number.strip()
                                if len(num) == 10 and num.isdigit():
                                    tel_numbers[i] = num
                                    tel_slots[i] = f"[{i+1}] - {num}"
                                else:
                                    raise ValueError
                        for j in range(i+1, 5):
                            tel_numbers[j] = "bos"
                            tel_slots[j] = f"[{j+1}] - (boş)"
                except Exception:
                    print(Fore.LIGHTRED_EX + Back.LIGHTCYAN_EX + Style.BRIGHT + "Dosya veya numara hatalı! Tekrar deneyin." + Style.RESET_ALL)
                    sleep(2)
                continue
            elif secim in [str(i+1) for i in range(5)]:
                idx = int(secim) - 1
                num = input(Fore.LIGHTCYAN_EX + f"Slot {secim} için 10 haneli numara: " + Fore.LIGHTGREEN_EX)
                if len(num) == 10 and num.isdigit():
                    tel_numbers[idx] = num
                    tel_slots[idx] = f"[{idx+1}] - {num}"
                else:
                    print(Fore.LIGHTRED_EX + Back.LIGHTCYAN_EX + Style.BRIGHT + "Numara hatalı!" + Style.RESET_ALL)
                    sleep(1)
                continue
            else:
                print(Fore.LIGHTRED_EX + Back.LIGHTCYAN_EX + Style.BRIGHT + "Geçersiz seçim!" + Style.RESET_ALL)
                sleep(1)
                continue
        tel_no, tel_no2, tel_no3, tel_no4, tel_no5 = tel_numbers
        try:
            print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "[+] " + Fore.CYAN + "Birden çok numara varsa her bir numara için.")
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT +
                  "\n• Kaç adet SMS göndermek istiyorsun? (Sonsuz için ENTER)" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "   (Her slot için ayrı ayrı gönderim yapılır.)" + Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "→ Adet: " + Style.RESET_ALL, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            print(Fore.LIGHTRED_EX + Back.LIGHTCYAN_EX + Style.BRIGHT + "Hatalı giriş! Lütfen geçerli bir sayı girin." + Style.RESET_ALL)
            sleep(2)
            continue
        try:
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT +
                  "\n• Kaç saniye arayla gönderilsin? (Örn: 2)" + Style.RESET_ALL)
            print(Fore.LIGHTBLACK_EX + "   (Her SMS arasında bekleme süresi.)" + Style.RESET_ALL)
            print(Fore.LIGHTCYAN_EX + Style.BRIGHT + "   0 yazarsanız en hızlı şekilde gönderilir." + Style.RESET_ALL)
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "→ Saniye: " + Style.RESET_ALL, end="")
            aralik = int(input())
        except ValueError:
            print(Fore.LIGHTRED_EX + Back.LIGHTCYAN_EX + Style.BRIGHT + "Hatalı giriş! Lütfen geçerli bir sayı girin." + Style.RESET_ALL)
            sleep(2)
            continue
        if kere is not None:
            tel_numbers = [tel_no, tel_no2, tel_no3, tel_no4, tel_no5]
            bos_olmayan = len([x for x in tel_numbers if x != "bos"])
            keree = kere * bos_olmayan
        sms = SendSms(tel_no, "")
        sms.adet = 0
        if isinstance(kere, int):
            while sms.adet < keree:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet >= keree:
                                break
                            exec("sms." + attribute + "()")
                            sleep(aralik)
            print(Fore.LIGHTCYAN_EX + Back.LIGHTGREEN_EX + Style.BRIGHT + "\nBelirtilen SMS adedine ulaşıldı! Ana menüye dönülüyor..." + Style.RESET_ALL)
            sleep(2)
            continue
        elif kere is None:
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms." + attribute + "()")
                            sleep(aralik)
        pass
    elif menu == 2:
        banner(show_animation=False)
        iletisim_goster()
    elif menu == 3:
        banner(show_animation=False)
        print(Fore.LIGHTRED_EX + Back.LIGHTWHITE_EX + Style.BRIGHT + "Çıkış yapılıyor..." + Style.RESET_ALL)
        break
