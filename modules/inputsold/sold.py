'input sold'

import datetime as dt


def sold(ws, empty_cell):
    'function sold'
    try:
        jumlah = int(input('Masukkan penjualan hari ini:\n>>> '))

        ws[empty_cell[0]] = dt.datetime.now()
        ws[empty_cell[1]] = jumlah
    except:  # pylint: disable=bare-except
        print('Input harus berupa angka')
