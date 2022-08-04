---
layout: page
title: common/gpg2 (中文)
description: "GNU Privacy Guard 2."
content_hash: 7ee54c33b8958c94ee01df01838d9624df16c276
related_topics:
  - title: Deutsch version
    url: /de/common/gpg2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg2.html
    icon: bi bi-globe
---
# gpg2

GNU Privacy Guard 2.
GNU Privacy Guard 1 请参见`gpg`.
更多信息：<https://docs.releng.linuxfoundation.org/en/latest/gpg.html>.

- 列出导入的密钥（公钥）：

`gpg2 --list-keys`

- 为指定的接收者加密指定的文件，将输出结果写到一个新的文件中，并附加 `.gpg`：

`gpg2 --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt</span>

- 只用密码（对称加密）对指定文件进行加密，将输出结果写入一个附加`.gpg`的新文件：

`gpg2 --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt</span>

- 解密指定的文件，并将结果写入标准输出：

`gpg2 --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/doc.txt.gpg</span>

- 导入一个公钥：

`gpg2 --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/public_key.gpg</span>

- 将指定电子邮件地址的公钥导出到标准输出：

`gpg2 --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- 将指定电子邮件地址的私钥导出到标准输出：

`gpg2 --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
