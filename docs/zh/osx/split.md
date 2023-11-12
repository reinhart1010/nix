---
layout: page
title: osx/split (中文)
description: "把一个文件拆分成几块。"
content_hash: 2ff59cbbbba9e43a9dd542fd8f4bea5a3102297a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/split.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># split

把一个文件拆分成几块。
更多信息：<https://ss64.com/osx/split.html>.

- 分割一个文件，每个分割部分有 10 行（除了最后一个）：

`split -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 用正则表达式拆分文件。匹配行将是下一个输出文件的第一行：

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 拆分一个文件，每个拆分中有 512 个字节（除了最后一个文件，使用 512K 表示 Kb，512M 表示 Mb）：

`split -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>
