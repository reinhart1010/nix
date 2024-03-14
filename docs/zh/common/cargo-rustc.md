---
layout: page
title: common/cargo-rustc (中文)
description: "编译一个 Rust 包。类似于 `cargo build`，但您可以向编译器传递额外的选项。"
content_hash: 84d18131aca54d4fbedd6a3b8996aa62832f2c23
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-rustc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-rustc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-rustc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-rustc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo rustc

编译一个 Rust 包。类似于 `cargo build`，但您可以向编译器传递额外的选项。
查看 `rustc --help` 获取所有可用选项。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-rustc.html>.

- 构建包并向 `rustc` 传递选项：

`cargo rustc -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rustc_options</span>

- 在 release 模式下构建构建，启用优化：

`cargo rustc --release`

- 使用针对当前 CPU 的特定架构优化编译：

`cargo rustc --release -- -C target-cpu=native`

- 使用速度优化编译：

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|2|3</span>

- 使用 [s]ize 优化编译（`z` 也会关闭循环向量化）：

`cargo rustc -- -C opt-level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|z</span>

- 检查您的包是否使用了不安全的代码：

`cargo rustc --lib -- -D unsafe-code`

- 构建特定的包：

`cargo rustc --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>

- 仅构建指定的二进制文件：

`cargo --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
