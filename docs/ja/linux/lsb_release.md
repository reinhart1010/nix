---
layout: page
title: linux/lsb_release (日本語)
description: "LSB (Linux Standard Base)とディストリビューション固有の情報を取得します。"
content_hash: 9fa10729af90409a0831366178f179f29d944f79
last_modified_at: 2025-03-02
related_topics:
  - title: català version
    url: /ca/linux/lsb_release.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/lsb_release.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/lsb_release.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/linux/lsb_release.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/lsb_release.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsb_release

LSB (Linux Standard Base)とディストリビューション固有の情報を取得します。
もっと詳しく: <https://manned.org/lsb_release>。

- 利用可能なすべての情報を表示する:

`lsb_release -a`

- オペレーティングシステムの説明(通常はフルネーム)を表示する:

`lsb_release -d`

- オペレーティングシステムの名前(ID)だけを表示する:

`lsb_release -i -s`

- ディストリビューションのリリース番号とコードネームを表示する:

`lsb_release -rcs`
