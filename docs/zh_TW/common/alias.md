---
layout: page
title: common/alias (中文 (繁體, 台灣))
description: "建立快捷鍵名稱 -- 取代命令字串的單字。"
content_hash: ab816b1bd0f633bfd71cd6411c3fdda1a282fbfc
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
  - title: 中文 version
    url: /zh/common/alias.html
    icon: bi bi-globe
tldri18n_status: 2
---
# alias

建立快捷鍵名稱 -- 取代命令字串的單字。
快捷鍵只會在現有的 shell 有效，除非在 shell 的設定檔中定義快捷鍵，例如：`~/.bashrc`.
更多資訊：<https://tldp.org/LDP/abs/html/aliases.html>.

- 列出所有快捷鍵：

`alias`

- 建立快捷鍵：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">快捷名稱</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令字串</span>`"`

- 查看與給定名稱有關的快捷鍵：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">快捷名稱</span>

- 移除快捷鍵：

`unalias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">快捷名稱</span>

- 將 `rm` 變成互動式指令：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rm --interactive</span>`"`

- 建立 `la` 作為 `ls --all` 的捷徑：

`alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">la</span>`="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls --all</span>`"`
