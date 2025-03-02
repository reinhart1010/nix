---
layout: page
title: common/jc (中文)
description: "将多个命令的输出转换为 JSON。"
content_hash: e2ee147d782dd8da18bd30e52602a3ab0bc80079
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jc

将多个命令的输出转换为 JSON。
更多信息：<https://github.com/kellyjonbrazil/jc>.

- 通过管道将命令输出转换为 JSON：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>

- 通过魔术语法将命令输出转换为 JSON：

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>

- 通过管道输出格式化的 JSON：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>` -p`

- 通过魔术语法输出格式化的 JSON：

`jc -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>
