---
layout: page
title: common/cargo-yank (中文)
description: "从索引中移除发布的包。应该只在意外发布了一个严重错误的包时使用。"
content_hash: 98dfd787bd8a1bda746b74d6a755c88a233fb8e2
last_modified_at: 2024-03-15
related_topics:
  - title: English version
    url: /en/common/cargo-yank.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cargo yank

从索引中移除发布的包。应该只在意外发布了一个严重错误的包时使用。
注意：这不会删除任何数据。包在被撤回后仍然存在，只是阻止新项目使用它。
更多信息：<https://doc.rust-lang.org/cargo/commands/cargo-yank.html>.

- 撤回指定版本的包：

`cargo yank `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 撤销撤回 (即允许再次下载)：

`cargo yank --undo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 使用指定的注册表 (注册表名称可以在配置中定义 - 默认为 <https：//crates.io>)：

`cargo yank --registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>
