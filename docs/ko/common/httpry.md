---
layout: page
title: common/httpry (한국어)
description: "HTTP 트래픽을 표시하고 기록하기 위한 경량 패킷 스니퍼."
content_hash: 15b10d90d1404afdcfe45bc1c34a3cb8844d76ad
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/httpry.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httpry.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httpry

HTTP 트래픽을 표시하고 기록하기 위한 경량 패킷 스니퍼.
구문 분석되는 트래픽을 실시간으로 표시하거나 출력 파일에 기록하는 데몬 프로세스로 실행될 수 있음.
더 많은 정보: <https://dumpsterventures.com/jason/httpry/>.

- 출력을 파일로 저장:

`httpry -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>

- 특정 인터페이스를 수신하고 출력을 바이너리 PCAP 형식 파일로 저장:

`httpry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>

- 쉼표로 구분된 HTTP 동사 목록으로 출력을 필터링:

`httpry -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">get|post|put|head|options|delete|trace|connect|patch</span>

- 입력 캡처 파일에서 IP로 필터링:

`httpry -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host 192.168.5.25</span>`'`

- 데몬 프로세스로 실행:

`httpry -d -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.log</span>
