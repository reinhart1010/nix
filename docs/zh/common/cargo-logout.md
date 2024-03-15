---
layout: page
title: common/cargo-logout (中文)
description: "从本地注册表中删除 API 令牌。"
content_hash: 4fc653b050f1abf97e1f3840e0bdef6b77f6f091
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-logout.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo logout

从本地注册表中删除 API 令牌。
该令牌用于对包注册表进行身份验证。您可以使用 `cargo login` 将其添加回来。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-logout.html>.

- 从本地凭据存储中 (位于 `$CARGO_HOME/credentials.toml`) 移除 API 令牌：

`cargo logout`

- 使用指定的注册表 (注册表名称可以在配置中定义，默认为 <https://crates.io>)：

`cargo logout --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
