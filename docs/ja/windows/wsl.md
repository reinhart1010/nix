---
layout: page
title: windows/wsl (日本語)
description: "Windows Subsystem for Linux を管理します。"
content_hash: 022e943d08e1d369488eff500c476ec642c37b1e
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/windows/wsl.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/wsl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/wsl.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/wsl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/wsl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wsl

Windows Subsystem for Linux を管理します。
もっと詳しく: <https://learn.microsoft.com/windows/wsl/reference>。

- Linuxシェルを起動する(デフォルトのディストリビューションの場合):

`wsl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">シェルコマンド</span>

- シェルを使わずにLinuxコマンドを実行する:

`wsl --exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド引数</span>

- 特定のディストリビューションを指定する:

`wsl --distribution `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディストリビューション</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">シェルコマンド</span>

- 利用可能なディストリビューションを一覧表示する:

`wsl --list`

- ディストリビューションを`.tar`ファイルにエクスポートする:

`wsl --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディストリビューション</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\distro_file.tar</span>

- ディストリビューションを`.tar`ファイルからインポートする:

`wsl --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディストリビューション</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\install_location</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/distro_file.tar</span>

- 指定したディストリビューションで使用するwslのバージョンを変更する:

`wsl --set-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディストリビューション</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">バージョン</span>

- Windows Subsystem for Linux をシャットダウンする:

`wsl --shutdown`
