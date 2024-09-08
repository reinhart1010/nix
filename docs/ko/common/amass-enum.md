---
layout: page
title: common/amass-enum (한국어)
description: "도메인의 하위 도메인 찾기."
content_hash: 45f505f9abf6e9c5400febdafdc265f3f58208d5
last_modified_at: 2024-09-08
related_topics:
  - title: English version
    url: /en/common/amass-enum.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/amass-enum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-enum.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/amass-enum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-enum.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/amass-enum.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># amass enum

도메인의 하위 도메인 찾기.
더 많은 정보: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- 도메인([d]omain)의 하위 도메인을 (수동적으로) 찾기:

`amass enum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 도메인([d]omain)의 하위 도메인을 찾아 발견된 하위 도메인을 해결하려고 시도하면서, 적극적으로 확인:

`amass enum -active -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80,443,8080</span>

- 하위 도메인(sub[d]omains)에 대한 무차별 대입 검색을 수행:

`amass enum -brute -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 결과를 텍스트 파일에 저장:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 터미널 출력을 파일에 저장하고 기타 자세한 출력을 디렉터리에 저장:

`amass enum -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` -dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인_이름</span>

- 사용 가능한 모든 데이터 소스 나열:

`amass enum -list`
