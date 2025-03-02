---
layout: page
title: common/ya (中文)
description: "管理 Yazi 软件包和插件。"
content_hash: a006cd0676409761746d3bfa6ff91dfefe66d35f
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/ya.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ya.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ya.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ya

管理 Yazi 软件包和插件。
更多信息：<https://github.com/sxyazi/yazi>.

- 添加一个软件包：

`ya pack -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 升级所有软件包：

`ya pack -u`

- 订阅来自所有远程实例的消息：

`ya sub `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">种类</span>

- 向当前实例发布一个字符串内容的消息：

`ya pub --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串消息</span>

- 向当前实例发布一个 JSON 内容的消息：

`ya pub --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json消息</span>

- 向指定实例发布一个字符串内容的消息：

`ya pub-to --str `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">消息</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">接收者</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">种类</span>
