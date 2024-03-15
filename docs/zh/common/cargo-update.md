---
layout: page
title: common/cargo-update (中文)
description: "更新记录在 `Cargo.lock` 中的依赖关系。"
content_hash: a8246586b250ab416988f74b2fa43d71a1d42216
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo update

更新记录在 `Cargo.lock` 中的依赖关系。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-update.html>.

- 将 `Cargo.lock` 中的依赖项更新为可能的最新版本：

`cargo update`

- 显示将会更新的内容，但实际上不写入锁定文件：

`cargo update --dry-run`

- 仅更新指定的依赖项：

`cargo update --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项1</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项2</span>` --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项3</span>

- 将特定依赖项设置为特定版本：

`cargo update --package `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">依赖项</span>` --precise `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.2.3</span>
