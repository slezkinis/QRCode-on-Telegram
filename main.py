import argparse
import qrcode

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--text', help='Ссылка', default='https://www.youtube.com/channel/UC92EEOWePEoz09IpI4MZ3Wg')
parser.add_argument('-n', '--name', help='Название файла', default='qrcode.png')
args = parser.parse_args()
qr = qrcode.make(args.text)
qr.save(args.name)
