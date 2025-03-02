---
layout: page
title: common/dig (日本語)
description: "DNS 情報を調べるユーティリティーです。"
content_hash: b349d0ab78253f8a41caf0e583298954660fceba
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/dig.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dig.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dig

DNS 情報を調べるユーティリティーです。
もっと詳しく: <https://manned.org/dig>。

- ホスト名に関連する IP を検索（A レコード）:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 指定したドメインの詳細な回答を得る（A レコード）:

`dig +noall +answer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 指定されたドメイン名に関連する特定の DNS レコードタイプを取得する:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|MX|TXT|CNAME|NS</span>

- 問い合わせる別の DNS サーバーを指定する:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IP アドレスの DNS 逆引きの実行（PTR レコード）:

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- ゾーンの権威ネームサーバーの検索と SOA レコードの表示:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- ドメイン名を解決するための反復的なクエリの実行と、そのトレースパス全体を表示する:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
