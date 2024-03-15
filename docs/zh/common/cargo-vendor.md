---
layout: page
title: common/cargo-vendor (中文)
description: "将项目的所有依赖项存储到指定目录中（默认为 `vendor`）。"
content_hash: 40c3e876f4f3e371bdfa9b3d031d34d8613001c5
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-vendor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo vendor

将项目的所有依赖项存储到指定目录中（默认为 `vendor`）。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-vendor.html>.

- 将依赖项存储到指定目录，并配置在当前项目中使用这些存储的源代码：

`cargo vendor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` > .cargo/config.toml`
