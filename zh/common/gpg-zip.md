---
layout: page
title: common/gpg-zip (中文)
description: "使用`GPG`加密存档中的文件和目录。"
content_hash: b2cd86289fae5734885039945f8e786d9946ed11
related_topics:
  - title: English version
    url: /en/common/gpg-zip.html
    icon: bi bi-globe
---
# gpg-zip

使用`GPG`加密存档中的文件和目录。
更多信息：<https://www.gnupg.org/documentation/manuals/gnupg/gpg_002dzip.html>.

- 使用密码将一个目录加密为`archive.gpg`：

`gpg-zip --symmetric --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.gpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 将`archive.gpg`解密到同名目录中：

`gpg-zip --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gpg</span>

- 列出加密的`archive.gpg`的内容：

`gpg-zip --list-archive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/archive.gpg</span>
