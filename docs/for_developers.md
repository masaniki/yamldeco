# For Developers

開発者向けのmessageを記述する。

## Deploy

### build

version情報は`src/yamldeco/decoModule.py`と`pyproject.toml`にあるので、その2か所を更新する。

`Python -m build .`

### upload

test PyPIへのupload.

`twine upload -r testpypi "dist/*"`

PyPIへのupload

`twine upload "dist/*"`

## Testing

testの仕方を記述する。

## Branchs

branch戦略を記述する。

### `master`

現在公開中のbranch。

### `develop`

破壊的commitが禁止されているbranch。

masterへmergeする。

### `feat/*`

破壊的commitができるbranch。

developへmergeする。

merge後は削除。
