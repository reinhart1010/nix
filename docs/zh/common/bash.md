---
layout: page
title: common/bash (中文)
description: "Bourne-Again SHell."
content_hash: 47ea21965ed8d1045f11f22885ad247cc45fc2f4
last_modified_at: 2023-11-12
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
  - title: português (Brasil) version
    url: /pt_BR/common/bash.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/bash.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bash

Bourne-Again SHell.
兼容`sh`的命令行解释器。
更多信息：<https://gnu.org/software/bash/>.

- 启动交互式 shell：

`bash`

- 执行命令：

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- 执行脚本文件：

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- 执行脚本文件，并将所有执行过的命令输出到终端：

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- 执行脚本文件，并在第一个错误处终止：

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.sh</span>

- 从输入（`stdin`）读取命令：

`bash -s`

- 将跟随的所有选项原样传递到要执行的脚本文件（可与`-s`选项共用来将选项传递到来自输入的命令 / 脚本）：

`bash --`

- 打印 bash 的版本信息（使用`echo $BASH_VERSION`来获得纯粹的版本字符串）：

`bash --version`
