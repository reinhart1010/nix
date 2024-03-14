---
layout: page
title: common/cargo-vendor (中文)
description: "将项目的所有依赖项存储到指定目录中（默认为 `vendor`）。"
content_hash: 40c3e876f4f3e371bdfa9b3d031d34d8613001c5
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-vendor.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-vendor.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo vendor

将项目的所有依赖项存储到指定目录中（默认为 `vendor`）。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>.

- 将依赖项存储到指定目录，并配置在当前项目中使用这些存储的源代码：

`cargo vendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` > .cargo/config.toml`
