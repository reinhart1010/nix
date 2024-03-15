---
layout: page
title: common/cargo-add (中文)
description: "向 Rust 项目的 `Cargo.toml` 文件添加依赖项。"
content_hash: a2824d8a582a2c031e3b6c9d9228bd89eb369771
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo add

向 Rust 项目的 `Cargo.toml` 文件添加依赖项。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-add.html>.

- 将最新版本的依赖项添加到当前项目：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>

- 添加特定版本的依赖项：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 添加依赖项并启动一个或多个特定功能：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>` --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">功能1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">功能2</span>

- 添加一个可选的依赖项，然后将其作为包(crate)的一个功能暴露出来：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>` --optional`

- 将本地包(crate)添加为依赖项：

`cargo add --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 添加一个开发或构建依赖项：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>

- 添加一个禁用所有默认功能的依赖项：

`cargo add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>` --no-default-features`
