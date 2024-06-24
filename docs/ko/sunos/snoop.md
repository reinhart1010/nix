---
layout: page
title: sunos/snoop (한국어)
description: "네트워크 패킷 스니퍼."
content_hash: 9465eb532f1037bef14a0761a34993ebb17a7fb5
last_modified_at: 2024-06-24
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/sunos/snoop.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/sunos/snoop.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snoop

네트워크 패킷 스니퍼.
tcpdump와 동일한 기능을 하는 SunOS 대체품.
더 많은 정보: <https://www.unix.com/man-page/sunos/1m/snoop>.

- 특정 네트워크 인터페이스에서 패킷을 캡처:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- 화면에 표시하는 대신 캡처된 패킷을 파일에 저장:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 패킷의 상세 프로토콜 레이어 요약 표시:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 호스트 이름에서 지정된 포트로 가는 네트워크 패킷을 캡처:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>

- 두 IP 주소 간에 교환되는 네트워크 패킷의 hex 덤프를 캡처하고 표시:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip2</span>
