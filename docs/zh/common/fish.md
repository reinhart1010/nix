---
layout: page
title: common/fish (中文)
description: "The Friendly Interactive SHell, 一个设计为用户友好的命令行解释器。"
content_hash: 23b3edb19116a991ed5e2a352e19957b759f54b2
last_modified_at: 2023-11-26
related_topics:
  - title: Deutsch version
    url: /de/common/fish.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/fish.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/fish.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fish.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fish

The Friendly Interactive SHell, 一个设计为用户友好的命令行解释器。
更多信息：<https://fishshell.com>.

- 启动交互式 shell 会话：

`fish`

- 启动不加载启动配置的交互式 shell 会话：

`fish --no-config`

- 执行特定命令：

`fish --command "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo 'fish is executed'</span>`"`

- 执行特定脚本：

`fish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.fish</span>

- 检查特定脚本是否有语法错误：

`fish --no-execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.fish</span>

- 从 `stdin` 执行特定命令：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo 'fish is executed'"</span>` | fish`

- 在专用模式下启动交互式 shell 会话，其中 shell 不会访问旧历史记录或保存新历史记录：

`fish --private`

- 定义并导出一个在 shell 重启后持续存在的环境变量（内置）：

`set --universal --export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">变量值</span>
