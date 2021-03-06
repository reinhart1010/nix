---
layout: page
title: common/cat (中文)
description: "打印和拼接文件的工具。"
content_hash: 61111cf1bdf84df9ec08876d5ea01c8ad1c39224
related_topics:
  - title: Deutsch version
    url: /de/common/cat.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cat.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cat.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cat.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cat.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cat.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cat.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/cat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cat.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/cat.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cat.html
    icon: bi bi-globe
---
# cat

打印和拼接文件的工具。
更多信息：<https://www.gnu.org/software/coreutils/cat>.

- 以标准输出，打印文件内容：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- 多文件合并到目标文件：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_file</span>

- 多文件合并，并追加到目标文件：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` >> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target_file</span>

- 显示行号：

`cat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- 显示不可打印和空白的字符（使用 `M-` 前缀标记非 ASCII 字符）：

`cat -v -t -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
