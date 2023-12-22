---
layout: page
title: common/firefox (中文)
description: "一个自由、开源的网络浏览器。"
content_hash: a23c8681409b6d76ca8d268705fc39c7cb9f790b
last_modified_at: 2023-12-22
related_topics:
  - title: Deutsch version
    url: /de/common/firefox.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/firefox.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/firefox.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/firefox.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># firefox

一个自由、开源的网络浏览器。
更多信息：<https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- 启动 Firefox 并打开网页：

`firefox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- 打开新窗口：

`firefox --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- 打开隐私（隐身）窗口：

`firefox --private-window`

- 使用默认搜索引擎搜索“wikipedia”：

`firefox --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wikipedia</span>`"`

- 在安全模式中启动 Firefox, 所有扩展会被禁用：

`firefox --safe-mode`

- 在无头模式中截取网页截屏：

`firefox --headless --screenshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/输出文件.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- 使用特定的配置文件允许多个单独的 Firefox 实例同时运行：

`firefox --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件夹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- 设置 Firefox 为默认浏览器：

`firefox --setDefaultBrowser`
