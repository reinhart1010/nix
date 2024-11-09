---
layout: page
title: linux/torify (한국어)
description: "네트워크 트래픽을 Tor 네트워크를 통해 라우팅."
content_hash: faa6aa5d977b826215fd644bc92577d10c95df73
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/torify.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/torify.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/torify.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># torify

네트워크 트래픽을 Tor 네트워크를 통해 라우팅.
참고: 이 명령은 더 이상 사용되지 않으며, 이제 `torsocks`의 하위 호환 래퍼입니다.
더 많은 정보: <https://manned.org/torify>.

- 트래픽을 Tor를 통해 라우팅:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 셸에서 Tor 토글:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Tor 사용 셸 생성:

`torify --shell`

- Tor 사용 셸 확인:

`torify show`

- Tor 설정 파일 지정:

`torify -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 특정 Tor SOCKS 프록시 사용:

`torify -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프록시</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 출력 결과를 파일로 리다이렉트:

`torify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>
