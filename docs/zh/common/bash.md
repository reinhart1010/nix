---
layout: page
title: common/bash (中文)
description: "Bourne-Again SHell，兼容 `sh` 的命令行解释器。"
content_hash: de770bd598bdf229f700f6e0638a983a8dd174d5
last_modified_at: 2024-11-28
related_topics:
  - title: Deutsch version
    url: /de/common/bash.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/bash.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bash.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bash.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bash.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bash.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bash.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/bash.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bash

Bourne-Again SHell，兼容 `sh` 的命令行解释器。
此外请参阅：`zsh`，`histexpand`（历史展开）。
更多信息：<https://www.gnu.org/software/bash/>.

- 启动交互式 shell：

`bash`

- 启动一个不加载启动配置的交互式的 shell 会话：

`bash --norc`

- 执行命令：

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo '已执行bash命令'</span>`"`

- 执行脚本文件：

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本文件.sh</span>

- 执行脚本文件，并将所有执行过的命令输出到终端：

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本文件.sh</span>

- 执行脚本文件，并在第一个错误处终止：

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本文件.sh</span>

- 从 `stdin` 执行指定的命令：

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "echo '已执行bash命令'"</span>` | bash`

- 启动一个限制的 shell 会话：

`bash -r`
