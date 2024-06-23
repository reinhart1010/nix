---
layout: page
title: common/age (中文)
description: "一个简单、现代、安全的文件加密工具。"
content_hash: 6f720f1632213df625331d34e8718f0a80518377
last_modified_at: 2024-06-23
related_topics:
  - title: Deutsch version
    url: /de/common/age.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/age.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/age.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/age.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/age.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/age.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/age.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># age

一个简单、现代、安全的文件加密工具。
参见：`age-keygen` 用于生成密钥对。
更多信息：<https://github.com/FiloSottile/age>.

- 生成一个可以用密码短语（passphrase）解密的加密文件：

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已加密文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/未加密文件</span>

- 用一个或多个公钥加密一个文件，这些公钥以字面形式输入：

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">公钥</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已加密文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/未加密文件</span>

- 用收件人文件中指定的一个或多个公钥来加密一个文件：

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/收件人文件</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已加密文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/未加密文件</span>

- 用密码短语解密一个文件：

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已解密文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已加密文件</span>

- 用私钥文件解密一个文件：

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥文件</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已解密文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/已加密文件</span>
