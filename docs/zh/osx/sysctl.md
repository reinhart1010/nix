---
layout: page
title: osx/sysctl (中文)
description: "访问内核状态信息。"
content_hash: ca63c5ff6c51c21c8c69885447c8b23af58b5215
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/sysctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sysctl

访问内核状态信息。
更多信息：<https://keith.github.io/xcode-man-pages/sysctl.8.html>.

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
