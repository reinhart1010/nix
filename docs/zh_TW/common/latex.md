---
layout: page
title: common/latex (中文 (繁體, 台灣))
description: "從 LaTeX 原始檔編譯 DVI 文件。"
content_hash: f441a48950f49c4130450e476ccda65db4ec0d37
last_modified_at: 2023-10-04
related_topics:
  - title: Deutsch version
    url: /de/common/latex.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/latex.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># latex

從 LaTeX 原始檔編譯 DVI 文件。
更多資訊：<https://www.latex-project.org>.

- 編譯 DVI 文件：

`latex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tex 檔案</span>

- 編譯 DVI 文檔，指定輸出位置：

`latex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">輸出目錄位置</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tex 檔案</span>

- 編譯 DVI 文檔，出錯時退出：

`latex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tex 檔案</span>
