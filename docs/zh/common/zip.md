---
layout: page
title: common/zip (中文)
description: "将文件打包并压缩（存档）为 zip 文件。"
content_hash: 73202f94ea9b4574f8793a8f563bfd0b6601fbe1
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/zip.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/zip.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># zip

将文件打包并压缩（存档）为 zip 文件。
更多信息：<https://manned.org/zip>.

- 递归地打包和压缩文件和目录：

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录2</span>

- 添加到压缩档案中并排除不需要的文件：

`zip -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/不需要的文件</span>

- 使用最高压缩级别 9 压缩目录和内容：

`zip -r -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 创建一个加密压缩档案（将会提示输入密码）：

`zip -e -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 将文件添加到现有的 zip 文件：

`zip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 从现有 zip 文件中删除文件：

`zip -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo/*.tmp</span>`"`

- 将指定目录及其内容打包并拆分为多个 zip 文件（例如：若干个 3 GB 的 zip 包）：

`zip -r -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 列出指定压缩档案中的文件（不提取文件）：

`zip -sf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">压缩文件.zip</span>
