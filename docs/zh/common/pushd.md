---
layout: page
title: common/pushd (中文)
description: "将目录放在堆栈上，以便以后访问。"
content_hash: 07286754714120c4db6f06241a6eaa6e7bc32bb8
last_modified_at: 2023-10-26
related_topics:
  - title: dansk version
    url: /da/common/pushd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pushd.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pushd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pushd

将目录放在堆栈上，以便以后访问。
另请参阅 `popd` 命令说明，以切换回原始目录。

- 切换到目录并将其添加到堆栈上：

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- 切换堆栈上的第一个和第二个目录：

`pushd`

- 通过使第 5 个元素成为堆栈的顶部来旋转堆栈：

`pushd +4`
