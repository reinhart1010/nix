---
layout: page
title: common/surge (한국어)
description: "간단한 웹 게시."
content_hash: ddfbe10ae2ad5e694f37e76997abe8189fa4fc97
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/surge.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/surge.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># surge

간단한 웹 게시.
더 많은 정보: <https://surge.sh>.

- 새로운 사이트를 surge.sh에 업로드:

`surge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/내_프로젝트</span>

- 사용자 지정 도메인으로 사이트 배포 (DNS 레코드는 surge.sh 하위 도메인을 가리켜야 함):

`surge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/내_프로젝트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_사용자_도메인.com</span>

- surge 프로젝트 나열:

`surge list`

- 프로젝트 제거:

`surge teardown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내_사용자_도메인.com</span>
