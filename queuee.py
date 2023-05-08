import os
import queue
os.system('cls')

# queue merupakan sebuah antrian

class myQ:
    def __init__(self):
        self.item = queue.Queue()
        
    #memeriksa queue kosong
    def isEmpty(self):
        return self.item.empty()
    
    #menambahkan elemen pada queue
    def qPut(self,item):
        self.item.put(item)
        
    #mengeluarkan elemen pada queue
    def qGet(self):
        if not self.item.empty():
            return self.item.get()
        else:
            return "empty"
    #mengeluarkan semua elemen
    def qGetAll(self):
        while not self.item.empty():
            self.item.get()
        
    #menghitung panjang queue
    def size(self):
        return self.item.qsize()
    
    #print queue
    def print(self):
        return self.item.queue
    
    #menu
    def menu(self):
        pilih = 'y'
        while pilih == 'y':
            print("1. Menambahkan Elemen")
            print("2. Megeluarkan Elemen")
            print("3. Ukuran Elemen")
            print("4. Cek Elemen")
            print("5. print Queue")
            print("6. mengeluarkan")
            pilihan = str(input("Pilih menu : "))
            if pilihan == "1":
                obj = str(input("Masukan Data : "))
                self.qPut(obj)
                print("===============================")
                print("Elemen "+obj+" Sudah ditambahkan")
                print ("==================================")
                
            elif pilihan == "2":
                obj = self.qGet()
                if obj != "empty":
                    print("===============================")
                    print("Elemen "+obj+" Sudah Dihapus")
                    print("===============================")
                else:
                    print("===============================")
                    print("Queue Kosong")
                    print("===============================")
                    
            elif pilihan == "3":
                print("===============================")
                print ("ukuran queue "+str(self.size()))
                print("===============================")
                
            elif pilihan == "4":
                print("===============================")
                print (self.isEmpty())
                print("===============================")
                
            elif pilihan == "5":
                print("===============================")
                print (self.print())
                print("===============================")
                
            elif pilihan == "6":
                print("===============================")
                print (self.qGetAll())
                print("===============================")
            else:
                pilih = 'n'
                
if __name__ == "__main__":
    q=myQ()
    q.menu()
                
