# 使い方

```bash
pipenv install -d
```



```bash
pipenv run tests
```

- おまじない

```bash
export PYTEST_ADDOPTS='-v -s --pdb --ff --doctest-modules'
```

- --doctest-modules を定義すると、pytestからdoctestを実行できます。
- --pdb: テスト失敗時に pdb（デバッガ） を起動
- --ff: 前回失敗したテストを先に実行


```bash
pipenv install jsondiff
pipenv install deepdiff
```