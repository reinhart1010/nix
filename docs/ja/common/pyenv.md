---
layout: page
title: common/pyenv (日本語)
description: "複数バージョンのPythonを容易に切り替えします。"
content_hash: 312e0a0dd7e5861f43ac9ab2261ad2075e9e4eca
last_modified_at: 2023-11-06
related_topics:
  - title: English version
    url: /en/common/pyenv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/pyenv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pyenv.html
    icon: bi bi-globe
---
# pyenv

複数バージョンのPythonを容易に切り替えします。
詳しくはこちら: <https://github.com/pyenv/pyenv>

- 利用可能なコマンド全てをリスト表示する:

`pyenv commands`

- `${PYENV_ROOT}/versions`ディレクトリ下のPythonバージョン全てをリスト表示する:

`pyenv versions`

- アップストリーム(Python公式)からインストール可能なPythonのバージョン全てをリスト表示する:

`pyenv install --list`

- `${PYENV_ROOT}/versions`ディレクトリ下に指定のPythonバージョンをインストールする:

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- `${PYENV_ROOT}/versions`ディレクトリ下の指定のPythonバージョンをアンインストールする:

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 現在のマシンでグローバルに使用するPythonバージョンをセットする:

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- カレントディレクトリとその下にある全てのディレクトリ内で使用するPythonバージョンをセットする:

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
