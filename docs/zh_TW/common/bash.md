---
layout: page
title: common/bash (中文 (繁體, 台灣))
description: "Bourne-Again SHell. 一個與 `sh` 相容的命令列。"
content_hash: c46a9c3972f9cb5c4fea1c02e2973a26d97dfc99
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
  - title: 中文 version
    url: /zh/common/bash.html
    icon: bi bi-globe
---
# bash

Bourne-Again SHell. 一個與 `sh` 相容的命令列。
參照 `histexpand` 以使用 history expansion 特性。
更多資訊：<https://gnu.org/software/bash/>.

- 開啟互動式 shell：

`bash`

- 執行指令然後退出：

`bash -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指令</span>`"`

- 執行腳本：

`bash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh檔</span>

- 執行腳本，每個指令執行之前先在命令列印出該指令：

`bash -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh檔</span>

- 執行腳本，執行錯誤時，終止執行該腳本：

`bash -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sh檔</span>

- 從標準輸入 (stdin) 讀取並執行指令：

`bash -s`

- 在終端機印出 bash 的版本資訊 （`$BASH_VERSION` 只包含版本號)：

`bash --version`
