---
layout: page
title: common/vim (日本語)
description: "コマンドラインのテキストエディタである Vim（Vi IMproved）には、さまざまな種類のテキスト操作のためのモードが用意されています。"
content_hash: 05a1d0acc645ce7920022d60f6776e01840a0555
last_modified_at: 2025-03-02
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
  - title: Indonesia version
    url: /id/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
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
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

コマンドラインのテキストエディタである Vim（Vi IMproved）には、さまざまな種類のテキスト操作のためのモードが用意されています。
`i` を押すと編集モードになります。`<Esc>` を押すと通常モードに戻り、通常のテキスト挿入はできません。
もっと詳しく: <https://www.vim.org>。

- ファイルを開く:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルへのパス</span>

- 指定した行番号でファイルを開く:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ライン番号</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルへのパス</span>

- Vim のヘルプマニュアルを見る:

`:help<Enter>`

- 保存と終了:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:x<Enter>|<Esc>:wq<Enter></span>

- 最後の操作を元に戻す:

`<Esc>u`

- ファイル内のパターンを検索する（`n`/`N` を押すと次/前のマッチに進む）:

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">検索パターン</span>`<Enter>`

- ファイル全体での正規表現による置換の実行:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パターン</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/g<Enter>`

- ライン番号の表示:

`:set nu<Enter>`
