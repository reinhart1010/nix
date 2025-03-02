---
layout: page
title: common/chsh (日本語)
description: "ユーザーのログインシェルを変更します。"
content_hash: acd4b20ac8e22c2948165421cba8b7616f4e41e7
last_modified_at: 2025-03-02
related_topics:
  - title: bosanski version
    url: /bs/common/chsh.html
    icon: bi bi-globe
  - title: dansk version
    url: /da/common/chsh.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/common/chsh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chsh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chsh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chsh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/chsh.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chsh.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chsh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chsh.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chsh.html
    icon: bi bi-globe
  - title: norsk version
    url: /no/common/chsh.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/chsh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chsh

ユーザーのログインシェルを変更します。
もっと詳しく: <https://manned.org/chsh>。

- カレントユーザーのログインシェルを対話的に変更する:

`chsh`

- カレントユーザーのログインシェルを変更する:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">シェルへのパス</span>

- 指定したユーザーのログインシェルを変更する:

`chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">シェルへのパス</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザー名</span>

- 使用可能なシェルの一覧を表示する:

`chsh -l`
