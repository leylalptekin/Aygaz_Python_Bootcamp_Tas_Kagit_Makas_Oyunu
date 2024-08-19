from tkinter import *
from PIL import Image, ImageTk
from random import randint
from tkinter import messagebox

def tas_kagit_makas_LEYLA_ALPTEKIN():
    # Oyun Tanıtımı ve Karşılama Mesajı
    def welcome_message():
        messagebox.showinfo("Hoş Geldiniz",
                            "Taş, Kağıt, Makas oyununa hoş geldiniz!\n\n"
                            "Kurallar:\n"
                            "1. Oyuncu taş, kağıt veya makas seçer.\n"
                            "2. Bilgisayar da rastgele bir seçim yapar.\n"
                            "3. Her turda kazanan belirlenir: Oyuncu kazanabilir, "
                            "bilgisayar kazanabilir veya beraberlik olabilir.\n"
                            "4. İlk iki turu kazanan oyunun galibi olur.\n\n"
                            "Oyunu başlatmak için Tamam'a tıklayın. :)\n"
                            "Çıkmak için pencereyi kapatabilirsiniz. :(")

    # Main penceresi
    root = Tk()
    root.title("Taş-Kağıt-Makas Oyunu")
    root.configure(background="#9b59b6")

    # Oyunun başında karşılama mesajı göster
    welcome_message()

    # Resimler
    rock_img = ImageTk.PhotoImage(Image.open("tas-user.png"))
    paper_img = ImageTk.PhotoImage(Image.open("kagit-user.png"))
    scissor_img = ImageTk.PhotoImage(Image.open("makas-user.png"))
    rock_img_comp = ImageTk.PhotoImage(Image.open("tas.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("kagit.png"))
    scissor_img_comp = ImageTk.PhotoImage(Image.open("makas.png"))

    # Resimleri yerleştir
    user_label = Label(root, image=scissor_img, bg="#9b59b6")
    comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
    comp_label.grid(row=1, column=0)
    user_label.grid(row=1, column=4)

    # Skorlar
    oyuncuSkor = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
    bilgisayarSkor = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
    bilgisayarSkor.grid(row=1, column=1)
    oyuncuSkor.grid(row=1, column=3)

    # Göstergeler
    user_indicator = Label(root, font=50, text="SİZ", bg="#9b59b6", fg="white")
    comp_indicator = Label(root, font=50, text="BİLGİSAYAR", bg="#9b59b6", fg="white")
    user_indicator.grid(row=0, column=3)
    comp_indicator.grid(row=0, column=1)

    # Mesajlar
    msg = Label(root, font=50, bg="#9b59b6", fg="white")
    msg.grid(row=3, column=2)

    # Tur kazançları için sayaçlar
    player_wins = 0
    computer_wins = 0

    # Mesaj güncelle
    def updateMessage(x):
        msg['text'] = x

    # Kullanıcı skorunu güncelle
    def updateUserScore():
        score = int(oyuncuSkor['text'])
        score += 1
        oyuncuSkor['text'] = str(score)

    # Bilgisayar skorunu güncelle
    def updateCompScore():
        score = int(bilgisayarSkor['text'])
        score += 1
        bilgisayarSkor['text'] = str(score)

    # Kazananı kontrol et
    def checkwin(player, computer):
        nonlocal player_wins, computer_wins

        if player == computer:
            updateMessage("Beraberlik!!!")
        elif player == "taş":
            if computer == "kağıt":
                updateMessage("Kaybettiniz :(")
                updateCompScore()
                computer_wins += 1
            else:
                updateMessage("Kazandınız ^_^")
                updateUserScore()
                player_wins += 1
        elif player == "kağıt":
            if computer == "makas":
                updateMessage("Kaybettiniz :(")
                updateCompScore()
                computer_wins += 1
            else:
                updateMessage("Kazandınız ^_^")
                updateUserScore()
                player_wins += 1
        elif player == "makas":
            if computer == "taş":
                updateMessage("Kaybettiniz :(")
                updateCompScore()
                computer_wins += 1
            else:
                updateMessage("Kazandınız ^_^")
                updateUserScore()
                player_wins += 1

        # İlk iki turu kazanan oyunu kazanır
        if player_wins == 2 or computer_wins == 2:
            if player_wins == 2:
                messagebox.showinfo("Oyun Bitti", "Tebrikler, oyunu kazandınız!")
            else:
                messagebox.showinfo("Oyun Bitti", "Maalesef, bilgisayar kazandı.")

            # Oyun bitince tekrar oynamak isteyip istemediğini sor
            replay = messagebox.askyesno("Oyun Bitti", "Tekrar oynamak ister misiniz?")
            if replay:
                # Sayaçları sıfırla ve skoru güncelle
                player_wins = 0
                computer_wins = 0
                oyuncuSkor['text'] = "0"
                bilgisayarSkor['text'] = "0"
                updateMessage("")
            else:
                root.quit()

    # Seçimleri güncelle
    choices = ("taş", "kağıt", "makas")

    def updateChoice(x):
        # Bilgisayar için
        compChoice = choices[randint(0, 2)]
        if compChoice == "taş":
            comp_label.configure(image=rock_img_comp)
        elif compChoice == "kağıt":
            comp_label.configure(image=paper_img_comp)
        else:
            comp_label.configure(image=scissor_img_comp)

        # Kullanıcı için
        if x == "taş":
            user_label.configure(image=rock_img)
        elif x == "kağıt":
            user_label.configure(image=paper_img)
        else:
            user_label.configure(image=scissor_img)

        checkwin(x, compChoice)

    # Butonlar
    Tas = Button(root, width=20, height=2, text="TAŞ", bg="#FF3E4D", fg="white",
                  command=lambda: updateChoice("taş"))
    Kagit = Button(root, width=20, height=2, text="KAĞIT", bg="#FAD02E", fg="white",
                   command=lambda: updateChoice("kağıt"))
    Makas = Button(root, width=20, height=2, text="MAKAS", bg="#0ABDE3", fg="white",
                     command=lambda: updateChoice("makas"))

    Tas.grid(row=2, column=1)
    Kagit.grid(row=2, column=2)
    Makas.grid(row=2, column=3)

    root.mainloop()

# Fonksiyonu çağırmak için
tas_kagit_makas_LEYLA_ALPTEKIN()
