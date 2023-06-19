[日本の古本屋](https://www.kosho.or.jp/)
================================================

- [ ] 検索結果のテーブル化を目標とする


検索API パラメータ分析
----------------------

- Entry point: https://www.kosho.or.jp/products/list.php
- Parameters:

mode
  values:search, search_retry (other mode is unknown)

search_only_has_stock
  values: 0/1 (1: true, 0: false)

search_word
  search_word

search_pageno
  values: int

pageno
  ?

product_id
  ?

reset_baseinfo_id
  ?

baseinfo_id
  ?

product_class_id
  ?

quantity
  ?

from_mode
  ?

search_facet_publisher
  ?

search_publisher
  publisher

search_publisher_matchtype
  含む:like
  含まない：
  完全：

search_name
  署名

search_name_matchtype
  含む：like
  含まない： not_like
  完全: equal

search_author
  著者名

search_author_matchtype
  含む: like
  含まない： not_like
  完全：equal

search_isbn
  ISBN/ISSN

search_published_year_min
  int

search_published_year_max
  int

search_comment4
  解説

search_comment4_matchtype
  含む：like
  完全: equal

search_book_flg
  ?

search_price_min
  最低価格: int

search_price_max
  価格上限: int

search_only_has_stock
  int 0/1

  在庫ありなし (0: false, 1: true)

serach_only_set
  セット販売 0/1

search_only_has_review
  レビューあり 0/1

search_orderby
  関連度：score

search_sorttype=asc
  ソート順

  asc: 昇順
  desc: 降順

search_page_max
  表示件数

search_image_disp
  検索結果の画像を表示する

  default: true
  OFF: off

search_adult
  成人図書を表示する

  1: true, 2: false
