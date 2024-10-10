import os
from datetime import datetime
import datetime
import time

dataTransaksi = {
    "MaxID" : 1,
    "data" : {},        
}

def menu():
    print("\t\tMenu Aplikasi")
    print("1. Penyewaan Lapangan")
    print("2. Batalkan Penyewaan")
    print("3. Riwayat Penyewaan")
    print("4. Cek Ketersediaan")
    print("5. Keluar Program")
    print("="*50)
def intro():
    print("="*50)
    print("||\tSistem Booking Lapangan Badminton\t||")
    print("||\t\tMaspen Sport Center\t\t||")
    print("="*50)
    print("1. Ananda Akhiratri - 411221110")
    print("2. M Azkia Hakim - 411221125")
    print("3. Rifda Mumtaz Audami - 411221129")
    print("4. Anisa Febiani - 411221134")
    print("="*50)
    print("Copyright by Kelompok 2 - 2023")
    print("Bias Yulisa Geni, S.Kom., M.Kom.")
    print("Algoritma dan Pemograman 2")
    print("="*50)
def alert(mess):
    print("="*50)
    print(f"||\t\t{mess}\t\t||")
    print("="*50)
def clear():
    os.system('cls')

def sewaLapangan():
    listData = []
    listHourBooked = []
    is_booked = 0
    sewaLagi = True
    while sewaLagi == True:
        clear()
        print("="*50)
        print("||\tSelamat Datang di Menu Sewa Lapangan\t||")
        print("="*50)
        listHour = []
        cekTanggal,cekBulan,cekTahun,cekJam,cekLama,cekNoLapangan = True,True,True,True,True,True

        MaxID = dataTransaksi['MaxID']
        nama = input("Masukan Nama Penyewa \t\t: ") 
        no_hp = input("Masukan No HP Penyewa \t\t: ") 
        while cekTanggal == True:
            tanggal_sewa = int(input("Masukan Tanggal Sewa \t\t: "))
            if tanggal_sewa > 31:
                 print("Tanggal tidak valid.")
            else:
                cekTanggal = False
        while cekBulan == True:
            bulan_sewa = int(input("Masukan Bulan Sewa [1-12] \t: ")) 
            if bulan_sewa > 12:
                print("Bulan tidak valid.")
            else:
                cekBulan = False
        while cekTahun == True:
            tahun_sewa = int(input("Masukan Tahun Sewa \t\t: "))
            if len(str(tahun_sewa)) != 4:
                print("Tahun tidak valid.")
            else:
                cekTahun = False
        while cekJam == True:
            jam_mulai = int(input("Masukan Jam Mulai [1-24] \t: "))
            if jam_mulai > 24:
                print("Jam mulai tidak valid.")
            else:
                cekJam = False
        while cekLama == True:
            lama_sewa = int(input("Masukan Lama Sewa \t\t: "))
            if lama_sewa > 24:
                print("Lama sewa tidak boleh lebih dari 24 jam.")
            else:
                cekLama = False
        while cekNoLapangan == True:
            no_lapangan = int(input("Masukan No Lapangan \t\t: "))
            if no_lapangan > 5:
                print("Lapangan hanya tersedia sampai 5.")
            else:
                cekNoLapangan = False

        datesewa = datetime.datetime(tahun_sewa,bulan_sewa,tanggal_sewa).strftime("%d-%m-%Y")
        listData = [nama,no_hp,datesewa,jam_mulai,lama_sewa, "OnGoing", no_lapangan]
        listHour.append(jam_mulai)
        for key in range(lama_sewa-1):
            listJam = jam_mulai+(key+1)
            listHour.append(listJam)
        if dataTransaksi['data']:    
            for key in dataTransaksi['data']:
                if dataTransaksi['data'][key][2] == datesewa and dataTransaksi['data'][key][5] == "OnGoing" and dataTransaksi['data'][key][6] == no_lapangan:
                    listHourBooked.append(dataTransaksi['data'][key][3])
                    for x in range(dataTransaksi['data'][key][4]-1):
                        listJam = dataTransaksi['data'][key][3]+(x+1)
                        listHourBooked.append(listJam)
            for value in listHour:
                if value in listHourBooked:
                    is_booked = 1
        if is_booked == 0:
            dataTransaksi['data'][MaxID] = listData
            dataTransaksi['MaxID'] = dataTransaksi['MaxID']+1
            print("Penyewaan berhasil dilakukan, Terimakasih")
            backMenu = input("Kembali ke Menu? [Y/N] : ")
            print("="*50)
            if backMenu == "y" or backMenu == "Y":
                sewaLagi = False 
        else:
            print("Lapangan telah digunakan")
            backMenu = input("Kembali ke Menu? [Y/N] : ")
            print("="*50)
            if backMenu == "y" or backMenu == "Y":
                sewaLagi = False

def batalSewa():
    batalLagi = True
    while batalLagi == True:
        clear()
        print("="*151)
        print("||"," "*60,"Pembatalan Sewa Lapangan"," "*59,"||")
        print("="*151)
        cekStatusOngoing = 0
        print("="*151)
        print(f"{'||':<4} {'Id Transaksi':<14} {'||':<8} {'Nama':<11} {'||':<8} {'No HP':<10} {'||':<8} {'Tanggal':<12} {'||':<6} {'Jam':<8} {'||':<8} {'Lama Sewa':<15} {'||':<8} {'No Lapangan':<15} {'||':<8}")
        print("="*151)
        if dataTransaksi['data']:    
            for key in dataTransaksi['data']:
                if dataTransaksi['data'][key][5] == "OnGoing":
                    cekStatusOngoing = cekStatusOngoing+1
            if cekStatusOngoing > 0 :
                for key in dataTransaksi['data']:
                    if dataTransaksi['data'][key][5] == "OnGoing":
                        mulai = f"0{dataTransaksi['data'][key][3]}:00" if len(str({dataTransaksi['data'][key][3]})) == 1 else f"{dataTransaksi['data'][key][3]}:00"
                        print(f"{'||':<8} {key:<10} {'||':<8} {dataTransaksi['data'][key][0]:<11} {'||':<6} {dataTransaksi['data'][key][1]:<8} {'||':<7} {dataTransaksi['data'][key][2]:<13} {'||':<6} {mulai:<8} {'||':<9} {dataTransaksi['data'][key][4]} {'Jam':<12} {'||':<8} Lapangan {dataTransaksi['data'][key][6]:<6} {'||':<8}")
            else:
                print("||"," "*60,"Daftar Penyewaan Kosong"," "*60,"||")
        else:
            print("||"," "*60,"Daftar Penyewaan Kosong"," "*60,"||")
        print("="*151)
        if dataTransaksi['data'] and cekStatusOngoing > 0:
            cekID = True
            while cekID == True:
                id_transaksi = int(input("Masukan ID Transaksi : "))
                if id_transaksi in dataTransaksi['data']:
                    cekID = False
                else:
                    print("ID Transaksi tidak ditemukan")
            confirm = input("Anda yakin ingin membatalkan? [Y/N] : ")
            if confirm == "y" or confirm == "Y":
                dataTransaksi['data'][id_transaksi][5] = "Canceled"
                print("Pembatalan berhasil dilakukan")
            else:
                print("Pembatalan berhasil digagalkan")

        backMenu = input("Kembali ke Menu? [Y/N] : ")
        if backMenu == "y" or backMenu == "Y":
                batalLagi = False 

def riwayatSewa():
    riwayatLagi = True
    nowDate = datetime.datetime.now()
    dt_now = nowDate.strftime("%d-%m-%Y %H:%M:%S")
    while riwayatLagi == True:
        clear()
        print("="*160)
        print("||"," "*67,"Riwayat Sewa Lapangan"," "*64,"||")
        print("="*160)
        cekStatusOngoing = 0
        print("="*160)
        print(f"{'||':<4} {'Id':<4} {'||':<8} {'Nama':<11} {'||':<8} {'No HP':<10} {'||':<8} {'Tanggal':<12} {'||':<6} {'Jam':<8} {'||':<8} {'Lama Sewa':<15} {'||':<8} {'No Lapangan':<16} {'||':<6} {'Status':<10} ||")
        print("="*160)
        if dataTransaksi['data']:    
            for key in dataTransaksi['data']:
                mulai = f"0{dataTransaksi['data'][key][3]}:00" if len(str({dataTransaksi['data'][key][3]})) == 1 else f"{dataTransaksi['data'][key][3]}:00"
                dt = dataTransaksi['data'][key][2]+ " " +mulai+":00"
                dt_sewa = datetime.datetime.strptime(dt, "%d-%m-%Y %H:%M:%S")
                if datetime.datetime.strptime(dt_now, "%d-%m-%Y %H:%M:%S") > dt_sewa:
                    dataTransaksi['data'][key][5] = "Finished"
                print(f"{'||':<4} {key:<4} {'||':<8} {dataTransaksi['data'][key][0]:<11} {'||':<6} {dataTransaksi['data'][key][1]:<8} {'||':<7} {dataTransaksi['data'][key][2]:<13} {'||':<6} {mulai:<8} {'||':<9} {dataTransaksi['data'][key][4]} {'Jam':<12} {'||':<8} Lapangan {dataTransaksi['data'][key][6]:<7} {'||':<6} {dataTransaksi['data'][key][5]:<10} ||")
        else:
            print("||"," "*66,"Daftar Penyewaan Kosong"," "*63,"||")
        print("="*160)
        backMenu = input("Kembali ke Menu? [Y/N] : ")
        if backMenu == "y" or backMenu == "Y":
                riwayatLagi = False

def cekLapangan():
    cekLagi = True
    while cekLagi == True :
        bookedLapangan1 = []
        bookedLapangan2 = []
        bookedLapangan3 = []
        bookedLapangan4 = []
        bookedLapangan5 = []
        clear()
        print("="*112)
        print("||"," "*43,"Cek Ketersediaan Lapangan"," "*36,"||")
        print("="*112)
        cekTanggal,cekBulan,cekTahun = True,True,True
        while cekTanggal == True:
            tanggal_sewa = int(input("Masukan Tanggal Sewa \t\t: "))
            if tanggal_sewa > 31:
                 print("Tanggal tidak valid.")
            else:
                cekTanggal = False
        while cekBulan == True:
            bulan_sewa = int(input("Masukan Bulan Sewa [1-12] \t: ")) 
            if bulan_sewa > 12:
                print("Bulan tidak valid.")
            else:
                cekBulan = False
        while cekTahun == True:
            tahun_sewa = int(input("Masukan Tahun Sewa \t\t: "))
            if len(str(tahun_sewa)) != 4:
                print("Tahun tidak valid.")
            else:
                cekTahun = False
        # dt_sewa = ("0"+str(tanggal_sewa) if len(str(tanggal_sewa)) == 1 else str(tanggal_sewa))+"-"+str(bulan_sewa)+"-"+str(tahun_sewa)
        dt_sewa = datetime.datetime(tahun_sewa,bulan_sewa,tanggal_sewa).strftime("%d-%m-%Y")
        print("="*112)
        print("||"," "*45,f"Tanggal : {dt_sewa}"," "*39,"||")
        print("="*112)
        print(f"{'||':<6} {'Jam':<7} {'||':<5} {'Lapangan 1':<12} {'||':<5} {'Lapangan 2':<12} {'||':<5} {'Lapangan 3':<12} {'||':<5} {'Lapangan 4':<12} {'||':<5} {'Lapangan 5':<12} ||")
        print("="*112)
        if dataTransaksi['data']:    
            for key in dataTransaksi['data']:
                if dataTransaksi['data'][key][2] == dt_sewa and dataTransaksi['data'][key][5] == "OnGoing":
                        if dataTransaksi['data'][key][6] == 1:
                            bookedLapangan1.append(dataTransaksi['data'][key][3])
                            for x in range(dataTransaksi['data'][key][4]-1):
                                listJam = dataTransaksi['data'][key][3]+(x+1)
                                bookedLapangan1.append(listJam)
                        elif dataTransaksi['data'][key][6] == 2:
                            bookedLapangan2.append(dataTransaksi['data'][key][3])
                            for x in range(dataTransaksi['data'][key][4]-1):
                                listJam = dataTransaksi['data'][key][3]+(x+1)
                                bookedLapangan2.append(listJam)
                        elif dataTransaksi['data'][key][6] == 3:
                            bookedLapangan3.append(dataTransaksi['data'][key][3])
                            for x in range(dataTransaksi['data'][key][4]-1):
                                listJam = dataTransaksi['data'][key][3]+(x+1)
                                bookedLapangan3.append(listJam)
                        elif dataTransaksi['data'][key][6] == 4:
                            bookedLapangan4.append(dataTransaksi['data'][key][3])
                            for x in range(dataTransaksi['data'][key][4]-1):
                                listJam = dataTransaksi['data'][key][3]+(x+1)
                                bookedLapangan4.append(listJam)
                        elif dataTransaksi['data'][key][6] == 5:
                            bookedLapangan5.append(dataTransaksi['data'][key][3])
                            for x in range(dataTransaksi['data'][key][4]-1):
                                listJam = dataTransaksi['data'][key][3]+(x+1)
                                bookedLapangan5.append(listJam)
            for i in range(24):
                jam = i+1
                str_jam = "0"+str(jam)+":00" if len(str(jam)) == 1 else str(jam)+":00"
                cekLap1 = "Tersedia" if jam not in bookedLapangan1 else "Digunakan"
                cekLap2 = "Tersedia" if jam not in bookedLapangan2 else "Digunakan"
                cekLap3 = "Tersedia" if jam not in bookedLapangan3 else "Digunakan"
                cekLap4 = "Tersedia" if jam not in bookedLapangan4 else "Digunakan"
                cekLap5 = "Tersedia" if jam not in bookedLapangan5 else "Digunakan"
                print(f"{'||':<5} {str_jam:<8} {'||':<6} {cekLap1:<11} {'||':<6} {cekLap2:<11} {'||':<6} {cekLap3:<11} {'||':<6} {cekLap4:<11} {'||':<6} {cekLap5:<11} ||")  
        else:
            for i in range(24):
                jam = i+1
                str_jam = "0"+str(jam)+":00" if len(str(jam)) == 1 else str(jam)+":00"
                cekLap1 = "Tersedia" if jam not in bookedLapangan1 else "Digunakan"
                cekLap2 = "Tersedia" if jam not in bookedLapangan2 else "Digunakan"
                cekLap3 = "Tersedia" if jam not in bookedLapangan3 else "Digunakan"
                cekLap4 = "Tersedia" if jam not in bookedLapangan4 else "Digunakan"
                cekLap5 = "Tersedia" if jam not in bookedLapangan5 else "Digunakan"
                print(f"{'||':<5} {str_jam:<8} {'||':<6} {'Tersedia':<11} {'||':<6} {'Tersedia':<11} {'||':<6} {'Tersedia':<11} {'||':<6} {'Tersedia':<11} {'||':<6} {'Tersedia':<11} ||") 
        print("="*112)
        backMenu = input("Kembali ke Menu? [Y/N] : ")
        if backMenu == "y" or backMenu == "Y":
                cekLagi = False

intro()
while True:
    menu()
    pil_menu = input("Pilih Menu [1/2/3/4/5] : ")
    if pil_menu == "1":
        clear()
        sewaLapangan()
        clear()
        intro()
    elif pil_menu == "2":
        clear()
        batalSewa()
        clear()
        intro()
    elif pil_menu == "3":
        clear()
        riwayatSewa()
        clear()
        intro()
    elif pil_menu == "4":
        clear()
        cekLapangan()
        clear()
        intro()
    elif pil_menu == "5":
        exit()
    else:
        alert("Menu Tidak Ditemukan!")


