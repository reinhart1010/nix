---
layout: page
title: common/cargo-init (中文)
description: "创建一个新的 Cargo 包。"
content_hash: 8ea705b60f499b67734219a3610fee135507e715
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo init

创建一个新的 Cargo 包。
相当于 `cargo new`，但是指定目录是可选的。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-init.html>.

- 在当前目录中初始化一个带有二进制目标的 Rust 项目：

`cargo init`

- 在指定目录中初始化一个带有二进制目标的 Rust 项目：

`cargo init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- 在当前目录中初始化一个带有库目标的 Rust 项目：

`cargo init --lib`

- 在项目目录中初始化版本控制系统仓库 (默认为git)：

`cargo init --vcs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">git|hg|pijul|fossil|none</span>

- 设置包名称 (默认为目录名称)：

`cargo init --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
