from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Toko Buku')

# variabel
buku_1 = StringVar()
buku_2 = StringVar()
buku_3 = StringVar()
buku_4 = StringVar()
buku_5 = StringVar()
buku_6 = StringVar()
buku_7 = StringVar()
buku_8 = StringVar()
buku_9 = StringVar()
buku_10 = StringVar()
tekstotal = StringVar()
teksaung = StringVar()
total = 0

# buat function
def totalbeli():
    global buku_1,buku_2,buku_3,buku_4,buku_5,buku_6,buku_7,buku_8,buku_9,buku_10, tekstotal, total
    hbuku_1 = int(buku_1.get()) * 75000
    hbuku_2 = int(buku_2.get()) * 95000
    hbuku_3 = int(buku_3.get()) * 172500
    hbuku_4 = int(buku_4.get()) * 45000
    hbuku_5 = int(buku_5.get()) * 200000
    hbuku_6 = int(buku_6.get()) * 76000
    hbuku_7 = int(buku_7.get()) * 23000
    hbuku_8 = int(buku_8.get()) * 97300
    hbuku_9 = int(buku_9.get()) * 99000
    hbuku_10 = int(buku_10.get()) * 125000
    total = hbuku_1 + hbuku_2 + hbuku_3 + hbuku_4 + hbuku_5 + hbuku_6 + hbuku_7 + hbuku_8 + hbuku_9 + hbuku_10
    tekstotal.set(str(total))

def kembalian():
    global total
    uang = int(teksaung.get())

    if uang >= total:
        kembalian = uang - total
        messagebox.showinfo(message='Kembalian kamu sebesar {}'.format(str(kembalian)))
    else:
        messagebox.showerror(message='maaf uang kamu kurang')

def clear():
        buku_1.set('0')
        buku_2.set('0')
        buku_3.set('0')
        buku_4.set('0')
        buku_5.set('0')
        buku_6.set('0')
        buku_7.set('0')
        buku_8.set('0')
        buku_9.set('0')
        buku_10.set('0')
        tekstotal.set('0')
        teksaung.set('0')


app.geometry('1000x600') # membuat ukuran
app.configure(bg='#ffeaa7') # membuat backgroung warna

# membuat properti tulisan title
Label(app, text='KASIR TOKO BUKU',padx=15, bg='#31c6d4', foreground='#fef5ac', font='poppins 18 bold').place(x=200,y=30)

# membuat label nama menu
Label(app, text='1. Si Kancil', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=100)
Label(app, text='2. Bawang Merah Bawang Putih', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=140)
Label(app, text='3. Think Out of The Box', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=180)
Label(app, text='4. Marmut Merah Jambu', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=220)
Label(app, text='5. Ketika Cinta Bertasbih', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=260)
Label(app, text='6. Rudy Habibie', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=300)
Label(app, text='7. Strategi Bisnis', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=340)
Label(app, text='8. 5 CM', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=380)
Label(app, text='9. Kupinang Kau dengan Bismillah', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=420)
Label(app, text='10. Laskar Pelangi', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=100,y=460)

# membuat label harga
Label(app, text='Rp. 75000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=100)
Label(app, text='Rp. 95000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=140)
Label(app, text='Rp. 172500', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=180)
Label(app, text='Rp. 45000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=220)
Label(app, text='Rp. 200000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=260)
Label(app, text='Rp. 76000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=300)
Label(app, text='Rp. 23000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=340)
Label(app, text='Rp. 97300', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=380)
Label(app, text='Rp. 99000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=420)
Label(app, text='Rp. 125000', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=400,y=460)

# membuat spinbox
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_1, command=totalbeli).place(x=500,y=100)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_2, command=totalbeli).place(x=500,y=140)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_3, command=totalbeli).place(x=500,y=180)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_4, command=totalbeli).place(x=500,y=220)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_5, command=totalbeli).place(x=500,y=260)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_6, command=totalbeli).place(x=500,y=300)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_7, command=totalbeli).place(x=500,y=340)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_8, command=totalbeli).place(x=500,y=380)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_9, command=totalbeli).place(x=500,y=420)
Spinbox(app, from_=0, to=100, width=6, font='poppins 10', textvariable=buku_10, command=totalbeli).place(x=500,y=460)

# membuat label pembayaran
Label(app, text='Masukan uang anda', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=600,y=280)

# membuat entry jumlah uang
Entry(app, textvariable=teksaung).place(x=600,y=320)

# membuat label total
Label(app, text='Rp. ', bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=800,y=300)
Label(app, textvariable=tekstotal, bg='#31c6d4', foreground='#fef5ac', font='poppins 12 bold').place(x=850,y=300)

# membuat tombol
Button(app, text='Total', foreground='white', bg='#36ae7c', width=10, command=kembalian).place(x=600,y=400)
Button(app, text='Clear', foreground='white', bg='#ff1e1e', width=10, command=clear).place(x=690,y=400)

# footer text
Label(app, text='Created by M Azkia Hakim.', bg='#31c6d4', foreground='#fef5ac', font='poppins 10 ').place(x=300,y=550)

app.mainloop() # menampilkan aplikasi