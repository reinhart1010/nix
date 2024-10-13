---
layout: page
title: common/behat (中文)
description: "基于 Behaviour-Driven Development 的自动化测试 PHP 框架。"
content_hash: 7da6e89e549c78426acc3f3ed6bf4ad9174ed984
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/behat.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/behat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/behat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# behat

基于 Behaviour-Driven Development 的自动化测试 PHP 框架。
更多信息：<https://behat.org>.

- 初始化一个 PHP behat 项目：

`behat --init`

- 运行所有测试：

`behat`

- 运行指定组所有的测试用例：

`behat --suite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">组名</span>

- 运行所有测试，指定输入格式：

`behat --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pretty|progress</span>

- 将测试结果输出到指定文件：

`behat --out `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 展示测试组所在的目录清单：

`behat --definitions`
