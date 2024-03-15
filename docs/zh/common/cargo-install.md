---
layout: page
title: common/cargo-install (中文)
description: "构建并安装一个 Rust 二进制文件。"
content_hash: be9c7ec9e5ae14131d13d79985667494e92a326e
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-install.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo install

构建并安装一个 Rust 二进制文件。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-install.html>.

- 从 <https://crates.io> 安装一个包 (版本是可选的，默认为最新版本)：

`cargo install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 从指定的 Git 仓库安装一个包：

`cargo install --git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库URL</span>

- 从 Git 仓库安装时，根据指定的 branch/tag/commit 构建：

`cargo install --git `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">仓库URL</span>` --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch|tag|rev</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">branch_name|tag|commit_hash</span>

- 列出所有已安装的包及其版本：

`cargo install --list`
