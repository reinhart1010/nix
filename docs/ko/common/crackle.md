---
layout: page
title: common/crackle (한국어)
description: "BLE(Bluetooth Low Energy) 암호화를 크랙하고 해독."
content_hash: af6d00ac7f18b513d0fdc909415cec5003df9274
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/crackle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/crackle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/crackle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># crackle

BLE(Bluetooth Low Energy) 암호화를 크랙하고 해독.
더 많은 정보: <https://github.com/mikeryan/crackle>.

- 녹음된 BLE 통신에 임시 키(TK)를 복구하는 데 필요한 패킷이 포함되어 있는지 확인:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pcap</span>

- 무차별 대입을 사용해 기록된 페어링 이벤트의 TK를 복구하고 이를 사용하여 모든 후속 통신을 해독:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복호화데이터.pcap</span>

- 지정된 장기 키 (LTK)를 사용하여 녹음된 통신을 해독:

`crackle -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.pcap</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복호화데이터.pcap</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">81b06facd90fe7a6e9bbd9cee59736a7</span>
