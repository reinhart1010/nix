---
layout: page
title: common/aircrack-ng (한국어)
description: "수집된 패킷의 핸드셰이크 과정 중, WEP 및 WPA/WPA2 키를 크랙."
content_hash: eab64dbfefd0658e3e21bd61790e7d7d4e3a8192
last_modified_at: 2024-09-08
related_topics:
  - title: Deutsch version
    url: /de/common/aircrack-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aircrack-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aircrack-ng.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/aircrack-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/aircrack-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aircrack-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aircrack-ng

수집된 패킷의 핸드셰이크 과정 중, WEP 및 WPA/WPA2 키를 크랙.
Aircrack-ng 네트워크 소프트웨어 제품군의 일부.
더 많은 정보: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- [w]ordlist를 사용해 캡처 파일에서 크랙 키를 생성:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/wordlist.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>

- [w]ordlist와 액세스 포인트의 [e]ssid를 사용하여 캡처 파일에서 키를 크랙:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/wordlist.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>

- [w]ordlist와 액세스 포인트의 MAC 주소를 사용하여 캡처 파일에서 키를 크랙:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/wordlist.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/capture.cap</span>
