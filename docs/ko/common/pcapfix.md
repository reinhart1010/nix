---
layout: page
title: common/pcapfix (한국어)
description: "손상되거나 손괴된 PCAP 및 PcapNG 파일 복구."
content_hash: 22064c14a6f5a7d34d1cb0e707b3782fcd68d4eb
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/pcapfix.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pcapfix.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pcapfix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pcapfix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pcapfix

손상되거나 손괴된 PCAP 및 PcapNG 파일 복구.
더 많은 정보: <https://f00l.de/pcapfix/>.

- PCAP/PCapNG 파일 복구 (참고: PCAP 파일의 경우 각 패킷의 처음 262144바이트만 스캔):

`pcapfix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcapng</span>

- 전체 PCAP 파일 복구:

`pcapfix --deep-scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>

- PCAP/PcapNG 파일을 복구하고 복구된 파일을 지정된 위치에 저장:

`pcapfix --outfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복구된파일.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>

- 지정된 파일을 자동 인식 무시하고 PcapNG 파일로 처리:

`pcapfix --pcapng `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcapng</span>

- 파일을 복구하고 과정을 자세히 표시:

`pcapfix --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>
