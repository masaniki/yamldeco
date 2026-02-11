# 概要

日本語で記述。

# インストール方法

`pip install <package_name>`

## パッケージ依存性

以下のpackageをインストールしないと正しく機能しない場合があります。

- [PyYAML](https://pypi.org/project/PyYAML/): 最も人気なPyhton用のYAMLパーサーです。

# 使い方

簡単な使用例を記述する。

# 詳細

YAMLやJSONに説明文を加えるためのlibrary。

形式層と装飾層を交互に入れ子にする。

装飾層は"@"から始まるdict型。

"@Children"で装飾層から形式層へ移行する。

"@Plh"でplaceholderを表す。\<yamldeco\>から\<yaml\>への変換にはplaceholderの指定が必須。

JSONにも対応する。拡張子".json"の時はJSONとして処理する。その他の拡張子は全てYAMLとして処理する。


## YAMLDECO CLI

`yamldeco (-v|--version)`:

- yamldecoのversion情報を出力する。

`yamldeco (-h|--help)`:

- yamldecoのcommandの使い方を出力する。

`yamldeco <input> <output>`

- もっとも簡単な使い方。

- 厳密には`yamldeco <input> <output> --in auto --out auto --method auto`の糖衣構文である。


`yamldeco <input> <output> [(-i|--in) (yaml|json|auto)]`

- defaultは`auto`.

- `-i yaml`

  \<input\>をYAMLとして解釈する。

- `-i json`

  \<input\>をJSONとして解釈する。

- `-i auto`

  \<input\>の拡張子が".json"ならばJSONとして解釈する。

  その他の拡張子の場合はYAMLとして解釈する。

`yamldeco <input> <output> [(-o|--out) (yaml|json|auto)]`

- defaultは`auto`.

- `-o yaml`

  \<output\>をYAMLとして解釈する。

- `-o json`

  \<output\>をJSONとして解釈する。

- `-o auto`

  \<output\>の拡張子が".json"ならばJSONとして解釈する。

  その他の拡張子の場合はYAMLとして解釈する。


`yamldeco <input> <output> [(-m|--method) (d|decorate|s|simplify|a|auto)]`

- defaultは`auto`。

- `-m (d|decorate)`

  \<input\>をsimple YAMLで解釈して、\<output\>にdecoration YAMLを返す。

- `-m (s|simplify)`

  \<input\>をdecotation YAMLで解釈して、\<output\>にsimple YAMLを返す。

- `-m (a|auto)`

  \<input\>が接頭辞`@`を含む場合、`-m simplify`と同様に振る舞う。

  逆に接頭辞`@`を含まない場合は、`-m decorate`と同様に振る舞う。


## Next To Do

- [ ] to do things.

## Ideas

- fileだけでなく、directoryも引数にできるようにする。
- そうすると、file名のfilterが必要になる。
- file名のfilterをどうするか？

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

