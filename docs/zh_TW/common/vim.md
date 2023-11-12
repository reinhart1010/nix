---
layout: page
title: common/vim (中文 (繁體, 台灣))
description: "Vim (Vi IMproved), 是一個命令列文字編輯器，為不同類型的文字操作提供了多種模式。"
content_hash: 3992a6906bd6916326421795c895a43827596408
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

Vim (Vi IMproved), 是一個命令列文字編輯器，為不同類型的文字操作提供了多種模式。
在正常模式下按下 `i` 進入插入模式。按 `<Esc>` 返回正常模式，可以使用 Vim 指令。
更多資訊：<https://www.vim.org>.

- 打開檔案：

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 使用指定行數打開檔案：

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">指定行數</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">檔案/完整/路徑</span>

- 查看 Vim 指令手冊：

`:help<Enter>`

- 儲存並且離開：

`:wq<Enter>`

- 進入正常模式並且復原上次操作：

`<ESC>u`

- 搜尋特定字詞：

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">欲搜尋字詞</span>`<Enter>`

- 使用正規表示式（RE）尋找並取代整份文件：

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正規表示式</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">取代文字</span>`/g<Enter>`

- 顯示行數：

`:set nu<Enter>`
