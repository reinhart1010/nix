---
layout: page
title: linux/tmt-try (中文)
description: "测试及环境快速上手。"
content_hash: 36ef230987ea058670b9173c22a3877dc9630456
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/linux/tmt-try.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tmt try

测试及环境快速上手。
更多信息：<https://tmt.readthedocs.io/en/stable/stories/cli.html#try>.

- 快速尝试默认的测试环境配置方法（当前工作目录中没有测试）：

`tmt try`

- 在当前的工作目录中运行一个测试：

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/test</span>` && tmt try`

- 使用特定的操作系统：

`tmt try `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora-41</span>

- 选择定制的镜像和测试环境配置方法：

`tmt try `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fedora@container</span>

- 根据定制的筛选条件选择测试：

`tmt try --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature</span>

- 配置客户机并等待用户输入指令：

`tmt try --ask`

- 直接登录到客户机：

`tmt try --login`

- 显示帮助：

`tmt try --help`
