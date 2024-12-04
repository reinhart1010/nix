---
layout: page
title: common/zek (中文)
description: "从 XML 生成一个 Go 结构体。"
content_hash: 79e8839b19f93567f3ec164a6b4c1a9c7319f2c6
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zek.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zek.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zek.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zek

从 XML 生成一个 Go 结构体。
更多信息：<https://github.com/miku/zek>.

- 从 `stdin` 中给定的 XML 生成一个 Go 结构体，并将输出显示在 `stdout` 上：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.xml</span>` | zek`

- 从 `stdin` 中给定的 XML 生成一个 Go 结构体，并将输出发送到文件：

`curl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://url/to/xml</span>` | zek -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.go</span>

- 从 `stdin` 中给定的 XML 生成一个示例 Go 程序，并将输出发送到文件：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输入.xml</span>` | zek -p -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出.go</span>
