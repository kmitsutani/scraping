#!/usr/bin/env python
from argparse import ArgumentParser
import requests

parser = ArgumentParser()
parser.add_argument('--mode', type=str, required=False, default='search')

parser.add_argument('--word', type=str, required=False, default='')
parser.add_argument('--title', type=str, required=False, default='')
parser.add_argument('--title-mt', type=str, required=False, default='like',
                    choices=('like', 'equal'))
parser.add_argument('--author', type=str, required=False, default='')
parser.add_argument('--author-mt', type=str, required=False,
                    choices=('like', 'not_like', 'equal'))
parser.add_argument('--publisher', type=str, required=False, default='')
parser.add_argument('--publisher-mt', type=str, required=False,
                    choices=('like', 'not_like', 'equal'))

parser.add_argument('--isbn', type=str, required=False, default='')
parser.add_argument('--year', type=int, required=False, nargs=2, default=(-1, -1))
parser.add_argument('--price', type=int, nargs=2, required=False, default=(-1, -1))
parser.add_argument('--detail', type=str, required=False, default='')
parser.add_argument('--detail-mt', type=str, required=False, default="like",
                    choices=('like', 'equal'))

category_dict = dict(book=1, magazine=2, media=3, paper=4, other=5)
def category_type(category_str):
    return category_dict[category_str]

parser.add_argument('--category', type=category_type, required=False, default=1,
                    choices=('book', 'magazine', 'media', 'paper', 'other'))

parser.add_argument('--pick-up', type=str, required=False, default=None)
order_dict = dict(
    relevance='score',
    title='name',
    author='author',
    publisher='publisher',
    year='year',
    new='update_date'
)
def order_type(order_str):
    return order_dict[order_str]
parser.add_argument('--orderby', type=order_type,
                    required=False, default='relevance',
                    choices=('score', 'title', 'author', 'publisher', 'year', 'new'))
parser.add_argument('--pages', type=int, required=False, default=25, choices=(25, 50, 100))

def image_type(image_str):
    return "" if image_str == 1 else "OFF"
parser.add_argument('--image', type=image_type, required=False, default="OFF",
                    choices=(1, 0))
parser.add_argument('--adult', type=lambda x: 2 - int(x), required=False, choices=(0, 1))


entrypoint = 'https://www.kosho.or.jp/products/list.php'

def main(args):
    payload = dict()
    payload.update(mode=args.mode)
    if args.word:
        payload.update(search_word=args.word)
    if args.title:
        payload.update(search_name=args.title)
        payload.update(search_name_matchtype=args.title-mt)
    if args.author:
        payload.update(search_author=args.author)
        payload.update(search_author_matchtype=args.author-mt)
    if args.publisher:
        payload.update(search_publisher=args.publisher)
        payload.update(search_publisher_matchtype=args.publisher-mt)
    if args.isbn:
        payload.update(search_isbn=args.isbn)
    year_min, year_max = args.year
    if year_min > 0:
        payload.update(search_published_year_min=year_min)
    if year_max > 0:
        payload.update(search_published_year_max=year_max)

    price_min, price_max = args.price
    if price_min > 0:
        payload.update(serach_price_min=price_min)
    if price_max > 0:
        payload.update(search_price_max=price_max)

    if args.detail:
        payload.update(search_comment4=args.detail)
        payload.update(search_comment4_mathchtype=args.detail-mt)

    if args.category:
        payload.update(search_book_flg=args.category)

    if args.pick_up:
        if 'set' in args.pick_up:
            payload.update(search_only_set=1)
        if 'has_stock' in args.pick_up:
            payload.update(search_only_has_stock=1)
        if 'reviewed' in args.pick_up:
            payload.update(search_only_has_review)


    payload.update(search_orderby=args.orderby)
    payload.update(search_page_max=args.pages)
    payload.update(search_image_disp=args.image)
    payload.update(search_adult=args.adult)

    r = requests.get(entrypoint, params=payload)
    print(r.text)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
