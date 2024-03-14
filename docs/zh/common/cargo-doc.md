---
layout: page
title: common/cargo-doc (中文)
description: "构建 Rust 包的文档。"
content_hash: d2ffd85a809de00c7b2e23495ebcabc9464e5953
last_modified_at: 2024-03-14
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-doc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo doc

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
