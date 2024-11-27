---
layout: page
title: common/ansible-galaxy (中文)
description: "执行与 Ansible 角色和集合相关的各种操作。"
content_hash: dc6e3beecf23382310bf8b682101f20380ae52c8
last_modified_at: 2024-11-27
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
  - title: Indonesia version
    url: /id/common/ansible-galaxy.html
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

执行与 Ansible 角色和集合相关的各种操作。
更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-galaxy.html>.

- 列出已安装的角色或集合：

`ansible-galaxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role|collection</span>` list`

- 使用不同的详细等级搜索角色（`-v` 应该放在最后）：

`ansible-galaxy role search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键字</span>` -v`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vvvvv</span>

- 安装或移除角色：

`ansible-galaxy role `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">角色名称1 角色名称2 ...</span>

- 创建一个新角色：

`ansible-galaxy role init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">角色名称</span>

- 获取关于角色的信息：

`ansible-galaxy role info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">角色名称</span>

- 安装或移除集合：

`ansible-galaxy collection `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|remove</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">集合名称1 集合名称2 ...</span>

- 显示关于角色或集合的帮助信息：

`ansible-galaxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role|collection</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
