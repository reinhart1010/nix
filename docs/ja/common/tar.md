---
layout: page
title: common/tar (日本語)
description: "アーカイブ(複数のファイルやフォルダを 1 つのファイルに纏める)の為のユーティリティー。"
content_hash: 9bfc04b96ac12f8a4c95e79b05e67ceb7f6fc12d
last_modified_at: 2025-03-02
related_topics:
  - title: العربية version
    url: /ar/common/tar.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/tar.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tar.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/tar.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/tar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tar.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tar.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/tar.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tar.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/tar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tar

アーカイブ(複数のファイルやフォルダを 1 つのファイルに纏める)の為のユーティリティー。
gzip や bzip2 などの圧縮方法と組み合わせることが多いです。
もっと詳しく: <https://www.gnu.org/software/tar>。

- アーカイブを作成し、それをファイルに書き込む:

`tar cf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">出力ファイル名.tar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル1 ファイル2 ...</span>

- gzip 形式で圧縮されたアーカイブを作成し、それをファイルに書き込む:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">出力ファイル名.tar.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル1 ファイル2 ...</span>

- 相対パスを用いてディレクトリから gzip 形式のアーカイブを作成する:

`tar czf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">出力ファイル名.tar.gz</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリへの相対パス</span>` .`

- (圧縮された)アーカイブファイルを、カレントディレクトリに過程を詳細表示しながら展開する:

`tar xvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">入力ファイル名.tar[.gz|.bz2|.xz]</span>

- (圧縮された)アーカイブファイルを、指定のディレクトリに展開する:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">入力ファイル名.tar[.gz|.bz2|.xz]</span>` --directory=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ディレクトリ</span>

- 圧縮されたアーカイブを作成し、それにファイルを書き込む。なお、接尾辞で圧縮プログラムを指定する:

`tar caf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">出力ファイル名.tar.xz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル1 ファイル2 ...</span>

- tar ファイルの内容を詳細に表示する:

`tar tvf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">入力ファイル名.tar</span>

- アーカイブファイルからパターンに合致するファイルを抽出する:

`tar xf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">入力ファイル名.tar</span>` --wildcards "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.html</span>`"`
