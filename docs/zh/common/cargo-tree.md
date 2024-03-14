---
layout: page
title: common/cargo-tree (中文)
description: "显示依赖图的树形可视化。"
content_hash: 30f4b72749d6b5dba4623f8cf64f685a57c8b403
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-tree.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-tree.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo tree

显示依赖图的树形可视化。
注意：在树中，标有 `(*)` 的包的依赖已在图的其他位置显示过，因此不会重复显示。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-tree.html>.

- 显示当前项目的依赖树：

`cargo tree`

- 仅显示到指定深度的依赖 (例如，当 `n` 为 1 时，仅显示直接依赖)：

`cargo tree --depth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- 在树中不显示给定的包（及其依赖)：

`cargo tree --prune `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_spec</span>

- 显示重复依赖的所有出现：

`cargo tree --no-dedupe`

- 仅显示 normal/build/dev 依赖：

`cargo tree --edges `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">normal|build|dev</span>
