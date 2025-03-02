---
layout: page
title: windows/where (日本語)
description: "検索パターンに一致するファイルの場所を表示します。"
content_hash: a29a25eba70f82e48a281fbb3df2c29988781a1d
last_modified_at: 2025-03-02
related_topics:
  - title: বাংলা version
    url: /bn/windows/where.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/where.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/windows/where.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/where.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/where.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/where.html
    icon: bi bi-globe
tldri18n_status: 2
---
# where

検索パターンに一致するファイルの場所を表示します。
デフォルトは現在の作業ディレクトリと環境変数 PATH のパスです。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/where>。

- ファイルパターンの場所を表示する:

`where `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパターン</span>

- ファイルサイズと日付を含む、ファイルパターンの場所を表示する:

`where /T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパターン</span>

- 指定したパスのファイルパターンを、再帰的に検索する:

`where /R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path\to\directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパターン</span>

- ファイルパターンの場所のエラーコードを、表示無しで返す:

`where /Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパターン</span>
