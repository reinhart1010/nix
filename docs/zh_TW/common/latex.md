---
layout: page
title: common/latex (中文 (繁體, 台灣))
description: "從 LaTeX 原始檔編譯 DVI 文件。"
content_hash: 46c42d16b6511268d80b71c8b2f99cfcb41e9110
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/latex.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/latex.html
    icon: bi bi-globe
tldri18n_status: 2
---
# latex

從 LaTeX 原始檔編譯 DVI 文件。
更多資訊：<https://www.latex-project.org>.

- 編譯 DVI 文件：

`latex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tex 檔案</span>

- 編譯 DVI 文件，指定輸出位置：

`latex -output-directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">輸出目錄位置</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tex 檔案</span>

- 編譯 DVI 文件，出錯時退出：

`latex -halt-on-error `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tex 檔案</span>
