---
layout: page
title: common/qrencode (中文)
description: "二维码生成器。支持 PNG 和 EPS 格式。"
content_hash: 33e4ef7ab0839904b65b4820d050e76a93cdcba9
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/qrencode.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qrencode.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/qrencode.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># qrencode

二维码生成器。支持 PNG 和 EPS 格式。
更多信息：<https://fukuchi.org/works/qrencode>.

- 将字符串转换为二维码并保存到输出文件：

`qrencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 将输入文件转换为二维码并保存到输出文件：

`qrencode -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件.png</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入文件</span>

- 将字符串转换为二维码并在终端中打印：

`qrencode -t ansiutf8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 从管道输入转换为二维码并在终端中打印：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>` | qrencode -t ansiutf8`
