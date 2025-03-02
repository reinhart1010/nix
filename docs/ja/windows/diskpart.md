---
layout: page
title: windows/diskpart (日本語)
description: "ディスク、ボリューム、およびパーティションマネージャ。"
content_hash: 4934c95f23d7901b6fe503ae96c85a7765d6f812
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/windows/diskpart.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/diskpart.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/diskpart.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/diskpart.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/diskpart.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diskpart

ディスク、ボリューム、およびパーティションマネージャ。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>。

- 管理者コマンドプロンプトでdiskpartを単独で実行し、コマンドラインを入力する:

`diskpart`

- 全てのディスクを一覧表示する:

`list disk`

- ボリュームを選択:

`select volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ボリューム</span>

- 選択したボリュームにドライブレターを割り当てる:

`assign letter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ドライブレター</span>

- 新しいパーティションを作成:

`create partition primary`

- 選択したボリュームを有効化:

`active`

- diskpartを終了する:

`exit`
