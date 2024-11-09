---
layout: page
title: linux/microcom (한국어)
description: "최소한의 터미널 프로그램으로, 콘솔에서 시리얼, CAN 또는 텔넷 연결을 통해 원격 장치에 접근하는 데 사용됩니다."
content_hash: 3fc5066230bf91a7a6e419972b2bad6032908ba3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/microcom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/microcom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># microcom

최소한의 터미널 프로그램으로, 콘솔에서 시리얼, CAN 또는 텔넷 연결을 통해 원격 장치에 접근하는 데 사용됩니다.
더 많은 정보: <https://manned.org/microcom>.

- 지정된 전송 속도를 사용하여 시리얼 포트 열기:

`microcom --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/시리얼_포트</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전송_속도</span>

- 지정된 호스트에 텔넷 연결 설정:

`microcom --telnet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
