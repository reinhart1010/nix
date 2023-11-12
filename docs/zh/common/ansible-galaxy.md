---
layout: page
title: common/ansible-galaxy (中文)
description: "创建和管理 Ansible 角色。"
content_hash: 35896ca586cc3c02570a8e7a911bf5164ec1c3d2
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-galaxy.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-galaxy.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-galaxy

创建和管理 Ansible 角色。
更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- 安装一个角色：

`ansible-galaxy install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名.角色名</span>

- 移除一个角色：

`ansible-galaxy remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名.角色名</span>

- 列出已安装的角色：

`ansible-galaxy list`

- 搜索一个指定的角色：

`ansible-galaxy search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">角色名</span>

- 创建一个新的角色：

`ansible-galaxy init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">角色名</span>
