---
layout: page
title: common/nload (中文)
description: "在终端中可视化查看网络流量。"
content_hash: bc39e3d5fc78e97353a6eeb00d80d4702f0d852c
last_modified_at: 2024-07-14
related_topics:
  - title: English version
    url: /en/common/nload.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nload.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nload

在终端中可视化查看网络流量。
更多信息： <https://github.com/rolandriegel/nload>.

- 查看所有网络接口的流量（使用方向键切换不同网口）：

`nload`

- 查看指定网络接口的流量（使用方向键切换网口）：

`nload devices `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网口1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">网口2</span>
