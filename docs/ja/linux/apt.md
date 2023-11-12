---
layout: page
title: linux/apt (日本語)
description: "Debian系ディストリビューションで使われるパッケージ管理システムです。"
content_hash: 3c81e31f609cb269aa88ee2fb63b466dcfdc0f9d
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Debian系ディストリビューションで使われるパッケージ管理システムです。
Ubuntuのバージョンが16.04か、それ以降で対話モードを使う場合`apt-get`の代わりとして使用します。
詳しくはこちら: <https://manpages.debian.org/latest/apt/apt.8.html>

- 利用可能なパーケージとバージョンのリストの更新（他の`apt`コマンドの前での実行を推奨）:

`sudo apt update`

- 指定されたパッケージの検索:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パッケージ</span>

- パッケージの情報を出力:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パッケージ</span>

- パッケージのインストール、または利用可能な最新バージョンに更新:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パッケージ</span>

- パッケージの削除（`sudo apt remove --purge`の場合設定ファイルも削除）:

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パッケージ</span>

- インストールされている全てのパッケージを最新のバージョンにアップグレード:

`sudo apt upgrade`

- インストールできるすべてのパッケージを表示:

`apt list`

- インストールされた全てのパッケージを表示（依存関係も表示）:

`apt list --installed`
