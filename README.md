# twitrename
全自動Twitter改名機だよ

# 概要
Python3で書かれたよく分からない何か

Cronで殴るたびに勝手に自分のTwiterの名前が変わるらしい

# つかいかた
1. TwitterのOAuthキーを取ってくる→
[https://apps.twitter.com/](https://apps.twitter.com/)

2. APIキーとかを```config.sample.py```に入れる

3. 名前を```name=""```のところに4文字ぐらいで入れる

4. ```config.sample.py```を```config.py```にリネーム

5. ```python3 rename.py```をCronとかでいい感じに叩く

# renamelist.txtの仕様
1行に1つの名前を定義してる

例えば```printf("<Name>")```で、名前が「響音カゲ」だったら```printf("響音カゲ")```に改名される

名前が20文字からあふれると他の名前を使おうとする
