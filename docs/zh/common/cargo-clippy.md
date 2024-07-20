---
layout: page
title: common/cargo-clippy (中文)
description: "一系列 lint 工具，用于捕获常见错误并改进 Rust 代码。"
content_hash: 8ac4471b54c90e23348369e7bb1ed47e56797233
last_modified_at: 2024-07-20
related_topics:
  - title: English version
    url: /en/common/cargo-clippy.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-clippy.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-clippy.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cargo clippy

一系列 lint 工具，用于捕获常见错误并改进 Rust 代码。
更多信息：<https://github.com/rust-lang/rust-clippy>.

- 对当前目录中的代码运行检查：

`cargo clippy`

- 要求 `Cargo.lock` 文件是最新的：

`cargo clippy --locked`

- 对工作区中的所有包进行检查：

`cargo clippy --workspace`

- 对某个包进行检查：

`cargo clippy --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 将警告视为错误：

`cargo clippy -- --deny warnings`

- 运行检查并忽略警告：

`cargo clippy -- --allow warnings`

- 自动应用 Clippy 的建议：

`cargo clippy --fix`
