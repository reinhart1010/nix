---
layout: page
title: common/cargo-fix (中文)
description: "自动修复 `rustc` 报告的 lint 警告。"
content_hash: aa4bc012649ec2bbe6b40128716956bad3a40cbc
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-fix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-fix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo fix

自动修复 `rustc` 报告的 lint 警告。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-fix.html>.

- 即使已经有编译器错误，也要修复代码：

`cargo fix --broken-code`

- 即使工作目录有更改，也要修复代码：

`cargo fix --allow-dirty`

- 将一个包迁移到下一个 Rust 版本：

`cargo fix --edition`

- 修复包的库：

`cargo fix --lib`

- 修复指定的集成测试：

`cargo fix --test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 修复工作区中的所有成员：

`cargo fix --workspace`
