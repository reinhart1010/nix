---
layout: page
title: common/gpg (中文)
description: "GNU Privacy Guard."
content_hash: 83957b22475c969183298ec83ca0e3328bd6415b
related_topics:
  - title: Deutsch version
    url: /de/common/gpg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gpg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/gpg.html
    icon: bi bi-globe
---
# gpg

GNU Privacy Guard.
请参阅`gpg2`了解 GNU Privacy Guard 2.
更多信息：<https://gnupg.org>.

- 不加密，仅对`doc.txt`进行签名（生成`doc.txt.asc`，格式为 ASCII 码形式）：

`gpg --clearsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- 对`doc.txt`进行签名并加密（生成`doc.txt.asc`，格式为 ASCII 码形式）：

`gpg --local-user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender_id</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">recipient_id</span>` --armor --sign --encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- 为接收者 alice@example.com 加密`doc.txt`（生成`doc.txt.gpg`）：

`gpg --encrypt --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- 只用密码加密`doc.txt`（生成`doc.txt.gpg`）：

`gpg --symmetric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt</span>

- 解密`doc.txt.gpg`（输出到标准输出）：

`gpg --decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">doc.txt.gpg</span>

- 导入一个公钥：

`gpg --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">public.gpg</span>

- 导出 alice@example.com 的公钥（输出到标准输出）：

`gpg --export --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>

- 导出 alice@example.com 的私钥（输出到标准输出）：

`gpg --export-secret-keys --armor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice@example.com</span>
