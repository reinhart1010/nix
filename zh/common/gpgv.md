---
layout: page
title: common/gpgv (中文)
description: "验证 OpenPGP 签名。"
content_hash: d2c345d812dbbcae90a97670bc95a173953dc27c
related_topics:
  - title: English version
    url: /en/common/gpgv.html
    icon: bi bi-globe
---
# gpgv

验证 OpenPGP 签名。
更多信息：<https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- 验证签名文件：

`gpgv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 使用分离式签名验证已签名的文件：

`gpgv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/signature</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 在 keyrings 列表中添加一个文件（一个导出的钥匙也算作一个 keyring）：

`gpgv --keyring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/keyring_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/signature</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
