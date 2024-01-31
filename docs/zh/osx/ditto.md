---
layout: page
title: osx/ditto (中文)
description: "复制文件和目录。"
content_hash: 9c1002fcaccf75b2c18892a012778a9b16f3d107
last_modified_at: 2024-01-31
related_topics:
  - title: বাংলা version
    url: /bn/osx/ditto.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/ditto.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/ditto.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ditto

复制文件和目录。
更多信息：<https://keith.github.io/xcode-man-pages/ditto.1.html>.

- 用源目录的内容覆盖目标目录的内容：

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件路径</span>

- 为复制的每个文件打印一行到终端窗口：

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件路径</span>

- 复制给定的文件或目录，同时保留原始文件权限：

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件路径</span>
