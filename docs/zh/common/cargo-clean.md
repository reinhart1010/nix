---
layout: page
title: common/cargo-clean (中文)
description: "删除 `target` 目录中生成的构建产物。"
content_hash: 019e64354e2c9a6d840bf157da4417e1c43142a7
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-clean.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo clean

删除 `target` 目录中生成的构建产物。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-clean.html>.

- 删除整个 `target` 目录：

`cargo clean`

- 删除文档构建产物 (`target/doc` 目录)：

`cargo clean --doc`

- 删除 release 模式的构建产物 (`target/release` 目录)：

`cargo clean --release`

- 删除给定配置文件的目录中的构建产物（在本例中为 `target/debug`)：

`cargo clean --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev</span>
