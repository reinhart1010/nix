---
layout: page
title: osx/sysctl (中文)
description: "访问内核状态信息。"
content_hash: 99dc30a82e50e29711b86274a1fa9b0571970af8
related_topics:
  - title: English version
    url: /en/osx/sysctl.html
    icon: bi bi-globe
---
# sysctl

访问内核状态信息。
更多信息：<https://ss64.com/osx/sysctl.html>.

- 显示所有可用变量及其值：

`sysctl -a`

- 显示 Apple 型号标识符：

`sysctl -n hw.model`

- 显示 CPU 模型：

`sysctl -n machdep.cpu.brand_string`

- 显示可用的 CPU 功能（MMX, SSE, SSE2, SSE3, AES, 等）：

`sysctl -n machdep.cpu.features`

- 设置一个可更改的内核状态变量：

`sysctl -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">部分。可修改的变量</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>
