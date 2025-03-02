---
layout: page
title: common/yacas (中文)
description: "另一个计算机代数系统。"
content_hash: 6e2b275ca7a9376d610876ec72036b34de7ac0ef
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yacas.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yacas.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yacas

另一个计算机代数系统。
更多信息：<https://www.yacas.org>.

- 启动交互式的 `yacas` 会话：

`yacas`

- 在 `yacas` 会话中，执行一个语句：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Integrate(x)Cos(x)</span>`;`

- 在 `yacas` 会话中，显示一个示例：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Example()</span>`;`

- 从 `yacas` 会话中退出：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">quit</span>

- 执行一个或多个 `yacas` 脚本（没有终端或提示符），然后退出：

`yacas -p -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本2</span>

- 执行并打印一个语句的结果，然后退出：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Echo( Deriv(x)Cos(1/x) );</span>`" | yacas -p -c /dev/stdin`
