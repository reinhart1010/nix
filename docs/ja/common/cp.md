---
layout: page
title: common/cp (日本語)
description: "ファイルやディレクトリをコピーします。"
content_hash: be164410ba103f380c7178b1c373c92495d9cfa9
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/common/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/cp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/cp.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/cp.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cp.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/cp.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

ファイルやディレクトリをコピーします。
詳しくはこちら: <https://www.gnu.org/software/coreutils/cp>

- ファイルを別の場所にコピー:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー元ファイルへのパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー先ファイルへのパス</span>

- ファイル名を維持したまま、ファイルを別のディレクトリにコピーする:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー元ファイルへのパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー先ディレクトリへのパス</span>

- ディレクトリの内容を別の場所に再帰的にコピーする（コピー先が存在する場合は、その中にディレクトリがコピーされる):

`cp -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー元ディレクトリへのパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー先ディレクトリへのパス</span>

- 詳細モードでディレクトリを再帰的にコピーする（コピーされたファイルが表示される）:

`cp -vR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー元ディレクトリへのパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー先ディレクトリへのパス</span>

- 対話形式でテキストファイルを別の場所にコピーする（上書きする前にユーザーに確認する）:

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー先ディレクトリへのパス</span>

- コピーする前にシンボリックリンクをたどる:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">link</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コピー先ディレクトリへのパス</span>
