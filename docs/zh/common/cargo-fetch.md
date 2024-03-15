---
layout: page
title: common/cargo-fetch (中文)
description: "从网络获取包的依赖项。"
content_hash: defba0556566d370f81c98b65220a43cdadb44d6
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-fetch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo fetch

从网络获取包的依赖项。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-fetch.html>.

- 获取 `Cargo.lock` 中指定的依赖项 (对所有目标)：

`cargo fetch`

- 为指定目标获取依赖项：

`cargo fetch --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">目标三元组</span>
