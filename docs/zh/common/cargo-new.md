---
layout: page
title: common/cargo-new (中文)
description: "创建一个新的 Cargo 包。"
content_hash: 77c9a305a7d460f2116630c6b35d84993eeaa591
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-new.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-new.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo new

创建一个新的 Cargo 包。
相当于 `cargo init`，但是需要指定一个目录。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-new.html>.

- 使用二进制目标创建一个新的 Rust 项目：

`cargo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>
