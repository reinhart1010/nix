---
layout: page
title: common/cargo-login (中文)
description: "将 API 令牌保存到本地的凭据存储中。"
content_hash: 5ea1c3712a3306649610b6a40758b8b79ed0689a
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo login

将 API 令牌保存到本地的凭据存储中。
该令牌用于对包注册表进行身份验证。您可以使用 `cargo logout` 来删除它。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-login.html>.

- 将 API 令牌添加到本地凭据存储中 (位于 `$CARGO_HOME/credentials.toml`)：

`cargo login`

- 使用指定的注册表 (注册表名称可以在配置中定义，默认为 <https://crates.io>)：

`cargo login --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
