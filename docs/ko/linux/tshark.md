---
layout: page
title: linux/tshark (한국어)
description: "패킷 분석 도구, Wireshark의 CLI 버전."
content_hash: 4c8787ba5330970b0720d04c082501f264358efb
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tshark.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/tshark.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tshark.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tshark

패킷 분석 도구, Wireshark의 CLI 버전.
더 많은 정보: <https://tshark.dev/>.

- 로컬호스트에서 모든 것 모니터링:

`tshark`

- 특정 캡처 필터와 일치하는 패킷만 캡처:

`tshark -f '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">udp port 53</span>`'`

- 특정 출력 필터와 일치하는 패킷만 표시:

`tshark -Y '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.request.method == "GET"</span>`'`

- 특정 프로토콜(예: HTTP)로 TCP 포트 디코딩:

`tshark -d tcp.port==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8888</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http</span>

- 캡처된 출력의 형식 지정:

`tshark -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text|ps|…</span>

- 출력할 특정 필드 선택:

`tshark -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fields|ek|json|pdml</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http.request.method</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip.src</span>

- 캡처된 패킷을 [f]파일에 저장:

`tshark -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- [f]파일에서 패킷 분석:

`tshark -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>
