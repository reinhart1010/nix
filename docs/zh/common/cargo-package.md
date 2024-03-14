---
layout: page
title: common/cargo-package (中文)
description: "将本地包装成一个可分发的 tarball 文件（`.crate` 文件）。"
content_hash: 02af10d4d3a0316398d93b8f4fddcc494887e3e9
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-package.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-package.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo package

将本地包装成一个可分发的 tarball 文件（`.crate` 文件）。
类似于 `cargo publish --dry-run`，但具有更多选项。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-package.html>.

- 执行检查并创建一个 `.crate` 文件 (相当于 `cargo publish --dry-run`)：

`cargo package`

- 显示将包含在tarball中的文件，而不实际创建它：

`cargo package --list`
