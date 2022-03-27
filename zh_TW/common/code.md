---
layout: page
title: common/code (中文 (繁體, 台灣))
description: "Visual Studio Code."
content_hash: cce6ab6083257fba0aa560b42028a2cc3587302b
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/code.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># code

Visual Studio Code.
更多資訊：<https://github.com/microsoft/vscode>.

- 執行 VS Code：

`code`

- 在 VS Code 開啟當前目錄：

`code .`

- 在 VS Code 開啟檔案或目錄：

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>

- 在目前開啟的 VS Code 視窗中開啟一個檔案或目錄：

`code --reuse-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>

- 在 VS Code 中比較兩個檔案：

`code -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案一</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案二</span>

- 用超級使用者 (sudo) 權限執行 VS Code：

`sudo code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案或目錄/完整/路徑</span>` --user-data-dir`
