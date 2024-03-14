---
layout: page
title: common/cargo-remove (中文)
description: "从 Rust 项目的 `Cargo.toml` 清单中移除依赖关系。"
content_hash: 176cc74eae9aaa4e1be9fec14f64142790a68a50
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-remove.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-remove.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo remove

从 Rust 项目的 `Cargo.toml` 清单中移除依赖关系。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-remove.html>.

- 从当前项目中移除一个依赖项：

`cargo remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>

- 移除开发或构建依赖项：

`cargo remove --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dev|build</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>

- 移除给定目标平台的依赖项：

`cargo remove --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标平台</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>
