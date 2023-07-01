#!/usr/bin/env python
from argparse import ArgumentParser
import requests

parser = ArgumentParser()
parser.add_argument('--mode', type=str, required=False, default='search')
parser.add_argument('--has_stock', type=int, required=False, default=0, choices=(0, 1))

parser.add_argument('--search_word', type=str, required=False, default='')
parser.add_argument('--search_publisher', type=str, required=False, default='')
parser.add_argument('--search_publisher_matchtype', type=str, required=False,
                    choices=('like', 'not_like', 'equal'))
parser.add_argument('--search_author', type=str, required=False, default='')
parser.add_argument('--search_author_matchtype', type=str, required=False,
                    choices=('like', 'not_like', 'equal'))

parser.add_argument('--search_isbn', type=str, required=False, default='')
parser.add_argument('--search_price_min', type=int, required=False, default=None)
parser.add_argument('--search_price_max', type=int, required=False, default=None)
parser.add_argument('--search_only_has_stock', type=int, required=False, choices=(0,1), default=0)

parser.add_argument('--search_image_disp', type=str, required=False, default='true')

entrypoint = 'https://www.kosho.or.jp/products/list.php'

def main(args):
    payload = dict()
    payload.update(mode=args.mode)
    payload.update(has_stock=1 - args.has_stock)
    payload.update(search_word=args.search_word)
    payload.update(search_publisher=args.search_publisher)
    payload.update(search_publisher_matchtype=args.search_publisher_matchtype)
    payload.update(search_author=args.search_author)
    payload.update(search_author_matchtype=args.search_author_matchtype)
    payload.update(search_isbn=args.search_isbn)
    if args.search_price_min:
        payload.update(search_price_min=args.search_price_min)
    if args.search_price_max:
        payload.update(search_price_max=args.search_price_max)
    payload.update(search_only_has_stock=1 - args.search_only_has_stock)
    payload.update(search_image_disp=args.search_image_disp)

    r = requests.get(entrypoint, params=payload)
    print(r.text)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
