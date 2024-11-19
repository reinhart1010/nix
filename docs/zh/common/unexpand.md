---
layout: page
title: common/unexpand (中文)
description: "将空格转换为制表符。"
content_hash: 3c4ebeac12ed049f1f264e161376c2a5ea1f92b6
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/unexpand.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/unexpand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/unexpand.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/unexpand.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># unexpand

将空格转换为制表符。
更多信息：<https://www.gnu.org/software/coreutils/unexpand>.

- 将每个文件中的空格转换为制表符，并写入到 `stdout`：

`unexpand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将空格转换为制表符，从 `stdout` 读取：

`unexpand`

- 转换所有空格，而不仅仅是开头的空格：

`unexpand -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 仅转换开头的空格序列（覆盖 -a）：

`unexpand --first-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>

- 将制表符间隔设置为某个字符数，而不是 8（启用 -a）：

`unexpand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数量</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
