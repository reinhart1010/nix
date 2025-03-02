---
layout: page
title: common/traceroute (日本語)
description: "ネットワークホストへの経路パケット追跡を表示します。"
content_hash: c5437ce057074937fa0b71ad77a86ae43f874211
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/traceroute.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/traceroute.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/traceroute.html
    icon: bi bi-globe
tldri18n_status: 2
---
# traceroute

ネットワークホストへの経路パケット追跡を表示します。
もっと詳しく: <https://manned.org/traceroute>。

- ホストへの経路追跡:

`traceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- IPアドレスとホスト名のマッピングを無効化する:

`traceroute -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 応答までの待機時間を秒単位で指定する:

`traceroute --wait=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- ホップごとのクエリ回数を指定する:

`traceroute --queries=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- プローブパケットのサイズをバイト単位で指定する:

`traceroute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- 宛先までのMTUを特定する:

`traceroute --mtu `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- UDPの代わりにICMPを使ってトレースルートする:

`traceroute --icmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
