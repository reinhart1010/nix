---
layout: page
title: linux/adduser (한국어)
description: "사용자 추가 도구."
content_hash: 7bc2605a66f4ba326652e1ed22f6d3e4d734466a
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: suomi version
    url: /fi/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/adduser.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/adduser.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># adduser

사용자 추가 도구.
더 많은 정보: <https://manned.org/adduser>.

- 기본 홈 디렉터리를 갖춘 새 사용자 생성 및 비밀번호 설정 안내:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 홈 디렉터리 없이 새 사용자 생성:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 지정된 경로에 홈 디렉터리를 갖춘 새 사용자 생성:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/홈</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 로그인 셸로 지정된 셸을 갖춘 새 사용자 생성:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/셸</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 지정된 그룹에 속하는 새 사용자 생성:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>
