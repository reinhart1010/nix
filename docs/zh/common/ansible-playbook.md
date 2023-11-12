---
layout: page
title: common/ansible-playbook (中文)
description: "通过 SSH 协议在远程计算机上执行 playbook 中定义的任务。"
content_hash: c737634cbc6a8b117741b56ec44609c2b5889cac
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ansible-playbook.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ansible-playbook.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ansible-playbook.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ansible-playbook.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ansible-playbook.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ansible-playbook

通过 SSH 协议在远程计算机上执行 playbook 中定义的任务。
更多信息：<https://docs.ansible.com/ansible/latest/cli/ansible-playbook.html>.

- 执行 playbook 中的任务：

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>

- 在给定的主机清单文件中执行 playbook 中的命令：

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">清单文件</span>

- 通过定义在命令行中额外的变量执行 playbook 中的任务：

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量 1</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值 1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量 2</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值 2</span>`"`

- 通过定义在一个 json 格式的文件中额外的变量执行 playbook 中的任务：

`ansible-playbook `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">playbook</span>` -e "@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variables.json</span>`"`
