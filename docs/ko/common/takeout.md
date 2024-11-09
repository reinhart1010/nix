---
layout: page
title: common/takeout (한국어)
description: "Docker 기반의 개발 전용 의존성 관리자."
content_hash: 2089e7c6423238ce1f1a9eabca1e8273a161bf2e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/takeout.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/takeout.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># takeout

Docker 기반의 개발 전용 의존성 관리자.
더 많은 정보: <https://github.com/tighten/takeout>.

- 사용 가능한 서비스 목록 표시:

`takeout enable`

- 특정 서비스 활성화:

`takeout enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 기본 매개변수로 특정 서비스 활성화:

`takeout enable --default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 활성화된 서비스 목록 표시:

`takeout disable`

- 특정 서비스 비활성화:

`takeout disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 모든 서비스 비활성화:

`takeout disable --all`

- 특정 컨테이너 시작:

`takeout start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_ID</span>

- 특정 컨테이너 중지:

`takeout stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_ID</span>
