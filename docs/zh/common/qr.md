---
layout: page
title: common/qr (中文)
description: "在终端中使用 ANSI VT-100 转义代码生成二维码。"
content_hash: 676c52a88d98405d604fb47a9118e9ab43926643
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/qr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qr.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qr.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qr

在终端中使用 ANSI VT-100 转义代码生成二维码。
更多信息：<https://github.com/lincolnloop/python-qrcode/>.

- 生成一个二维码：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据</span>`" | qr`

- 指定错误纠正等级（默认为 M）：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数据</span>`" | qr --error-correction=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">L|M|Q|H</span>
