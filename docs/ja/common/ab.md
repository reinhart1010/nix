---
layout: page
title: common/ab (日本語)
description: "Apache HTTP server のベンチマーク用ツールです。"
content_hash: 205f10287a5fd3351101016987f8b2f55ecb7c59
last_modified_at: 2025-03-02
related_topics:
  - title: বাংলা version
    url: /bn/common/ab.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/ab.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ab.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ab.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ab.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ab.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ab.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ab.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ab.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/ab.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ab.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/ab.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/ab.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ab.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ab

Apache HTTP server のベンチマーク用ツールです。
もっと詳しく: <https://httpd.apache.org/docs/current/programs/ab.html>。

- 指定された URL に 100 個の GET リクエストを送信する:

`ab -n 100 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 指定された URL に 100 個の GET リクエストを、10 個ずつ同時に送信する:

`ab -n 100 -c 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- ファイルからの JSON ペイロードを使って、指定された URL に 100 個の POST リクエストを送信する:

`ab -n 100 -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application/json</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイルパス.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- [K]eep Alive を有効化する（１つの HTTP セッションで複数のリクエストを実行する）:

`ab -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- ベンチマークを行う最大秒数を設定する:

`ab -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">60</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
