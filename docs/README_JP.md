# 自己紹介

YAMLやJSONに説明文を付けるためのライブラリです。

# インストール方法

`pip install yamldeco`

# 使い方

簡単な使用例を記述する。

# 詳細

形式層と装飾層を交互に入れ子にする。

装飾層は"@"から始まるdict型。

"@Children"で装飾層から形式層へ移行する。

JSONにも対応する。拡張子".json"の時はJSONとして処理する。その他の拡張子は全てYAMLとして処理する。

simple YAML ----decorate---> decoration YAML

simple YAML <---simplify---- decoration YAML

## 詳細

`yamldeco [-h] [-v] [-i {yaml,json,auto}] [-o {yaml,json,auto}] [-m {d,s,a,decorate,simplify,auto}] origin outcome`

位置引数:
| 変数名  | 説明 |
| ---     | --- |
| origin  | 変更前のfile名を指定する。YAMLかJSON。 |
| outcome | 出力するfile名を指定する。YAMLかJSON。 |

オプション引数:
| 変数名        | 初期値 | 説明　|
| ---           | --- | --- |
| [-h\|--help]  | --- | help messageを表示する。 |
| [-v\|--version] | --- | version messageを表示する。 |
| [-i\|--input] {yaml,json,auto} | auto | \<origin\>のfile形式を指定する。autoの時は拡張子に基づいて判断。 |
| [-o\|--output] {yaml,json,auto} | auto | \<outcome\>のfile形式を指定する。autoの時は拡張子に基づいて判断。 |
| [-m\|--method] {d,s,a,decorate,simplify,auto} | auto | decorateかsimplifyかを指定する。autoの時は\<origin\>の中に接頭辞`@`があるか否かで判断。 |

## Next To Do

- [ ] to do things.

## Ideas

- fileだけでなく、directoryも引数にできるようにする。
- そうすると、file名のfilterが必要になる。
- file名のfilterをどうするか？

"@Plh"でplaceholderを表す。\<yamldeco\>から\<yaml\>への変換にはplaceholderの指定が必須。

# Others

## /docs
documentを格納するdirecotry.

## /src
ここでmoduleを開発する。

## testUnit
単体testを行うdirectory。

## testSystem
結合testを行うdirectory。

## sanbox.py
pythonの挙動を確認する。

