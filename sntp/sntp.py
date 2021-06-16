import argparse
import socket

from SNTPServer import SNTPServer


def parse_args():
    parser = argparse.ArgumentParser(description='SNTP experimental server')
    parser.add_argument('-d', '--delay', type=int, default=20.0,
                        help='Set delay')
    parser.add_argument('-p', '--port', type=int, nargs=1, default=123,
                        help='Listen port')
    return parser.parse_args().__dict__


def start(delay: int, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('localhost', port))
    s.settimeout(1)

    sntp = SNTPServer(s, delay)
    sntp.run()


if __name__ == "__main__":
    args = parse_args()
    start(**args)
