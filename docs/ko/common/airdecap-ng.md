---
layout: page
title: common/airdecap-ng (한국어)
description: "WEP, WPA 또는 WPA2로 암호화된 캡처 파일 해독."
content_hash: fed28462145019f2f8130dab1b184e326ee0c621
last_modified_at: 2024-09-08
related_topics:
  - title: English version
    url: /en/common/airdecap-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/airdecap-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airdecap-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airdecap-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airdecap-ng

WEP, WPA 또는 WPA2로 암호화된 캡처 파일 해독.
Aircrack-ng 네트워크 소프트웨어 제품군의 일부.
더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- 열려있는 네트워크 캡처 파일에서 무선 헤더를 제거, 액세스 포인트의 MAC 주소를 사용해 필터링:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>

- 16진수 형식의 키를 사용하여 [w]EP 암호화된 캡처 파일을 해독:

`airdecap-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>

- 액세스 포인트의 [e]ssid 및 [p]assword를 사용하여 WPA/WPA2 암호화된 캡처 파일을 해독:

`airdecap-ng -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>

- 액세스 포인트의 [e]ssid 및 [p]assword를 사용하여 헤더를 보존하는, WPA/WPA2 암호화된 캡처 파일을 해독:

`airdecap-ng -l -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>

- 액세스 포인트의 [e]ssid 및 [p]assword를 사용하여 WPA/WPA2 암호화된 캡처 파일을 해독하고, 해당 MAC 주소를 사용하여 필터링:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>
