---
layout: page
title: common/cargo-run (中文)
description: "运行当前的 Cargo 包。"
content_hash: 611bfe3b64fad201fccaed2adba9f05de095ad80
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo run

运行当前的 Cargo 包。
注意: 执行的二进制文件的工作目录将设置为当前工作目录。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-run.html>.

- 运行默认的二进制目标：

`cargo run`

- 运行指定的二进制文件：

`cargo run --bin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 运行指定的示例：

`cargo run --example `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">示例名</span>

- 激活一系列以空格或逗号分隔的功能：

`cargo run --features `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">功能1 功能2 ...</span>

- 禁用默认功能：

`cargo run --no-default-features`

- 激活所有可用的功能：

`cargo run --all-features`

- 使用指定的配置文件运行：

`cargo run --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件名称</span>
