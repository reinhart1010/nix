---
layout: page
title: common/l2ping (한국어)
description: "L2CAP 에코 요청을 보내고 응답을 받습니다."
content_hash: 53fc1701bdac6a4c330b7e15ce0241d5d6502911
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/l2ping.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/l2ping.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># l2ping

L2CAP 에코 요청을 보내고 응답을 받습니다.
더 많은 정보: <https://manned.org/l2ping>.

- 블루투스 장치에 핑:

`sudo l2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>

- 블루투스 장치에 역방향 핑:

`sudo l2ping -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>

- 지정된 인터페이스에서 블루투스 장치에 핑:

`sudo l2ping -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hci0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>

- 지정된 크기의 데이터 패키지로 블루투스 장치에 핑:

`sudo l2ping -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>

- 블루투스 장치에 핑 플러드:

`sudo l2ping -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>

- 블루투스 장치에 지정된 횟수만큼 핑:

`sudo l2ping -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">횟수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>

- 요청 간의 지정된 지연으로 블루투스 장치에 핑:

`sudo l2ping -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac_주소</span>
