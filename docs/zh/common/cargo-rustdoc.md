---
layout: page
title: common/cargo-rustdoc (中文)
description: "构建 Rust 包的文档。"
content_hash: d36cc1c1166471b5b001b70bc3497c8c16bb08d4
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-rustdoc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo rustdoc

构建 Rust 包的文档。
类似于 `cargo doc`，但您可以向 `rustdoc` 传递选项。查看 `rustdoc --help` 获取所有可用选项。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html>.

- 向 `rustdoc` 传递选项：

`cargo rustdoc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustdoc_options</span>

- 关于文档 lint 发出警告：

`cargo rustdoc -- --warn rustdoc::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lint_name</span>

- 忽略文档 lint:

`cargo rustdoc -- --allow rustdoc::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lint_name</span>

- 为包的库生成文档：

`cargo rustdoc --lib`

- 为指定的二进制文件生成文档：

`cargo rustdoc --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 为指定的示例生成文档：

`cargo rustdoc --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 为指定的集成测试生成文档：

`cargo rustdoc --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
