---
layout: page
title: linux/tc (한국어)
description: "트래픽 제어 설정을 표시/조작합니다."
content_hash: 8f29c062fea9186c840d73262c8f3a0b5f7e16e7
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/tc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/tc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tc

트래픽 제어 설정을 표시/조작합니다.
더 많은 정보: <https://manned.org/tc>.

- 아웃바운드 패킷에 일정한 네트워크 지연 추가:

`tc qdisc add dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지연_시간_밀리초</span>`ms`

- 아웃바운드 패킷에 정규 분포된 네트워크 지연 추가:

`tc qdisc add dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">평균_지연_시간_밀리초</span>`ms `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지연_표준_편차_밀리초</span>`ms`

- 일부 패킷에 손상/손실/중복 추가:

`tc qdisc add dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">손상|손실|중복</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">효과_비율</span>`%`

- 대역폭, 버스트 속도 및 최대 지연 시간 제한:

`tc qdisc add dev eth0 root tbf rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_대역폭_메가비트</span>`mbit burst `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_버스트_속도_킬로비트</span>`kbit latency `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">드롭_전_최대_지연_시간_밀리초</span>`ms`

- 활성 트래픽 제어 정책 표시:

`tc qdisc show dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 모든 트래픽 제어 규칙 삭제:

`tc qdisc del dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>

- 트래픽 제어 규칙 변경:

`tc qdisc change dev `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eth0</span>` root netem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정책_매개변수</span>
