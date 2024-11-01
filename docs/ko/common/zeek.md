---
layout: page
title: common/zeek (한국어)
description: "패시브 네트워크 트래픽 분석기."
content_hash: 6fe639a9d95d10edfbd1212af47f306e690d1640
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zeek.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zeek.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zeek

패시브 네트워크 트래픽 분석기.
출력 및 로그 파일은 현재 작업 디렉토리에 저장됩니다.
더 많은 정보: <https://docs.zeek.org/en/lts/quickstart.html#zeek-as-a-command-line-utility>.

- 네트워크 인터페이스에서 실시간 트래픽 분석:

`sudo zeek --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 네트워크 인터페이스에서 실시간 트래픽 분석 및 사용자 지정 스크립트 로드:

`sudo zeek --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트2</span>

- 네트워크 인터페이스에서 실시간 트래픽 분석, 스크립트 로드 없이:

`sudo zeek --bare-mode --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 네트워크 인터페이스에서 `tcpdump` 필터를 적용하여 실시간 트래픽 분석:

`sudo zeek --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/필터</span>` --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- 네트워크 인터페이스에서 워치독 타이머를 사용하여 실시간 트래픽 분석:

`sudo zeek --watchdog --iface `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>

- PCAP 파일에서 트래픽 분석:

`zeek --readfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.trace</span>
