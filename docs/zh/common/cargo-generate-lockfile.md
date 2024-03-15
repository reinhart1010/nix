---
layout: page
title: common/cargo-generate-lockfile (中文)
description: "为当前包生成 Cargo.lock 文件。类似于 cargo update，但选项更少。"
content_hash: da697498be51dee00bea8592e6375fca27579f7b
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-generate-lockfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo generate-lockfile

为当前包生成 Cargo.lock 文件。类似于 cargo update，但选项更少。
如果锁定文件已经存在，它将使用每个包的最新版本重新构建。
更多信息：<https://doc.rust-lang.org/stable/cargo/commands/cargo-generate-lockfile.html>.

- 使用每个包的最新版本生成Cargo.lock文件：

`cargo generate-lockfile`
