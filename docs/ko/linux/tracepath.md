---
layout: page
title: linux/tracepath (한국어)
description: "네트워크 호스트로의 경로를 추적하여 이 경로를 따라 MTU를 발견합니다."
content_hash: d01794ce812ab4794cbfe8964558549a3fee19ba
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tracepath.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tracepath.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tracepath

네트워크 호스트로의 경로를 추적하여 이 경로를 따라 MTU를 발견합니다.
더 많은 정보: <https://manned.org/tracepath>.

- 호스트로의 경로를 추적하는 권장 방법:

`tracepath -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">33434</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 초기 목적지 포트 지정 (비표준 방화벽 설정에 유용):

`tracepath -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">목적지_포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 호스트명과 숫자 IP 주소 둘 다 출력:

`tracepath -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 최대 TTL(홉 수) 지정:

`tracepath -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_홉수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 초기 패킷 길이 지정 (IPv4의 경우 기본값은 65535, IPv6의 경우 128000):

`tracepath -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패킷_길이</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- IPv6 주소만 사용:

`tracepath -6 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>
