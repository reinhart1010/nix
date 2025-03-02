---
layout: page
title: linux/df (日本語)
description: "ファイルシステムのディスク使用量の概要を表示します。"
content_hash: 31fca398f99eff5191581b3d286afc52993380b2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

ファイルシステムのディスク使用量の概要を表示します。
もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html>。

- すべてのファイルシステムとそのディスク使用量を表示する:

`df`

- すべてのファイルシステムとそのディスク使用量を、人が解釈可能な形式で表示する:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--human-readable</span>

- 与えられたファイルまたはディレクトリを含むファイルシステムと、そのディスク使用量を表示する:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 空きinode数の統計を含める:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--inodes</span>

- ファイルシステムを表示するが、指定したタイプは除外する:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">squashfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-x|--exclude-type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs</span>

- ファイルシステムのタイプを表示する:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-T|--print-type</span>
