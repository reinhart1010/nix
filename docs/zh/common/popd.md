---
layout: page
title: common/popd (中文)
description: "通过 pushd shell 内置程序删除目录堆栈中的目录。"
content_hash: d8c8f87f3e283e774793b573db31cb9af4b9c8b1
last_modified_at: 2023-10-26
related_topics:
  - title: dansk version
    url: /da/common/popd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/popd.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/popd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># popd

通过 pushd shell 内置程序删除目录堆栈中的目录。

- 从堆栈中删除顶部目录，并用 `cd` 跳转到该目录：

`popd`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表左侧开始）：

`popd +N`

- 删除第 n 个目录（从零开始，以用 `dirs` 打印的列表右侧开始）：

`popd -N`
