---
layout: page
title: common/cargo-test (中文)
description: "执行 Rust 包的单元测试和集成测试。"
content_hash: b24ef8483e4e7f53159c35f86fdd61a90733f823
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-test.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cargo-test.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cargo-test.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-test.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo test

执行 Rust 包的单元测试和集成测试。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-test.html>.

- 仅运行包含特定字符串在其名称中的测试：

`cargo test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">测试名称</span>

- 设置并行运行测试用例的数量：

`cargo test -- --test-threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">数量</span>

- 在 release 模式下测试构建，启用优化：

`cargo test --release`

- 测试工作区中的所有包：

`cargo test --workspace`

- 为特定包运行测试：

`cargo test --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 运行测试时不隐藏测试执行的输出：

`cargo test -- --nocapture`
