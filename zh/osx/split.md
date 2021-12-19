---
layout: page
title: osx/split (中文)
description: "把一个文件拆分成几块。"
content_hash: ed41611bf8027cd6d9d1d43a260e79dabff94bad
related_topics:
  - title: English version
    url: /en/osx/split.html
    icon: bi bi-globe
---
# split

把一个文件拆分成几块。

- 分割一个文件，每个分割部分有 10 行（除了最后一个）：

`split -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 用正则表达式拆分文件。匹配行将是下一个输出文件的第一行：

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 拆分一个文件，每个拆分中有 512 个字节（除了最后一个文件，使用 512K 表示 Kb，512M 表示 Mb）：

`split -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>
