---
layout: page
title: common/airodump-ng (한국어)
description: "패킷을 캡처하고, 무선 네트워크에 대한 정보를 표시."
content_hash: 753a4ac18e292aa43e65ab3e127224e4be251863
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/airodump-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/airodump-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airodump-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airodump-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airodump-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airodump-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airodump-ng

패킷을 캡처하고, 무선 네트워크에 대한 정보를 표시.
`aircrack-ng`의 일부.
더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=airodump-ng>.

- 2.4GHz 대역의 무선 네트워크에 대한 패킷을 캡처하고 정보를 표시:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 5GHz 대역의 무선 네트워크에 대한 패킷을 캡처하고 정보를 표시:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` --band a`

- 2.4GHz 및 5GHz 대역 모두에서 무선 네트워크에 대한 패킷을 캡처하고 정보를 표시:

`sudo airodump-ng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` --band abg`

- MAC 주소와 채널을 통해 패킷을 캡처하고, 무선 네트워크에 대한 정보를 표시 및 출력 결과를 파일에 저장:

`sudo airodump-ng --channel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">channel</span>` --write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface</span>
