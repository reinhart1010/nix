---
layout: page
title: common/cargo-report (中文)
description: "显示各种类型的报告。"
content_hash: 825ce85b4210f6661f4ced60f9e6f557f4396cb6
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-report.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-report.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo report

显示各种类型的报告。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-report.html>.

- 显示一个报告：

`cargo report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">future-incompatibilities|...</span>

- 显示具有指定由 Cargo 生成的 id 的报告：

`cargo report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">future-incompatibilities|...</span>` --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>

- 为指定的包显示报告：

`cargo report `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">future-incompatibilities|...</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package</span>
