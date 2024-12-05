---
layout: page
title: common/zip2john (中文)
description: "从 Zip 压缩文件中提取密码哈希，供 John the Ripper 密码破解程序使用。"
content_hash: 3321a1b82ed23d871e2324fac088ecd3c852cfed
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zip2john.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zip2john.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zip2john

从 Zip 压缩文件中提取密码哈希，供 John the Ripper 密码破解程序使用。
这是一个通常作为 John the Ripper 安装的一部分安装的实用工具。
更多信息：<https://www.openwall.com/john/>.

- 从一个压缩文件中提取密码哈希，列出压缩文件中的所有文件：

`zip2john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>

- 仅使用特定压缩文件提取密码哈希：

`zip2john -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩_文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>

- 从压缩文件中提取密码哈希到一个特定文件（供 John the Ripper 使用）：

`zip2john -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/压缩_文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.zip</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.hash</span>
