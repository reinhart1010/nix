---
layout: page
title: common/cargo-fmt (中文)
description: "在 Rust 项目中对所有源文件运行 `rustfmt`。"
content_hash: e178f93b6fd88c85ab8809e26275c5dee5603b07
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-fmt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-fmt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo fmt

在 Rust 项目中对所有源文件运行 `rustfmt`。
更多信息：<https://github.com/rust-lang/rustfmt>.

- 格式化所有源文件：

`cargo fmt`

- 检查格式错误，不对文件进行写入操作：

`cargo fmt --check`

- 将参数传递给每个 rustfmt 调用：

`cargo fmt -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustfmt参数</span>
