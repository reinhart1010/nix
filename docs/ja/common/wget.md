---
layout: page
title: common/wget (日本語)
description: "Webからファイルをダウンロードします。"
content_hash: e67e9775144fcaed1b04c54b81586d6cedf133bc
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/wget.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/wget.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/wget.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wget.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/wget.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wget

Webからファイルをダウンロードします。
HTTP, HTTPS, そして FTP をサポートします。
もっと詳しく: <https://www.gnu.org/software/wget>。

- URLの内容を、ファイルにダウンロードする (この場合 "foo" と言う名前で):

`wget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- URLの内容を、ファイルにダウンロードする (この場合 "bar" と言う名前で):

`wget --output-document `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/foo</span>

- 1つのウェブページと、その全てのリソースを、リクエスト間隔を3秒にしてダウンロードする (スクリプト、スタイルシート、画像など):

`wget --page-requisites --convert-links --wait=3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepage.html</span>

- ディレクトリと、そのサブディレクトリ内のリストされたファイルを、全てダウンロードする (埋め込まれたページ要素はダウンロードしない):

`wget --mirror --no-parent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- ダウンロード速度と接続再試行回数を制限する:

`wget --limit-rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">300k</span>` --tries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/somepath/</span>

- HTTPサーバーからBasic認証を使って、ファイルをダウンロードする (FTPも機能する):

`wget --user=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>` --password=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">パスワード</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 未完了のダウンロードを続行する:

`wget --continue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- テキストファイルに格納されている全てのURLを、特定のディレクトリにダウンロードする:

`wget --directory-prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --input-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URLs.txt</span>
