---
layout: page
title: common/cargo-doc (中文)
description: "构建 Rust 包的文档。"
content_hash: d2ffd85a809de00c7b2e23495ebcabc9464e5953
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-doc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-doc.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-doc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo doc

构建 Rust 包的文档。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-doc.html>.

- 为当前项目及所有依赖项构建文档：

`cargo doc`

- 不为依赖项构建文档：

`cargo doc --no-deps`

- 构建并在浏览器中打开文档：

`cargo doc --open`

- 构建并查看特定包的文档：

`cargo doc --open --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>
