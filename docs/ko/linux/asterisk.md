---
layout: page
title: linux/asterisk (한국어)
description: "전화 및 교환기(전화) 서버 인스턴스를 실행하고 관리합니다."
content_hash: ded3de4867ee322847a53dd7c5e5029fedf34d46
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/asterisk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/asterisk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/asterisk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># asterisk

전화 및 교환기(전화) 서버 인스턴스를 실행하고 관리합니다.
더 많은 정보: <https://docs.asterisk.org>.

- 실행 중인 서버에 [r]재연결하고, 3단계의 [v]자세히 로깅을 활성화:

`asterisk -r -vvv`

- 실행 중인 서버에 [r]재연결하여 단일 명령을 실행하고 반환:

`asterisk -r -x "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>`"`

- chan_SIP 클라이언트(전화) 표시:

`asterisk -r -x "sip show peers"`

- 활성 통화 및 채널 표시:

`asterisk -r -x "core show channels"`

- 음성 사서함 표시:

`asterisk -r -x "voicemail show users"`

- 채널 종료:

`asterisk -r -x "hangup request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">채널_ID</span>`"`

- chan_SIP 구성 다시 로드:

`asterisk -r -x "sip reload"`
