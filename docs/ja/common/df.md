---
layout: page
title: common/df (日本語)
description: "ファイルシステムのディスク使用量の概要を表示します。"
content_hash: a3e0550288136d38757fa0bbb203cc17fc14263d
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/df.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/df.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/df.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/df.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/df.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/df.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/df.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/df.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/df.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/df.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/df.html
    icon: bi bi-globe
tldri18n_status: 2
---
# df

ファイルシステムのディスク使用量の概要を表示します。
もっと詳しく: <https://manned.org/df.1posix>。

- 512バイト単位で全てのファイルシステムとそのディスク使用量を表示する:

`df`

- 指定したファイルまたはディレクトリを含むファイルシステムとそのディスク使用量を表示する:

`df `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file_or_directory</span>

- 1024バイト単位で表示する:

`df -k`

- 移植性のある方法で情報を表示する:

`df -P`
