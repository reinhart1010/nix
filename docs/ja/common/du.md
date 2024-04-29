---
layout: page
title: common/du (日本語)
description: "ディスク使用状況: ファイルとディレクトリの使用量の概算を表示します。"
content_hash: e07f716cc1f84da631147fe16adb4562b65e14ab
last_modified_at: 2024-04-29
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># du

ディスク使用状況: ファイルとディレクトリの使用量の概算を表示します。
詳しくはこちら: <https://www.gnu.org/software/coreutils/du>

- 指定した単位 (B/KiB/MiB) でディレクトリおよびサブディレクトリのサイズを表示します:

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>

- 人間にとって解釈しやすい形式(サイズに応じた単位の選択など)で、ディレクトリおよびサブディレクトリのサイズを表示します:

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>

- 人間にとって解釈しやすい形式で、単一ディレクトリのサイズを表示します:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>

- 人間にとって解釈しやすい形式で、指定ディレクトリ、そのサブディレクトリ、それらに含まれる全てのファイルのサイズを表示します:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>

- 人間にとって解釈しやすい形式で、指定ディレクトリおよび N 階層先までのディレクトリのサイズを表示します:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリパス</span>

- 人間にとって解釈しやすい形式で、現在のディレクトリおよびその下のディレクトリに含まれる全ての `.jpg` ファイルサイズを表示し、最後に合計を表示します:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>
