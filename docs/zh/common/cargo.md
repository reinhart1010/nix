---
layout: page
title: common/cargo (中文)
description: "管理 Rust 项目及其模块依赖项（crates）。"
content_hash: da3629a087626cf15b61efce1bcf71166719e019
last_modified_at: 2024-03-14
related_topics:
  - title: Deutsch version
    url: /de/common/cargo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cargo.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cargo.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cargo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cargo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cargo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/cargo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo

管理 Rust 项目及其模块依赖项（crates）。
一些子命令，如 `build`，具有自己的用法文档。
更多信息：<https://doc.rust-lang.org/cargo>.

- 搜索包：

`cargo search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索关键词</span>

- 下载二进制包（crate)：

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 列出已安装的二进制包（crate)：

`cargo install --list`

- 在指定目录 （或默认情况下在当前工作目录) 中创建一个新的二进制或库 Rust项目：

`cargo init --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bin|lib</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 向当前目录的 `Cargo.toml` 添加一个依赖：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项目</span>

- 使用 release 模式在当前目录中构建 Rust 项目：

`cargo build --release`

- 使用最新的编译器在当前目录中构建 Rust 项目 （需要 `rustup`)：

`cargo +nightly build`

- 使用特定数量的线程构建 （默认为逻辑 CPU 的数量)：

`cargo build --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">线程数</span>
