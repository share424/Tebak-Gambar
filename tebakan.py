import random


def main():
    # tentukan angka misteri
    misteri = random.randint(1, 100)
    tebakan = 0
    counter = 0
    while misteri != tebakan:
        counter += 1
        # masukkan angka tebakan
        tebakan = input('Masukkan angka tebakan: ')
        tebakan = int(tebakan)

        # cek angka tebakan dengan angka misteri
        if tebakan == misteri:
            print(f'Anda benar! Anda telah mencoba sebanyak {counter} kali')
        elif tebakan > misteri:
            print('Tebakan Anda kebesaran!')
        else:
            print('Tebakan kekecilan!')


if __name__ == '__main__':
    main()
