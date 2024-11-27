---
layout: page
title: common/cp (中文)
description: "复制文件和目录。"
content_hash: 09397be94d2f9df9947ae228373f530a411fb968
last_modified_at: 2024-11-27
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

复制文件和目录。
更多信息：<https://www.gnu.org/software/coreutils/cp>.

- 将文件复制到另一个位置：

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源_文件.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标文件.ext</span>

- 将文件复制到另一个文件夹，并保留原来的文件名：

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标的目录</span>

- 以递归方式将文件夹内的内容复制到另一个位置（如果目标文件夹存在，则将此文件夹复制到目标文件夹中）：

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 以详细模式递归复制目录（在复制文件时显示文件信息）：

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>

- 一次将多个文件复制到一个目录：

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标_目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>

- 以交互方式将文本文件复制到另一个位置（覆盖之前会提示用户）：

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标_目录</span>

- 复制之前遵循符号链接：

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">链接</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标_目录</span>

- 使用第一个参数作为目标目录（对于 `xargs ... | cp -t <目标_目录>` 这样的命令非常有用）：

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目标目录</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件或目录1 路径/到/文件或目录2 ...</span>
