---
layout: page
title: common/alias (中文)
description: "创建别名 -- 用给定的字符串指代特定的命令。"
content_hash: 08735f6fb485e86218039f0a704f41d28a7540a6
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/common/alias.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/alias.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/alias.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/alias.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/alias.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alias.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/alias.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/alias.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alias.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/alias.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alias.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/alias.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/alias.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alias.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/alias.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/alias.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/alias.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alias

创建别名 -- 用给定的字符串指代特定的命令。
别名只会在当前的 shell 会话中生效，除非它们在 shell 的配置文件中被定义，例如`~/.bashrc`.
更多信息：<https://tldp.org/LDP/abs/html/aliases.html>.

- 创建一个通用的别名：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">别名</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>`"`

- 通过给定的别名查看它所指代的命令：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">别名</span>

- 移除一个别名：

`unalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">别名</span>

- 列出所有的别名：

`alias -p`

- 将 rm 转换为交互式命令：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm -i</span>`"`

- 创建别名 `la` 来指代 `ls -a`：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">la</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -a</span>`"`
