---
layout: page
title: common/tlmgr-repository (한국어)
description: "TeX Live 설치의 저장소를 관리합니다."
content_hash: 417c19b86a806041e40ea674973a6f7fa5a9eaee
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/tlmgr-repository.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tlmgr-repository.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tlmgr repository

TeX Live 설치의 저장소를 관리합니다.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- 모든 설정된 저장소와 해당 태그(설정된 경우)를 나열:

`tlmgr repository list`

- 특정 저장소에서 사용할 수 있는 모든 패키지를 나열:

`tlmgr repository list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로|url|태그</span>

- 특정 태그와 함께 새 저장소 추가 (태그는 필수 아님):

`sudo tlmgr repository add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로|url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 특정 저장소 제거:

`sudo tlmgr repository remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로|url|태그</span>

- 새로운 저장소 목록 설정, 이전 목록 덮어쓰기:

`sudo tlmgr repository set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로|url|태그</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로|url|태그</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">...</span>

- 모든 설정된 저장소의 검증 상태 표시:

`tlmgr repository status`
