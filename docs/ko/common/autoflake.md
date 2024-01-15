---
layout: page
title: common/autoflake (한국어)
description: "Python 코드에서 사용하지 않는 가져오기 및 변수를 제거하는 도구."
content_hash: 24b1d4d532942c970fa3f09ef57a81401d087709
last_modified_at: 2024-01-15
related_topics:
  - title: English version
    url: /en/common/autoflake.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autoflake.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autoflake.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/autoflake.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/autoflake.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/autoflake.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/autoflake.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># autoflake

Python 코드에서 사용하지 않는 가져오기 및 변수를 제거하는 도구.
더 많은 정보: <https://github.com/myint/autoflake>.

- 단일 파일에서 사용되지 않는 변수를 제거하고 차이점을 표시:

`autoflake --remove-unused-variables `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 여러 파일에서 사용되지 않은 가져오기를 제거하고 차이점을 표시:

`autoflake --remove-all-unused-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.py 경로/대상/파일2.py ...</span>

- 파일에서 사용되지 않는 변수를 제거하고 파일을 덮어씀:

`autoflake --remove-unused-variables --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 디렉터리의 모든 파일에서 사용되지 않는 변수를 반복적으로 제거하여 각 파일을 덮어씀:

`autoflake --remove-unused-variables --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
