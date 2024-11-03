---
layout: page
title: common/kismet (한국어)
description: "무선 네트워크 및 장치 감지기, 스니퍼, 워드라이빙 도구, WIDS(무선 침입 탐지) 프레임워크."
content_hash: ee537cbe6f3729786e49e3d620e8630ba3bf68c0
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/kismet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kismet

무선 네트워크 및 장치 감지기, 스니퍼, 워드라이빙 도구, WIDS(무선 침입 탐지) 프레임워크.
더 많은 정보: <https://www.kismetwireless.net/>.

- 특정 무선 인터페이스에서 패킷 캡처:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- 무선 인터페이스에서 여러 채널 모니터링:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0,wlan1</span>` -m`

- 패킷을 캡처하고 특정 디렉토리에 저장:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 특정 구성 파일로 Kismet 시작:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.conf</span>

- SQLite 데이터베이스에 데이터를 모니터링하고 기록:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --log-to-db`

- 특정 데이터 소스를 사용하여 모니터링:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --data-source=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtl433</span>

- 특정 이벤트에 대한 경고 활성화:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --enable-alert=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_ap</span>

- 특정 AP의 패킷에 대한 자세한 정보 표시:

`sudo kismet -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>` --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BSSID</span>
