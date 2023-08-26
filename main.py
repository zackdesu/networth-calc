'main'

import locale
import openpyxl as xl
import modules

if __name__ == '__main__':

    wb = xl.load_workbook('./dist/product.xlsx')
    ws = wb.active

    locale.setlocale(locale.LC_ALL, 'id_ID')

    while True:
        modules.clear()
        print(f"{'Aplikasi Penjualan Risoles Saya':^100}")
        print(100 * '=')
        print(f'''{'||':<98}||
{"||":<32}{"1. Memasukkan penjualan hari ini":<66}||
{"||":<32}{"2. Melihat pendapatan kotor dan bersih":<66}||
{"||":<32}{"3. Keluar":<66}||
{'||':<98}||''')
        print(100 * '=')

        option = int(input('\nPilihlah opsi:\n>>> '))

        match option:
            case 1:
                modules.clear()
                cells = modules.cell(ws)
                modules.sold(ws, cells)
                wb.save('./dist/product2.xlsx')
            case 2:
                modules.clear()
                modules.worth(ws)
            case 3: break
            case _:
                print('\nInput tidak valid!')

        option = input('\nLanjutkan? (y/n)\n>>> ')
        if option == 'n':
            break
