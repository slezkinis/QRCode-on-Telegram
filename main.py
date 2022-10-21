import argparse
import qrcode


def qr_code(text, name):
    qr = qrcode.make(text)
    qr.save(name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', help='Ссылка', default='https://www.youtube.com/channel/UC92EEOWePEoz09IpI4MZ3Wg')
    parser.add_argument('-n', '--name', help='Название файла', default='qrcode.png')
    args = parser.parse_args()
    qr_code(args.text, args.name)