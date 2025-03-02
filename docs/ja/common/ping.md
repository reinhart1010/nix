---
layout: page
title: common/ping (日本語)
description: "ICMP ECHO_REQUEST パケットをネットワークホストに送信します。"
content_hash: 036926030c3d2fc3cb03cfc8561da1bd7eb1a2e6
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ping.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ping.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ping

ICMP ECHO_REQUEST パケットをネットワークホストに送信します。
もっと詳しく: <https://manned.org/ping>。

- ホストをPingする:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>

- ホストに特定の回数だけpingする:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">回数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>

- リクエストの間隔を秒単位で指定して、ホストにpingする (デフォルトは1秒):

`ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>

- アドレスのシンボリックネームを調べずに、ホストにpingする:

`ping -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>

- pingしてパケットを受信したら、ベルを鳴らす (端末がサポートしている場合):

`ping -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>

- 応答がない場合は、メッセージも表示する:

`ping -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>

- 特定のping回数、パケットごとの応答タイムアウト(`-W`)、ping実行全体の制限時間(`-w`)を指定して、ホストにpingする:

`ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">回数</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒数</span>` -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒数</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ホスト</span>
