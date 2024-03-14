---
layout: page
title: common/cargo-uninstall (中文)
description: "移除使用 `cargo install` 安装的 Rust 二进制文件。"
content_hash: ae5313009fea13dfeece2f8b9500ac3d1bdc099e
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-uninstall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-uninstall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo uninstall

移除使用 `cargo install` 安装的 Rust 二进制文件。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-uninstall.html>.

- 移除一个已安装的二进制文件：

`cargo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_spec</span>
