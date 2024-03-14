---
layout: page
title: common/cargo-metadata (中文)
description: "以 JSON 格式输出当前包的工作空间成员和已解析的依赖关系。"
content_hash: b0f15784d882a44eafea60dd5034b1873b83e29e
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-metadata.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-metadata.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo metadata

以 JSON 格式输出当前包的工作空间成员和已解析的依赖关系。
注意：输出格式可能在未来的 Cargo 版本中发生变化。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-metadata.html>.

- 打印当前包的工作空间成员和已解析的依赖关系：

`cargo metadata`

- 仅打印工作空间成员，不获取依赖项：

`cargo metadata --no-deps`

- 根据指定版本打印特定格式的元数据：

`cargo metadata --format-version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 打印带有 `resolve` 字段的元数据，仅包括给定目标三元组的依赖关系 (注意：`packages` 数组仍将包括所有目标的依赖关系)：

`cargo metadata --filter-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标三元组</span>
