---
layout: page
title: common/sngrep (한국어)
description: "터미널에서 SIP 호출 메시지 흐름을 표시."
content_hash: 2f81f5abbcbc29fb40ec53ba97150e86ceaaa232
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sngrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sngrep

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
