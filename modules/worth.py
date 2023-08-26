'worth func'
import locale


def to_currency(num, times):
    'tocurrency'
    return str(locale.currency(num * times, grouping=True))


def worth(ws):  # pylint: disable=invalid-name
    'worth func'
    counter = 2
    total = 0
    while True:
        letnum = f'C{counter}'
        cells = ws[letnum].value
        if cells is None:
            break
        counter += 1
        total += int(cells)

    terjual = f'{str(total):^10}'
    p_k = f'{to_currency(total, 2500):^45}'
    p_b = f'{to_currency(total, 500):^45}'

    print(110*'=')
    print(
        f"| {'Terjual':^10} | {'Pendapatan Kotor':^45} | {'Pendapatan Bersih':^45} |")
    print(110*'-')
    print(
        f'| {terjual} | {p_k} | {p_b} |')
    print(110*'=')
