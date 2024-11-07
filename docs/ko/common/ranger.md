---
layout: page
title: common/ranger (한국어)
description: "VI 키 바인딩을 사용하는 콘솔 파일 관리자."
content_hash: 396f26deb4dd87056181e5c61f0ea2ebc5825267
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ranger.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ranger.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ranger.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ranger

VI 키 바인딩을 사용하는 콘솔 파일 관리자.
같이 보기: `clifm`, `vifm`, `mc`, `dolphin`.
더 많은 정보: <https://github.com/ranger/ranger>.

- ranger 실행:

`ranger`

- 디렉토리만 표시:

`ranger --show-only-dirs`

- 설정 디렉토리 변경:

`ranger --confdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 데이터 디렉토리 변경:

`ranger --datadir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 종료 시 CPU 사용 통계 출력:

`ranger --profile`
