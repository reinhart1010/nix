---
layout: page
title: common/du (日本語)
description: "ディスク使用状況: ファイルとディレクトリの使用量の概算を表示します。"
content_hash: e611d29f782ec2d65a5d5fd2ea34f80336208f2c
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
---
# du

ディスク使用状況: ファイルとディレクトリの使用量の概算を表示します。
詳しくはこちら: <https://www.gnu.org/software/coreutils/du>

- 指定した単位 (B/KiB/MiB) でディレクトリおよびサブディレクトリのサイズを表示します:

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 人間にとって解釈しやすい形式(サイズに応じた単位の選択など)で、ディレクトリおよびサブディレクトリのサイズを表示します:

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 人間にとって解釈しやすい形式で、単一ディレクトリのサイズを表示します:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 人間にとって解釈しやすい形式で、指定ディレクトリ、そのサブディレクトリ、それらに含まれる全てのファイルのサイズを表示します:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 人間にとって解釈しやすい形式で、指定ディレクトリおよび N 階層先までのディレクトリのサイズを表示します:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 人間にとって解釈しやすい形式で、現在のディレクトリおよびその下のディレクトリに含まれる全ての `.jpg` ファイルサイズを表示し、最後に合計を表示します:

`du -ch */*.jpg`
