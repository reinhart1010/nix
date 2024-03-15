---
layout: page
title: common/cargo-check (中文)
description: "检查本地软件包及其所有依赖包是否有错误。"
content_hash: cd1d1d9b15a5e4edaf9c39354856e34e788f0e7d
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-check.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo check

检查本地软件包及其所有依赖包是否有错误。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-check.html>.

- 检查当前包：

`cargo check`

- 检查所有测试：

`cargo check --tests`

- 检查 `tests/integration_test1.rs` 中的集成测试：

`cargo check --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">integration_test1</span>

- 使用 `feature1` 和 `feature2` 功能检查当前包：

`cargo check --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">feature1,feature2</span>

- 禁用默认功能后检测当前包：

`cargo check --no-default-features`
