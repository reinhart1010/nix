---
layout: page
title: linux/deb-get (한국어)
description: "타사 저장소 또는 직접 다운로드를 통해 배포된 `.deb` 패키지에 대한 `apt-get` 기능."
content_hash: 789cd0bd709b572360b35c77e28f96e677b605db
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/deb-get.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/deb-get.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># deb-get

타사 저장소 또는 직접 다운로드를 통해 배포된 `.deb` 패키지에 대한 `apt-get` 기능.
`apt-get`을 사용하는 Linux 배포판과 함께 작동합니다.
더 많은 정보: <https://github.com/wimpysworld/deb-get>.

- 사용 가능한 패키지 및 버전 목록 업데이트:

`deb-get update`

- 특정 패키지 검색:

`deb-get search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 정보 표시:

`deb-get show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 설치 또는 최신 버전으로 업데이트:

`deb-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 패키지 제거 (`purge`를 사용하면 구성 파일도 제거):

`deb-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지를 최신 버전으로 업그레이드:

`deb-get upgrade`

- 사용 가능한 모든 패키지 나열:

`deb-get list`
