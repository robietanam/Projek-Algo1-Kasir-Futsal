from io import BufferedIOBase
import json
import os
import datetime

tanggal_trans = str(datetime.date.today())
harga_lap = 80000
#-------------------------------------File Handling--------------------------------------------------------------#


# Fungsi untuk mengambil data dari file json dalam suatu folder
def loadData(PATH,folder):
    file = os.listdir(folder)
    if PATH in file:
        with open( folder + "/"+ PATH) as database:
            tmp = json.load(database)
    else:
        tmp = []
    return tmp
# Fungsi untuk menyimpan data ke file json ke suatu folder
def simpanData(PATH,data,folder):
    with open( folder + "/"+ PATH,'w+') as database:
        json_object = json.dumps(data, indent = 2)
        database.write(json_object)

#--------------------------------------------Menu Awal--------------------------------------------------------------------#


# Menu awal 
def welcome():
    os.system('cls')
    
    while True :
        print('-----------------------------------------')
        print("Selamat Datang Di Aplikasi Futsal MarBit")
        print('-----------------------------------------')
        print('Silahkan pilih menu dibawah')
        menu_login = input(" 1.Login 2.Edit Profile Admin 3.Exit : ")
        if menu_login == "1":
            login()
        elif menu_login == "2":
            profile()
        elif menu_login == '3':
            exit()
        else : 
            print("Silahkan pilih menu diatas")


# Fungsi login 
def login():
    os.system('cls')
    datauser = loadData('user.json',folder='data')
    print('-----------------------------------------')
    print("--------------Login Admin----------------")
    print('-----------------------------------------')
    username = input("Silahkan masukkan username anda : ")
    pwd = input("Silahkan masukkan password anda : ")
    os.system('cls')
    

    if not datauser == [] :
        for user in datauser :
            
            # ' '.join(str.split()) Menghapus kelebihan space di tengah , awal dan akhir input
            if ' '.join(username.lower().split()) == user['username'] :
                if ' '.join(pwd.lower().split()) == user['password'] :
                    menu_utama(username)
                else : 
                    print("Password salah")
    else:
        print('Silahkan membuat akun terlebih dahulu')


# Profile
def profile():
    os.system('cls')
    # Mengload data user.json pada folder data
    datauser = loadData('user.json',folder='data')
    print('---------------------------------')
    print('--------Menu Edit Profile--------')
    print('---------------------------------')
    # strip untuk menghilangkan white space di awal dan akhir 
    username = input('Masukkan username : ').strip()
    pwd = input("Masukkan password : ").strip()

    # Mencari data user
    for user in datauser :
        if username == user['username'] :
            if pwd == user['password'] :
                os.system('cls')
                # Edit profile pengguna
                
                while True:
                    print('---------------------------------')
                    print('-----------Edit Profile----------')
                    print('---------------------------------')
                    print('1.Edit nama 2.Edit pass 3.Simpan 4.Keluar')
                    choice = input('Masukkan pilihan : ')
                    if choice == '1':
                        username = input("Masukkan nama baru : ")
                        input('Username berhasil diubah Enter untuk melanjutkan')
                        os.system('cls')
                    elif choice == '2':
                        pwd = input('Masukkan pass baru : ')
                        input('Password berhasil diubah Enter untuk melanjutkan')
                        os.system('cls')
                    elif choice == '3' :
                        # Mengupdate isi file json user.json
                        user['username'] = username
                        user['password'] = pwd
                        input('Data tersimpan Enter untuk melanjutkan')
                        os.system('cls')
                        # Menyimpan data pada datauser ke file user.json pada folder data
                        simpanData(PATH='user.json' ,data = datauser,folder='data')
                    elif choice == '4' :
                        break  
            else: 
                print('Username atau password salah')
                break
        else:
            print('Username salah')
            break
    os.system('cls')      


def tambahData():
    os.system('cls')
    data_pelanggan = loadData('pelanggan.json',folder='data')
    print('---------------------------------')
    print('------Daftar Pelanggan Baru------')
    print('---------------------------------')
    nama_lengkap = input('Masukkan nama lengkap : ')
    while True:
        username = input('Masukkan panggilan/inisial : ')
        for pelanggan in data_pelanggan:
            if pelanggan['panggilan'] == username:
                os.system('cls')
                print('Inisial sudah ada')
                continue
        break
    # append = menambah data baru pada list disini listnya dalah data_pelanggan yg berisi isi file json pelanggan.json
    data_pelanggan.append({'nama':nama_lengkap,'panggilan':username,'tipe':'reguler','jumlah_pemesanan':0})
    simpanData('pelanggan.json',folder='data',data=data_pelanggan)
    input('Data sudah tersimpan Enter untuk melanjutkan')
    os.system('cls')

# Mengubah format integer ke dalam bentuk rupiah
def rupiah(rupiah):
    rupiah = int(rupiah)
    # Mengubah nilai misal 20000 menjadi  RP. 20,000.00
    rupiah = "RP. {:,.2f}".format(rupiah)
    # Mengembalikan nilai ke fungsi rupiah bila dipanggil
    return rupiah


def menu_utama(username):
    os.system('cls')

    while True:
        os.system('cls')
        print('---------------------------------')
        print('Selamat datang Admin,',username)
        print('---------------------------------')
        print('1. Tambah Jadwal 2. Lihat Jadwal 3. Edit Data 4. Lihat Data Pemasukkan 5.Exit')
        pilih = input('Silahkan pilih menu diatas : ')

        if pilih == "1":
            tanggal = int(input("Silahkan masukkan tanggal : "))
            bulan = int(input("Silahkan masukkan bulan : "))
            pesan_lapangan(tanggal,bulan)

        elif pilih == "2":
            tanggal = int(input("Silahkan masukkan tanggal : "))
            bulan = int(input("Silahkan masukkan bulan : "))
            lihat_lapangan(tanggal,bulan)

        elif pilih == "3":
            edit_data()     

        elif pilih == '4':
            lihat_pemasukan()

        else :
            break


def beli_member(username):
    os.system('cls')

    datauser = loadData('pelanggan.json',folder='data')
    trans = loadData(f'{tanggal_trans}.json',folder='data/transaksi')
    print('---------------------------------')
    print('----------Beli Member------------')
    print('---------------------------------')
    print('Harga member 50.000')
    bayar = ''.join(input('masukkan uang : ').split())
    kembalian = int(bayar) - 50000
    print('Kembalian : ',kembalian)
    if kembalian <= 0 :
        print('Uang kurang')
    else:
        for user in datauser:
            if user['panggilan'] == username:
                user['tipe'] = 'member'
                nama = user['nama']

        trans.append({'nama':nama,'panggilan':username,'order':tanggal_trans,'total_bayar':50000,'tipe': user['tipe'],'transaksi':'beli_member'})
    
    simpanData(f'{tanggal_trans}.json',folder='data/transaksi',data=trans)   
    simpanData('pelanggan.json',folder='data',data=datauser)  


def edit_data():
    os.system('cls')
    datauser = loadData('pelanggan.json',folder='data')
    print('---------------------------------')
    print('---------Menu Edit Data----------')
    print('---------------------------------')
    print('1.Edit data pelanggan 2.Hapus data transaksi 3.Exit')
    pilih = input('Pilih menu diatas : ')
    if pilih == '1':
        os.system('cls')
        print('---------------------------------')
        print('-------Edit Data Pelanggan-------')
        print('---------------------------------')
        username = input('Masukkan user yg ingin diedit : ').strip()
        # Mengiterasi data json dalam datauser
        datauser = loadData('pelanggan.json',folder='data')
        for user in datauser:
            # Check bila isi dari kunci panggilan sama dengan username
            if user['panggilan'] == username:
                while True:
                    os.system('cls')
                    print('---------------------------------')
                    print('-------Edit Data Pelanggan-------')
                    print('---------------------------------')
                    print('1.) Username     : ',user['panggilan'])
                    print('2.) Nama lengkap : ',user['nama'])
                    print('3.) Status       : ',user['tipe'])
                    print('4.) Simpan')
                    print('5.) Hapus user')
                    print('6.) Exit')
                    while True:
                        pilih = input('Pilih no data yang ingin diedit : ')
                        if pilih.isnumeric():
                            break
                        else:
                            print('Masukkan data dengan benar')
                            continue
                    if pilih == '1':
                        username = input('Masukkan username baru :')
                        user['panggilan'] = username
                        input('Inisial berhasil dirubah')
                    elif pilih == '2':
                        nama = input('Masukkan nama baru :')
                        user['nama'] = nama
                        input('Nama berhasil dirubah')
                    elif pilih == '3':
                        print('Status saat ini :',user['tipe'])
                        print('1.Reguler 2.Member')
                        tipe = input('Pilih tipe : ')
                        if tipe == '1':
                            user['tipe'] = 'reguler'
                        elif tipe == '2':
                            beli_member(user['panggilan'])
                            user['tipe'] = 'member'
                    elif pilih == '4':
                        simpanData('pelanggan.json',folder='data',data=datauser)
                        input('Perubahan berhasil disimpan')
                    elif pilih == '5':
                        datauser.remove(user)
                        simpanData('pelanggan.json',folder='data',data=datauser)
                        input('Perubahan berhasil disimpan')
                        break
                    else:
                        break
                break
    elif pilih == '2':
        os.system('cls')
        print('---------------------------------')
        print('------Hapus Data Transaksi-------')
        print('---------------------------------')
        tanggal = int(input('Masukkan tanggal : '))
        bulan = int(input('Masukkan bulan : '))
        tahun = int(input('Masukkan tahun : '))
        data = loadData("%s-%.2d-%.2d.json"%(tahun,int(bulan),int(tanggal)),folder='data/transaksi')
        while True:
            
            j = 0
            print('---------------------------------')
            print('------Hapus Data Transaksi-------')
            print('---------------------------------')
            print(f'Transaksi pada tanggal : {tanggal}-{bulan}-{tahun}')
            for i in data:
                j += 1
                print(f'{j} .)')
                print('Nama Lengkap : ',i['nama'])
                print('Username     : ',i['panggilan'])
                print('Transaksi    : ',i['total_bayar'])
                print('Tipe         : ',i['tipe'])
                
                if 'transaksi' in i.keys():
                    print('Transaksi    : ',i['transaksi'])
                else :
                    print('Transaksi    : ' + 'Pemesanan Futsal')
            if data == None:
                print("Tidak ada data")
                break
            while True:
                pilih = input('Pilih index yang ingin dihapus : ')
                if pilih.isnumeric():
                    break
            data.pop(int(pilih)-1)
            milih = input('hapus lagi(y/n) : ')
            if milih == 'n':
                break
        memilih = input('Simpan data?(y/n) : ')
        if memilih == 'y':
            simpanData("%s-%.2d-%.2d.json"%(tahun,int(bulan),int(tanggal)),folder='data/transaksi',data=data)
    else:
        pass


# Fungsi tambahan untuk check jadwal
def check_jadwal(i,jadwal):
    tmp = '-'
    # jadwal adalah waktu yang sudah penuh terisi
    # jadwal berisi list dictionary ,dimana dalam satu dictionary terdapat nama , pukul pesan
    for j in jadwal:
        # contoh isi j = {'nama': nama,'pukul':10}
        # check bila isi dari salah satu dict pada value dari kunci pukul sama dengan pukul pada var i
        if j['pukul'] == i:
            # jika sama akan mengubah var tmp menjadi nama user pada dict j 
            tmp = j['nama']
            break
        else:
            # jika nama tidak sama var tmp akan tetap sama '-'
            tmp = '-'
    # Mengembalikan nilai tmp saat fungsi dipanggil
    return tmp


def lihat_lapangan(tanggal,bulan):
    # Load data pada file sesuai dengan input tanggal dan bulan
    jadwals = loadData("%.2d-%.2d-2021.json"%(bulan,tanggal), folder="data/jadwal_penuh")
    os.system('cls')
    print('Tanggal : %.2d-%.2d-2021'%(tanggal,bulan))
    print("| %-11s | %-8s | %-8s | %-8s | %-8s | "%('Pukul','WB','CB','BP','SM'))
   
    # WB,CB,BP,SM berisi jam yang sudah dibooking pada data jadwals
    WB = []
    CB = []
    BP = []
    SM = []
    for jadwal in jadwals:

        # Check jika value kunci lapangan pada dict jadwal sama dengan windah basaudata
        if jadwal['lapangan'] == "Windah Basaudara":
            # Mengcopy 3 nilai dari kunci lama , pukul , panggiilan
            lama = int(jadwal['lama'])
            pukul = int(jadwal['pukul'])
            nama = jadwal['panggilan']
            # Mengisi isi WB dengan data contoh jika lama = 2,pukul = 10, nama = budy 
            # maka akan menambah data {nama:budi,pukul:10},{nama:budi,pukul:11} pada WB
            for d in range(lama):
                WB.append({'nama':nama,'pukul':pukul+d})

        elif jadwal['lapangan'] == "Cherrybale":
            lama = int(jadwal['lama'])
            pukul = int(jadwal['pukul'])
            nama = jadwal['panggilan']
            for t in range(lama):
                CB.append({'nama':nama,'pukul':pukul+t})
        elif jadwal['lapangan'] == "Blackpink":
            lama = int(jadwal['lama'])
            pukul = int(jadwal['pukul'])
            nama = jadwal['panggilan']
            for r in range(lama):
                BP.append({'nama':nama,'pukul':pukul+r})
        elif jadwal['lapangan'] == "SMASH":
            lama = int(jadwal['lama'])
            pukul = int(jadwal['pukul'])
            nama = jadwal['panggilan']
            for e in range(lama+1):
                SM.append({'nama':nama,'pukul':pukul+e})
    # Print list jadwal dari jam 9 - jam 22 
    for i in range(9,22):
        # contoh line satu i = 9 , maka | 09:00 - 10:00 | - | - | - | - | jika tidak ada jadwal pada data jadwals
        print("| %.2d:00-%.2d:00 | %-8s | %-8s | %-8s | %-8s | "%(i,i+1,check_jadwal(i,WB),check_jadwal(i,CB),check_jadwal(i,BP),check_jadwal(i,SM)))
    input('Enter untuk melanjutkan')


def pesan_lapangan(tanggal,bulan):
   
    data_pelanggan = loadData('pelanggan.json',folder='data')
    while True:
        ada = True
        pilih = input('Pelanggan baru?(y/n) : ')
        if pilih == 'y':
            tambahData()
            data_pelanggan = loadData('pelanggan.json',folder='data')
        os.system('cls')
        print('---------------------------------')
        print('---------Menu Pemesanan----------')
        print('---------------------------------')
        if data_pelanggan == []:
            print('Pelanggan baru mohon buat akun')
            continue
        print('Masukkan n untuk kembali')
        panggilan = input("Masukkan panggilan : ")
        if panggilan == 'n':
            break
        # mengambil daya nama dan tipe pada data pelanggan
        for pelanggan in data_pelanggan:
            if pelanggan['panggilan'] == panggilan:

                nama = pelanggan['nama']
                tipe = pelanggan['tipe']
                ada = True
                break
            else:
                ada = False
                print('Pelanggan baru mohon buat akun')
        if not ada :
            continue
        elif ada:
            break 
    if not panggilan == 'n':
        jadwals = loadData("%.2d-%.2d-2021.json"%(bulan,tanggal),folder='data/jadwal_penuh')
        while True:
            lihat_lapangan(tanggal,bulan)
            print('Harga per jam : Rp. 80.000')
            waktu = int(input('Pesan dari pukul? (9-22) : '))
            jam = int(input('Berapa jam ?: '))
            print('Lapangan') 
            print('1. Windah Bersaudara(WB)')
            print('2. Cherrybale(CB)')
            print('3. Blackpink(BP)')
            print('4. SMASH(SM) ')
            jalan = True
            while True:
                no_lapangan = input('Pilih no lapangan : ')
                if no_lapangan == '1':
                    lapangan = 'Windah Basaudara'
                elif no_lapangan == '2':
                    lapangan = 'Cherrybale'
                elif no_lapangan == '3':
                    lapangan = 'Blackpink'
                elif no_lapangan == '4':
                    lapangan = 'SMASH'
                else:
                    continue
                break
            # res berisi jam yang tidak diperbolehkan dipesan karena sudah penuh
            res = []    
            for jadwal in jadwals:
                # check lapangan pada jadwal apakah sama dengan lapangan
                if jadwal['lapangan'] == lapangan:

                    # Mengisi isi res dengan data contoh jika lama = 2,pukul = 10 pada jadwal
                    # maka akan menambah data {pukul:10},s{pukul:11} pada res
                    for k in range(jadwal['lama']):
                        res.append(jadwal['pukul']+k)

            # check bila waktu dan jam dari input tidak termasuk dalam list waktu yg dilarang untuk dipilih pada list res tadi#
            for i in range(waktu,waktu+jam):
                if i in res:
                    jalan = False
                    os.system('cls')
                    print('Jadwal sudah penuh mohon lihat jadwal lagi')
                    break
            if not waktu in range(9,23) or not waktu + jam in range(9,23):
                jalan = False
                os.system('cls')
                print('Jadwal tidak ada mohon lihat jadwal lagi')

            if jalan :
                break
            #-------------------------------------------------------------------------------------------------------------------#

        harga = int(jam)*harga_lap
        print('Harga : ',rupiah(harga))
        
        end = input('Enter untuk meneruskan,n untuk kembali')
        if end == 'n':
            menu_utama()
        else:
            struck(nama,panggilan,waktu,jam,tanggal,bulan,lapangan,harga,tipe)


def struck(nama,panggilan,waktu,jam,tanggal,bulan,lapangan,harga,tipe):
    os.system('cls')
    data = loadData("pelanggan.json", folder="data")
    diskon = 0
    for d in data:
        if d['panggilan'] == panggilan:
            tipe_pembeli = d['tipe']
            d['jumlah_pemesanan'] += 1
        # jika pemesanan adalah kelipatan 5 maka akan diskon 10000
            if d['jumlah_pemesanan'] % 5 == 0 and d['tipe'] == 'member':
                diskon += 10000
            elif d['jumlah_pemesanan'] % 25 == 0  and d['tipe'] == 'member':
            # jika pemesanan adalah kelipatan 25 maka akan diskon 10000
                diskon += 20000
            else:
                diskon += 0

    simpanData('pelanggan.json',folder='data',data=data)
    harga_total = (harga_lap * jam) - diskon 
    print('---------------------------------')
    print('---------Menu Pembayaran---------')
    print('---------------------------------')
    print('Diskon   : ',rupiah(diskon))
    print('Harga    : ',rupiah(harga_total))
    while True:
        # Bila diinput 20 000 maka akan diubah menjadi 20000
        bayar = ''.join(input('Bayar    : ').split())
        if not bayar.isnumeric() :
            continue
        else :
            if int(bayar) < harga_total:
                print('Uang kurang mencukupi')
                print(bayar)
                continue
        bayar = int(bayar)
        break
    # Print struk
    os.system('cls')
    print('-----------------------------------------------')
    print('--------------------Struk----------------------')
    print('-----------------------------------------------')
    print('Nama Pembeli         : ',nama)
    print('Nama lapangan        : ',lapangan)
    print('Harga                : ',rupiah(harga_lap))
    print('Tanggal              : '+ ' %.2d-%.2d-2021'%(tanggal,bulan))
    print('Jam sewa             : ','%.2d:00-%.2d:00'%(waktu,waktu+jam) )
    print('-----------------------------------------------')
    print('Jumlah               : ',rupiah(harga))
    print('Diskon               : ',rupiah(diskon))
    print('-----------------------------------------------')
    print('Total bayar          : ',rupiah(harga_total))
    print('Bayar                : ',rupiah(bayar))
    print('Kembalian            : ',rupiah(bayar-harga_total))
    print('-----------------------------------------------')

    print('Terima Kasih Telah Memesan di Aplikasi Kami')
    # Menyimpan data transaksi dan data jadwal yang sudah diproses tadi

    data = loadData("%.2d-%.2d-2021.json"%(int(bulan),int(tanggal)), folder="data/jadwal_penuh")
    data.append({'nama':nama,'panggilan':panggilan,'tipe':tipe,'pukul':waktu,'lama':jam,'tanggal':tanggal,'bulan':bulan,'lapangan': lapangan})
    simpanData("%.2d-%.2d-2021.json"%(int(bulan),int(tanggal)),data=data,folder='data/jadwal_penuh')
    trans = loadData(f'{str(tanggal_trans)}.json',folder='data/transaksi')
    trans.append({'nama':nama,'panggilan':panggilan,'order':tanggal_trans,'total_bayar':harga_total,'tipe':tipe})
    simpanData(f'{str(tanggal_trans)}.json',folder='data/transaksi',data=trans)

    #---------------------------------------------------#
    input('Enter untuk melanjutkan')
    os.system('cls')


def lihat_pemasukan():
    os.system('cls')
    # Melihat isi dari foler transaksi , files akan berisi list nama file pada folder transaksi
    files = os.listdir('data/transaksi')
   
    # Lihat pemasukkan hari ini
    pemasukkan = 0
    for file in files:
        # Format awal contoh 2021-11-02 , maka akan dislice strnya sesuai dengan posisi tanggal,bulan,tahun
        tanggal = file[8:10]
        bulan = file[5:7]
        tahun = file[0:4]
        if tanggal == str(datetime.date.today())[8:10]:
            data = loadData(file,folder='data/transaksi')
            for i in data:
                pemasukkan += i['total_bayar']
    
    while True:
        os.system('cls')
        print('-----------------------------------------------------')
        print('--------------------Lihat Pemasukkan-----------------')
        print('-----------------------------------------------------')
        print('Hasil pemasukkan hari ini : ',rupiah(pemasukkan))
        print('1.Tahunan 2.Bulanan 3.Harian 4.Jumlah user 5.Kembali')
        pilih = input('Pilih lihat laporan : ')
        # Check pilih
        if pilih == '1':
            while True:
                # Mengapus white space diawal dan akhir output
                tahun = input('Masukkan Tahun : ').strip()
                # Check apakah termasuk angka atau tidak

                if not (tahun.isnumeric()):
                    print('Masukkan dengan benar')
                    continue
                break
            # Menjumlahkan pemasukkan satu tahun
            pemasukkan = 0
            jumlah_beli_member = 0
            jumlah_pesan_lapangan = 0
            for file in files:
                # Check semua nama file apakah irisan nama file index ke 0-3 apakah sama dengan tahun yang diinput
                if file[0:4] == tahun:
                    data = loadData(file,folder='data/transaksi')
                    # Menambah semua data transaksi di file yg diload di data = loadData()
                    for i in data:
                        pemasukkan += i['total_bayar']
                        if 'transaksi' in i.keys():
                            jumlah_beli_member += 1
                        else :
                            jumlah_pesan_lapangan += 1
            # jumlah pemasukkan
            os.system('cls')
            print(f'Tahun : {tahun}')
            print('----------------------------------------------------------')
            print('Hasil pemasukkan tahunan                   : ',rupiah(pemasukkan))
            print('----------------------------------------------------------')
            print('Jumlah member baru                         : ',jumlah_beli_member)
            print('Jumlah Pemasukan dari beli member          : ',rupiah(jumlah_beli_member* 50000))
            print('----------------------------------------------------------')
            print('Jumlah pemesanan lapangan                  : ',jumlah_pesan_lapangan)
            print('Jumlah pemasukkan dari pemesanan lapangan  : ', rupiah(pemasukkan - (jumlah_beli_member*50000)))
            print('----------------------------------------------------------')
            input('Enter untuk melanjutkan')
            os.system('cls')
        elif pilih == '2':
            while True:
                tahun = ''.join(input('Masukkan Tahun : ').split())
                bulan = ''.join(input('Masukkan Bulan : ').split())
                if not (tahun.isnumeric() and bulan.isnumeric()):
                    print('Masukkan dengan benar')
                    continue
                break
            pemasukkan = 0
            jumlah_beli_member = 0
            jumlah_pesan_lapangan = 0
            for file in files:
                if file[0:4] == tahun:
                    if file[5:7] == '%.2d'%(int(bulan)):
                        data = loadData(file,folder='data/transaksi')
                        for i in data:
                            pemasukkan += i['total_bayar']
                            if 'transaksi' in i.keys():
                                jumlah_beli_member += 1
                            else :
                                jumlah_pesan_lapangan += 1
            os.system('cls')
            print(f'Pemasukkan Bulan : {bulan}, Tahun : {tahun}')
            print('----------------------------------------------------------')
            print('Hasil pemasukkan bulanan                   : ',rupiah(pemasukkan))
            print('----------------------------------------------------------')
            print('Jumlah member baru                         : ',jumlah_beli_member)
            print('Jumlah Pemasukan dari beli member          : ',rupiah(jumlah_beli_member* 50000))
            print('----------------------------------------------------------')
            print('Jumlah pemesanan lapangan                  : ',jumlah_pesan_lapangan)
            print('Jumlah pemasukkan dari pemesanan lapangan  : ', rupiah(pemasukkan - (jumlah_beli_member*50000)))
            print('----------------------------------------------------------')
            input('Enter untuk melanjutkan')
            os.system('cls')
        elif pilih == '3':
            while True:
                tahun = ''.join(input('Masukkan Tahun : ').split())
                bulan = ''.join(input('Masukkan Bulan : ').split())
                hari = ''.join(input('Masukkan Tanggal : ').split())
                if not (tahun.isnumeric() and bulan.isnumeric() and hari.isnumeric()):
                    print('Masukkan dengan benar')
                    continue
                break
            pemasukkan = 0
            jumlah_beli_member = 0
            jumlah_pesan_lapangan = 0
            for file in files:
                if file[0:4] == tahun:
                    if file[5:7] == '%.2d'%(int(bulan)):
                        if file[8:10] == '%.2d'%(int(hari)):
                            data = loadData(file,folder='data/transaksi')
                            for i in data:
                                pemasukkan += i['total_bayar']
                                if 'transaksi' in i.keys():
                                    jumlah_beli_member += 1
                                else :
                                    jumlah_pesan_lapangan += 1
            os.system('cls')
            print(f'Pemasukkan Tanggal : {hari}, Bulan : {bulan}, Tahun : {tahun}')
            print('----------------------------------------------------------')
            print('Hasil pemasukkan harian                   : ',rupiah(pemasukkan))
            print('----------------------------------------------------------')
            print('Jumlah member baru                         : ',jumlah_beli_member)
            print('Jumlah Pemasukan dari beli member          : ',rupiah(jumlah_beli_member* 50000))
            print('----------------------------------------------------------')
            print('Jumlah pemesanan lapangan                  : ',jumlah_pesan_lapangan)
            print('Jumlah pemasukkan dari pemesanan lapangan  : ', rupiah(pemasukkan - (jumlah_beli_member*50000)))
            print('----------------------------------------------------------')
            input('Enter untuk melanjutkan')
            os.system('cls')
        elif pilih == '4':
            pelanggan = loadData('pelanggan.json',folder='data')
            member = 0
            reguler = 0
            for p in pelanggan:
                if p['tipe'] == 'member':
                    member += 1
                elif p['tipe'] == 'reguler':
                    reguler += 1
            os.system('cls')
            print('------------------------------------------------')
            print('Jumlah member terdaftar : ',member)
            print('Jumlah total user       : ',reguler+member)
            print('------------------------------------------------')
            input('Enter untuk kembali')
            os.system('cls')
        elif pilih == '5':
            break
if __name__ == '__main__':
    welcome()