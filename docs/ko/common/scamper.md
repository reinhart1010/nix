---
layout: page
title: common/scamper (한국어)
description: "인터넷을 능동적으로 탐색하여 토폴로지와 성능을 분석."
content_hash: 9f2fc8d1ce599aa84b24481d5f54d3f03f78ccbf
last_modified_at: 2024-11-09
related_topics:
  - title: Deutsch version
    url: /de/common/scamper.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/scamper.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/scamper.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scamper

인터넷을 능동적으로 탐색하여 토폴로지와 성능을 분석.
`sc_`로 시작하는 몇 가지 도구를 포함, 예를 들어 `sc_warts2text` 또는 `sc_ttlexp`.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 목적지에 표준 옵션(트레이서트) 실행:

`scamper -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>

- 두 가지 작업(핑 및 트레이서트)을 두 개의 다른 대상에 실행:

`scamper -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>`" -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.2</span>`"`

- 여러 호스트에 UDP로 핑, 첫 번째 핑에 특정 포트 번호를 사용하고 각 후속 핑마다 증가:

`scamper -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UDP-목적지_포트</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33434</span>`" -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.2</span>

- 다중 경로 발견 알고리즘(MDA)을 사용하여 목적지로의 로드 밸런싱 경로 존재 여부를 결정하고 ICMP 에코 패킷을 사용하여 최대 세 번 시도하여 샘플링한 결과를 `warts` 파일에 기록:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.warts</span>` -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tracelb</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ICMP-echo</span>` -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.0.2.1</span>`"`

- 목적지에 ICMP로 파리 트레이서트 실행하고 결과를 압축된 `warts` 파일에 저장:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts.gz</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.warts</span>` -I "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trace</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">icmp-paris</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:beaf::4</span>`"`

- 특정 IP 주소에 도착하는 모든 ICMP 패킷과 특정 ICMP ID를 `warts` 파일에 기록:

`scamper -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">warts</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.warts</span>` -I "sniff -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2001:db8:dead:beef::6</span>` icmp[icmpid] == `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">101</span>`"`
