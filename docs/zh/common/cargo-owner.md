---
layout: page
title: common/cargo-owner (中文)
description: "管理包在注册表上的所有者。"
content_hash: 3c7f49523c0d2239e252be6e760203e6f8a3183c
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/cargo-owner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cargo-owner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cargo owner

管理包在注册表上的所有者。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-owner.html>.

- 邀请指定的用户或团队作为所有者：

`cargo owner --add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名|github:机构名称:团队名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 将指定的用户或团队从所有者中删除：

`cargo owner --remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名|github:机构名称:团队名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 列出一个包的所有者：

`cargo owner --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 使用指定的注册表 (注册表名称可以在配置中定义，默认为 <https://crates.io>)：

`cargo owner --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>
