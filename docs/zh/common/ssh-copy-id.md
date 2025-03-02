---
layout: page
title: common/ssh-copy-id (中文)
description: "在远程机器的 authorized_keys 中安装您的公钥。"
content_hash: 1769ed5cd723b0da66af799bde98cd2b7ba2ec7e
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh-copy-id.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-copy-id.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-copy-id

在远程机器的 authorized_keys 中安装您的公钥。
更多信息：<https://manned.org/ssh-copy-id>.

- 将您的密钥复制到远程主机：

`ssh-copy-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机</span>

- 将给定的公钥文件复制到远程主机：

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/公钥文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机</span>

- 将给定的公钥文件通过特定端口复制到远程主机：

`ssh-copy-id -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/公钥文件</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机</span>
