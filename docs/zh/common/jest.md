---
layout: page
title: common/jest (中文)
description: "一个零配置的 JavaScript 测试平台。"
content_hash: 447b65a5ddef56f0514d3d8ca3168ce7bea51bed
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jest

一个零配置的 JavaScript 测试平台。
更多信息：<https://jestjs.io>.

- 运行所有可用的测试：

`jest`

- 从指定文件中运行测试套件：

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件1 路径/到/文件2 ...</span>

- 从当前目录和子目录中路径匹配给定正则表达式的文件运行测试套件：

`jest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式2</span>

- 运行名称匹配给定正则表达式的测试：

`jest --testNamePattern `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正则表达式</span>

- 运行与给定源文件相关的测试套件：

`jest --findRelatedTests `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/源文件.js</span>

- 运行与所有未提交文件相关的测试套件：

`jest --onlyChanged`

- 监视文件更改并自动重新运行相关测试：

`jest --watch`

- 显示帮助信息：

`jest --help`
