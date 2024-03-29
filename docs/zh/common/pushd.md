---
layout: page
title: common/pushd (中文)
description: "将目录放在堆栈上，以便以后访问。"
content_hash: da6148d499bf1981ce377d33c78c902bd47ddfda
last_modified_at: 2023-11-12
related_topics:
  - title: dansk version
    url: /da/common/pushd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pushd.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pushd

将目录放在堆栈上，以便以后访问。
另请参阅 `popd` 命令说明，以切换回原始目录。
更多信息：<https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- 切换到目录并将其添加到堆栈上：

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directory</span>

- 切换堆栈上的第一个和第二个目录：

`pushd`

- 通过使第 5 个元素成为堆栈的顶部来旋转堆栈：

`pushd +4`
