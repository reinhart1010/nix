---
layout: page
title: osx/ditto (中文)
description: "复制文件和目录。"
content_hash: aa1b6a28bf505fce99022a4f40b3cefceef5084d
last_modified_at: 2023-11-12
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
更多信息：<https://ss64.com/osx/ditto.html>.

- 用源目录的内容覆盖目标目录的内容：

`ditto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件路径</span>

- 为复制的每个文件打印一行到终端窗口：

`ditto -V `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件路径</span>

- 复制给定的文件或目录，同时保留原始文件权限：

`ditto -rsrc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">源文件路径</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标文件路径</span>
