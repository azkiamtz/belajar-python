import os
import datetime
from tkinter import *
from tkinter import messagebox
app = Tk()


nama = StringVar()
nama_layanan = StringVar()
bentuk = StringVar()
jk = StringVar()
lama_layanan = StringVar()
jenis_pelayanan = StringVar()
jenis_dokter = StringVar()
uang_bayar = StringVar()
tgl_check = StringVar()
bln_check = StringVar()
thn_check = StringVar()
jam_check = StringVar()



data_pasien = {}
data_pelayanan = {}


 

def tambahPasien():
    global nama,jk,bentuk
    index = 0 if len(data_pasien) == 0 else len(data_pasien)
    data_pasien[index] = {
        0 : nama.get(),
        1 : jk.get(),
        2 : bentuk.get()
    }
    messagebox.showinfo(message='Data Pasien Berhasil Ditambahkan')
    nama.set('')
    no=1
    row = 110
    for i in range(len(data_pasien)):
        kolom = 1000
        for j in range(3):
            Label(app, text=f"| {no:<2} | {data_pasien[i][0]:<8} | {data_pasien[i][1]:<8} | {data_pasien[i][2]:<6} |", bg='#31c6d4', foreground='#fef5ac', width=50,font='poppins 14 bold',padx=0).place(x=kolom,y=row)
            kolom = kolom+30
        row = row+30
        no=no+1

def selesaiPelayanan(total):
    global uang_bayar
    kembali = 0
    bayar = 0
    print(uang_bayar.get())
    if total > bayar:
        messagebox.showerror(message='Uang pembayaranmu kurang!')
        uang_bayar.set('')
    else:
        kembali = uang_bayar-total
        index = 0 if len(data_pelayanan) == 0 else len(data_pelayanan)
        datecheck = datetime.datetime(int(thn_check.get()),int(bln_check.get()),int(tgl_check.get()),int(jam_check.get())).strftime("%d-%m-%Y %H:00")
        print(datecheck)
        data_pelayanan[index] = {
            0:nama_layanan.get(),
            1:lama_layanan.get(),
            2:jenis_pelayanan.get(),
            3:jenis_dokter.get(),
            4:total,
            5:uang_bayar.get(),
            6:kembali,
            7:datecheck
        }
        messagebox.showinfo(message=f'Pelayanan berhasil diselesaikan, kembalian anda Rp {kembali}')
        nama_layanan.set('')
        uang_bayar.set('')
        lama_layanan.set('')
        tgl_check.set('')
        bln_check.set('')
        thn_check.set('')
        jam_check.set('')




def buatPelayanan():
    is_pasien = 0
    harga_pel = 0
    harga_lama = 0
    total = 0
    if len(data_pasien) > 0:
        for data in data_pasien:
            if data_pasien[data][0] == nama_layanan.get():
                is_pasien = 1
    if is_pasien == 1:
        if int(lama_layanan.get()) == 1:
            harga_lama = 100000
        elif int(lama_layanan.get()) == 2:
            harga_lama = 150000
        elif int(lama_layanan.get()) > 3 and int(lama_layanan.get() <= 6):
            harga_lama = 250000
        elif int(lama_layanan.get()) > 7:
            harga_lama = 600000

        if jenis_pelayanan.get() == "Rawat Jalan":
            harga_pel = 250000
        elif jenis_pelayanan.get() == "Rawat Inap":
            harga_pel = 500000
        elif jenis_pelayanan.get() == "Gawat Darurat":
            harga_pel = 750000
        elif jenis_pelayanan.get() == "Kanker Terpadu":
            harga_pel = 800000
        elif jenis_pelayanan.get() == "Kedokteran Nuklir":
            harga_pel = 900000
        elif jenis_pelayanan.get() == "Ibu dan Anak Terpadu":
            harga_pel = 600000
        elif jenis_pelayanan.get() == "Rawat Inap Intensif Terpadu":
            harga_pel = 1000000
        elif jenis_pelayanan.get() == "Bedah Sentral dan Anastesi":
            harga_pel = 2000000

        total = harga_lama+harga_pel

        Label(app, text=f"Total Harga Pelayanan : Rp {total}",padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=800)
        
        Label(app, text=f"Uang Bayar",padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=850)
        Entry(app, textvariable=uang_bayar,width=30).place(x=700,y=850)

        Button(app, text='Selesaikan Pelayanan', foreground='white', bg='#36ae7c', width=15, command=selesaiPelayanan(total)).place(x=770,y=900)
        
    else:
        messagebox.showerror(message='Data pasien tidak ditemukan')
        lama_layanan.set('')


app.title("Aplikasi Sistem Pelayanan Rumah Sakit")
        
app.geometry('1000x600') # membuat ukuran
app.configure(bg='#ffeaa7')
app.state('zoomed')

Label(app, text='SISTEM PELAYANAN RUMAH SAKIT',padx=15, bg='#31c6d4', foreground='#fef5ac', font='poppins 18 bold').place(x=450,y=30)

Label(app, text='Nama Pasien : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=100)
Entry(app, textvariable=nama,width=30).place(x=700,y=103)

Label(app, text='Jenis Kelamin : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=150)
jenkel = ['Laki-Laki','Perempuan']
jk.set(jenkel[0]) 
OptionMenu(app,jk,*jenkel).place(x=700,y=153)

Label(app, text='Bentuk Pelayanan : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=200)
pelayanan = ['BPJS','Non BPJS']
bentuk.set(pelayanan[0]) 
OptionMenu(app,bentuk,*pelayanan).place(x=700,y=200)

Button(app, text='Tambah Pasien', foreground='white', bg='#36ae7c', width=15, command=tambahPasien).place(x=770,y=250)

Label(app, text='DATA PASIEN',padx=15, bg='#31c6d4', foreground='#fef5ac', font='poppins 14 bold').place(x=1000,y=30)
Label(app, text=f"{'|':<6} {'No':<6} | {'Nama Pasien':<12} | {'Jenis Kelamin':<12} | {'Bentuk Pelayanan':<8} |", bg='#31c6d4', foreground='#fef5ac', font='poppins 14 bold',width=50).place(x=1000,y=80)

Label(app, text='PELAYANAN PASIEN',padx=15, bg='#31c6d4', foreground='#fef5ac', font='poppins 14 bold').place(x=470,y=300)

Label(app, text='Nama Pasien : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=350)
Entry(app, textvariable=nama_layanan,width=30).place(x=700,y=350)

Label(app, text='Lama Pelayanan : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=400)
Spinbox(app, textvariable=lama_layanan,width=30).place(x=700,y=400)

Label(app, text='Tanggal Checkup : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=450)
Entry(app, textvariable=tgl_check,width=30).place(x=700,y=450)

Label(app, text='Bulan Checkup : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=500)
Entry(app, textvariable=bln_check,width=30).place(x=700,y=500)

Label(app, text='Tahun Checkup : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=550)
Entry(app, textvariable=thn_check,width=30).place(x=700,y=550)

Label(app, text='Jam Checkup : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=600)
Entry(app, textvariable=jam_check,width=30).place(x=700,y=600)

Label(app, text='Jenis Pelayanan : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=650)
pelayanan = ['Rawat Jalan','Rawat Inap','Gawat Darurat','Kanker Terpadu','Kedokteran Nuklir','Ibu dan Anak Terpadu','Rawat Inap Intensif Terpadu','Bedah Sentral dan Anestesi']
jenis_pelayanan.set(pelayanan[0]) 
OptionMenu(app,jenis_pelayanan,*pelayanan).place(x=700,y=650)
Label(app, text='Nama Dokter : ',padx=10,bg='#ffeaa7', foreground='#000000', font='poppins 12 bold').place(x=470,y=700)
dokter = ['dr. Alberto','dr. Alexa','dr. Brain','dr. Adelwis','dr. Bonerto','dr. Glenn','dr. Dilan','dr. Brillian','dr. Kawisha']
jenis_dokter.set(dokter[0]) 
OptionMenu(app,jenis_dokter,*dokter).place(x=700,y=700)

Button(app, text='Buat Pelayanan', foreground='white', bg='#36ae7c', width=15, command=buatPelayanan).place(x=770,y=750)



app.mainloop()