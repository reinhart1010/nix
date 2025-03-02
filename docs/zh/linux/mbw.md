---
layout: page
title: linux/mbw (中文)
description: "内存带宽性能测试工具。"
content_hash: b80f1247f857f0655edd54c3a7c25f93bf77fb10
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/mbw.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mbw

内存带宽性能测试工具。
更多信息：<https://github.com/raas/mbw>.

- 以 512MB 大小运行 3 次内存带宽测试：

`mbw -n 3 512`

- 以 512MB 大小运行 3 次内存带宽测试，仅输出统计信息，不显示平均值：

`mbw -n 3 -q -a 512`

- 以 512MB 大小运行 3 次内存复制测试，仅输出统计信息：

`mbw -n 3 -q -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` 512`

- 用 1024字节 的块运行10次内存块复制测试，分配 8192MB 内存：

`mbw -n 10 -q -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -b 1024 8192`

- 持续 2048MB 大小运行内存字符串复制测试，仅输出统计信息：

`mbw -n 0 -t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -q 2048`
