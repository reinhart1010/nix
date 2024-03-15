---
layout: page
title: common/cargo-verify-project (中文)
description: "检查 `Cargo.toml` 文件清单的正确性，并将结果以 JSON 对象的形式打印出来。"
content_hash: e31659bd8a449b82f8d113dc1469942a75162f58
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-verify-project.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo verify-project

检查 `Cargo.toml` 文件清单的正确性，并将结果以 JSON 对象的形式打印出来。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-verify-project.html>.

- 检查当前项目清单的正确性：

`cargo verify-project`

- 检查指定清单文件的正确性：

`cargo verify-project --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Cargo.toml</span>
