---
layout: page
title: common/cargo-locate-project (中文)
description: "打印项目的 `Cargo.toml` 清单文件的完整路径。"
content_hash: 3fb7315ec6f22a18c3680d138f73d5789dfd40f6
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-locate-project.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-locate-project.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo locate-project

打印项目的 `Cargo.toml` 清单文件的完整路径。
如果项目是工作区的一部分，则显示项目的清单文件，而不是工作区的清单文件。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-locate-project.html>.

- 显示包含完整路径到 `Cargo.toml` 清单文件的 JSON 对象：

`cargo locate-project`

- 以指定格式显示项目路径：

`cargo locate-project --message-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">plain|json</span>

- 显示位于工作区根目录而不是当前工作区成员的 `Cargo.toml` 清单文件：

`cargo locate-project --workspace`

- 显示特定目录中的 `Cargo.toml` 清单文件：

`cargo locate-project --manifest-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/Cargo.toml</span>
