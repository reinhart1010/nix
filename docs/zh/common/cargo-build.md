---
layout: page
title: common/cargo-build (中文)
description: "编译本地包及其所有依赖项。"
content_hash: 527e1e8041e2028ae466cf58fd142cc674b6fd0d
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-build.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-build.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-build.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo build

编译本地包及其所有依赖项。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-build.html>.

- 在本地路径中构建由 `Cargo.toml` 清单文件定义的一个或多个包：

`cargo build`

- 以 release 模式构建，并进行优化：

`cargo build --release`

- 要求 `Cargo.lock` 文件为最新版本：

`cargo build --locked`

- 构建工作区中的所有包：

`cargo build --workspace`

- 构建特定的包：

`cargo build --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 仅构建指定的二进制文件：

`cargo build --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 仅构建指定的测试目标：

`cargo build --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">测试名称</span>
