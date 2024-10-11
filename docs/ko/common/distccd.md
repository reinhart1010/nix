---
layout: page
title: common/distccd (한국어)
description: "distcc 분산 컴파일러용 서버 데몬."
content_hash: d73c89aa90debde089fb347d08d6fbe95f83e7da
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/distccd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/distccd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># distccd

distcc 분산 컴파일러용 서버 데몬.
더 많은 정보: <https://distcc.github.io>.

- 기본 설정으로 데몬을 시작:

`distccd --daemon`

- IPv4 개인 네트워크 범위 연결을 수락해 데몬을 시작:

`distccd --daemon --allow-private`

- 특정 네트워크 주소 또는 주소 버위로부터의 연결을 수락해 데몬을 시작:

`distccd --daemon --allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소|네트워크_접두사</span>

- 한 번에 최대 4개의 작업을 실행할 수 있는 낮은 우선순위로 데몬을 시작:

`distccd --daemon --jobs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` --nice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- 데몬을 시작하고 mDNS/DNS-SD (Zeroconf)를 통해 등록:

`distccd --daemon --zeroconf`
