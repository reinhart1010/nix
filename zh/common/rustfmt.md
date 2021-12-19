---
layout: page
title: common/rustfmt (中文)
description: "格式化 Rust 源代码的工具。"
content_hash: 490183b1b4f2df18a41a0f1ba3ec7d71b5430938
related_topics:
  - title: English version
    url: /en/common/rustfmt.html
    icon: bi bi-globe
---
# rustfmt

格式化 Rust 源代码的工具。
更多信息：<https://github.com/rust-lang/rustfmt>.

- 格式化文件，就地覆盖原始文件：

`rustfmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.rs</span>

- 检查文件的格式并在控制台上显示所有更改：

`rustfmt --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.rs</span>

- 格式化之前，备份所有修改过的文件（原始文件的扩展名为 `.bk`）：

`rustfmt --backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source.rs</span>
