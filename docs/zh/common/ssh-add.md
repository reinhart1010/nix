---
layout: page
title: common/ssh-add (中文)
description: "在 ssh 代理中管理加载的 ssh 密钥。"
content_hash: 9892aa2d43a2bd232b2323e0674f460b70690b55
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ssh-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-add

在 ssh 代理中管理加载的 ssh 密钥。
需要确保 ssh 代理已启动并正在运行以加载其中的密钥。
更多信息：<https://man.openbsd.org/ssh-add>.

- 将 `~/.ssh` 中的默认 SSH 密钥添加到 SSH 代理：

`ssh-add`

- 向 ssh 代理添加指定密钥：

`ssh-add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥文件</span>

- 列出当前加载的密钥的指纹：

`ssh-add -l`

- 从 ssh 代理中删除密钥：

`ssh-add -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥文件</span>

- 从 ssh 代理中删除所有当前已有的密钥：

`ssh-add -D`

- 向 ssh 代理和密钥链添加密钥：

`ssh-add -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥文件</span>
