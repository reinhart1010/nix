---
layout: page
title: common/zmv (中文)
description: "移动或重命名符合指定扩展模式的文件。"
content_hash: 28ca41cc7b3d106a264df4111f36cdbb8545abb7
last_modified_at: 2024-12-04
related_topics:
  - title: English version
    url: /en/common/zmv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zmv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zmv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zmv

移动或重命名符合指定扩展模式的文件。
请参阅：`zcp` 和 `zln`。
更多信息：<https://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- 使用类似正则表达式的模式移动文件：

`zmv '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- 预览移动结果，但不进行任何实际更改：

`zmv -n '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- 交互式移动文件，在每次更改之前进行提示：

`zmv -i '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`

- 在执行时详细打印每个操作：

`zmv -v '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">(*).log</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$1.txt</span>`'`
