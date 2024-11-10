---
layout: page
title: common/sc_warts2pcap (한국어)
description: "`warts` 객체에 포함된 패킷을 PCAP 파일로 작성."
content_hash: 00a3340ddc5abd882a53280efb1b3e085bb0af57
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/common/sc_warts2pcap.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sc_warts2pcap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sc_warts2pcap

`warts` 객체에 포함된 패킷을 PCAP 파일로 작성.
이는 tbit, sting 및 sniff에 대해서만 가능합니다.
더 많은 정보: <https://www.caida.org/catalog/software/scamper/>.

- 여러 `warts` 파일의 데이터를 하나의 PCAP 파일로 변환:

`sc_warts2pcap -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.warts 경로/대상/파일2.warts ...</span>

- `warts` 파일의 데이터를 PCAP 파일로 변환하고 패킷을 타임스탬프별로 정렬:

`sc_warts2pcap -s -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pcap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.warts</span>
