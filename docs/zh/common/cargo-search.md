---
layout: page
title: common/cargo-search (中文)
description: "在 https://crates.io 上搜索包。"
content_hash: 55ecf61ce15c97d243bc4ac5d197d7715e77fc3f
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-search.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo search

在 https://crates.io 上搜索包。
显示包及其描述，以 TOML 格式显示，可复制到 `Cargo.toml` 中。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-search.html>.

- 搜索包：

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询词</span>

- 显示 n 个结果 (默认为 10，最多为 100)：

`cargo search --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询词</span>
