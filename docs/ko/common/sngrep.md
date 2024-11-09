---
layout: page
title: common/sngrep (한국어)
description: "터미널에서 SIP 호출 메시지 흐름을 표시."
content_hash: 2f81f5abbcbc29fb40ec53ba97150e86ceaaa232
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sngrep.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sngrep.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sngrep

터미널에서 SIP 호출 메시지 흐름을 표시.
더 많은 정보: <https://github.com/irontec/sngrep>.

- PCAP 파일에서 SIP 패킷 시각화:

`sngrep -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>

- PCAP 파일에서 RTP 패킷이 포함된 INVITE 패킷으로 시작하는 대화만 시각화:

`sngrep -crI `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>

- RTP 패킷이 포함된 INVITE 패킷으로 시작하는 대화만 실시간 인터페이스로 표시:

`sngrep -cr`

- 인터페이스 없이 패킷을 파일로만 캡처:

`sngrep -NO `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.pcap</span>
