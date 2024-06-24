---
layout: page
title: common/a2ping (中文)
description: "将图像转换为 EPS 或 PDF 文件。"
content_hash: 47f5dfa87d942d2838bf81e03bfceabc995bb5ae
last_modified_at: 2024-06-24
related_topics:
  - title: বাংলা version
    url: /bn/common/a2ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/a2ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/a2ping.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/a2ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/a2ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/a2ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/a2ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2ping

将图像转换为 EPS 或 PDF 文件。
更多信息：<https://manned.org/a2ping>.

- 将图像转换为 PDF（注意：指定输出文件名是可选的）：

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图像文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">输出PDF文件</span>

- 使用指定的方法压缩文档：

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 如果存在，则扫描 HiResBoundingBox（默认为是）：

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 允许页面内容位于原点的下方和左侧（默认为否）：

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 将额外的参数传递给 `gs`：

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 将额外的参数传递给外部程序（如 `pdftops`）：

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">参数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件</span>

- 显示帮助信息：

`a2ping -h`
