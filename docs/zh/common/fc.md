---
layout: page
title: common/fc (中文)
description: "打开最近的命令进行编辑，然后运行它。"
content_hash: 7490511e3b82bd95b4c5b5168c38befd129e2b83
last_modified_at: 2024-11-28
related_topics:
  - title: English version
    url: /en/common/fc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fc

打开最近的命令进行编辑，然后运行它。
更多信息：<https://manned.org/fc>.

- 在默认系统编辑器中打开最后一个命令，并在编辑后运行：

`fc`

- 指定一个编辑器打开：

`fc -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'emacs'</span>

- 从历史记录中列出最近的命令：

`fc -l`

- 以相反的顺序列出最近的命令：

`fc -l -r`

- 从历史记录中编辑并运行一个命令：

`fc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">编号</span>

- 编辑并运行指定区间内的命令：

`fc '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">416</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">420</span>`'`

- 显示帮助：

`fc --help`
