import sys
from datetime import datetime

from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
                             QLineEdit, QMessageBox, QPushButton, QTableWidget,
                             QTableWidgetItem, QVBoxLayout, QWidget)


class AppListBelanja(QWidget):
    def __init__(self):
        super().__init__()

        # Inisialisasi daftar belanja
        self.item_belanja = []

        # Inisialisasi antarmuka pengguna
        self.init_ui()

    def init_ui(self):
        # GUI element
        self.item_masuk = QLineEdit(self)
        self.tombol_tambah = QPushButton('Tambah', self)
        self.table_belanja = QTableWidget(self)
        self.tombol_hapus = QPushButton('Hapus', self)
        self.tombol_selesai = QPushButton('Selesai', self)
        self.tombol_simpan = QPushButton('Simpan', self)
        self.status_label = QLabel('', self)

        # Layout
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Masukkan Daftar Belanja :'))
        vbox.addWidget(self.item_masuk)
        vbox.addWidget(self.tombol_tambah)
        vbox.addWidget(self.table_belanja)
        vbox.addWidget(self.status_label)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.tombol_hapus)
        hbox.addWidget(self.tombol_selesai)

        vbox.addLayout(hbox)
        vbox.addWidget(self.tombol_simpan)

        self.setLayout(vbox)

        # Menghubungkan tombol dengan fungsi-fungsi
        self.tombol_tambah.clicked.connect(self.tambah_item)
        self.tombol_hapus.clicked.connect(self.hapus_item)
        self.tombol_selesai.clicked.connect(self.tanda_selesai)
        self.tombol_simpan.clicked.connect(self.simpan_list)

        # Memuat daftar yang sudah disimpan
        self.load_list()

        # Setting main / jendela utama
        self.setGeometry(300, 300, 600, 500)
        self.setWindowTitle('Aplikasi Daftar Belanja')
        self.show()

    def tambah_item(self):
        # Menambahkan item baru ke daftar belanja
        item = self.item_masuk.text()
        if item:
            now = datetime.now()
            waktu = now.strftime("%Y-%m-%d %H:%M:%S")
            self.item_belanja.append({'item': item, 'done': False, 'time': waktu})
            self.update_table()
            self.item_masuk.clear()

    def update_table(self):
        # Memperbarui tampilan daftar belanja dalam bentuk tabel
        self.table_belanja.setRowCount(len(self.item_belanja))
        self.table_belanja.setColumnCount(4)  # Menambahkan kolom untuk hari dan jam
        self.table_belanja.setHorizontalHeaderLabels(['Item', 'Selesai', 'Waktu', 'Hari'])
        
        for row, item in enumerate(self.item_belanja):
            item_text = item['item']
            done_text = 'Selesai' if item['done'] else 'Belum Selesai'
            waktu_text = item['time']
            hari_text = datetime.strptime(waktu_text, "%Y-%m-%d %H:%M:%S").strftime('%A')
            
            self.table_belanja.setItem(row, 0, QTableWidgetItem(item_text))
            self.table_belanja.setItem(row, 1, QTableWidgetItem(done_text))
            self.table_belanja.setItem(row, 2, QTableWidgetItem(waktu_text))
            self.table_belanja.setItem(row, 3, QTableWidgetItem(hari_text))

        # Mengatur lebar kolom otomatis
        self.table_belanja.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def hapus_item(self):
        # Menghapus item terpilih dari daftar belanja
        selected_item = self.table_belanja.currentItem()
        if selected_item:
            row = selected_item.row()
            self.item_belanja.pop(row)
            self.update_table()
        QMessageBox.information(self, 'Info', 'Daftar belanja dihapus!')

    def tanda_selesai(self):
        # Menandai item sebagai selesai atau belum selesai
        selected_item = self.table_belanja.currentItem()
        if selected_item:
            row = selected_item.row()
            item = self.item_belanja[row]
            item['done'] = not item['done']
            if item['done']:
                self.status_label.setText('Barang sudah selesai!')
                with open("list_belanja.txt", "a") as file:
                    file.write(f"{item['item']} sudah selesai\n")
            else:
                self.status_label.clear()
            self.update_table()
        QMessageBox.information(self, 'Info', 'Daftar belanja selesai!')

    def simpan_list(self):
        # Menyimpan daftar belanja ke file teks setelah diurutkan
        sorted_items = sorted(self.item_belanja, key=lambda x: x['item'])
        with open("list_belanja.txt", "w") as file:
            for item in sorted_items:
                file.write(f"{item['item']}:{item['done']} - Waktu: {item['time']}\n")
        QMessageBox.information(self, 'Info', 'Daftar belanja berhasil disimpan!')

    def load_list(self):
        # Memuat daftar belanja yang sudah disimpan
        try:
            with open("list_belanja.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().rsplit('-', 1)
                    if len(parts) == 2:
                        item_text, time_part = parts[0].rsplit(':', 1)
                        done_text = parts[1].split(':')[1]
                        time_text = time_part.strip().replace('Waktu: ', '')
                        item = {'item': item_text, 'done': done_text == 'True', 'time': time_text}
                        self.item_belanja.append(item)
                self.update_table()
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppListBelanja()
    sys.exit(app.exec_())
