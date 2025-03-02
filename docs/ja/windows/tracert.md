---
layout: page
title: windows/tracert (日本語)
description: "PCとターゲット間の経路の各ステップに関する情報を受信します。"
content_hash: bd9f5c584df9a46a1f5f945df6222138c551c2e1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/windows/tracert.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/tracert.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tracert

PCとターゲット間の経路の各ステップに関する情報を受信します。
もっと詳しく: <https://learn.microsoft.com/windows-server/administration/windows-commands/tracert>。

- ルートを追跡する:

`tracert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- `tracert`がIPアドレスをホスト名に解決しないようにする:

`tracert /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- `tracert`にIPv4のみの利用を強制する:

`tracert /4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- `tracert`にIpv6のみの利用を強制する:

`tracert /6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- ターゲットの検索における最大ホップ数を指定する:

`tracert /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">最大ホップ数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP</span>

- ヘルプを表示する:

`tracert /?`
