---
layout: page
title: linux/arpspoof (한국어)
description: "패킷을 가로채기 위해 ARP 응답을 위조합니다."
content_hash: 9d8500ed920800a727f0060762d8fc6abf91a104
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/arpspoof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arpspoof

패킷을 가로채기 위해 ARP 응답을 위조합니다.
더 많은 정보: <https://monkey.org/~dugsong/dsniff>.

- 호스트의 패킷을 가로채기 위해 [i]인터페이스의 모든 호스트를 중독:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_IP</span>

- 호스트의 패킷을 가로채기 위해 [i]인터페이스의 [t]대상을 중독:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_IP</span>

- 호스트의 패킷을 가로채기 위해 [i]인터페이스의 [t]대상과 호스트를 모두 중독:

`sudo arpspoof -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -r -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_IP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_IP</span>
