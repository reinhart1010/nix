---
layout: page
title: common/autopep8 (한국어)
description: "PEP 8 스타일 가이드에 따라 Python 코드 형식을 지정."
content_hash: d45b699b2e5539b11a8a5304041e54cb27f95cf4
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/autopep8.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/autopep8.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/autopep8.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/autopep8.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/autopep8.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># autopep8

PEP 8 스타일 가이드에 따라 Python 코드 형식을 지정.
더 많은 정보: <https://github.com/hhatto/autopep8>.

- 사용자 정의 최대 줄 길이를 사용해, 파일을 `stdout`로 포맷:

`autopep8 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>` --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">길이</span>

- 변경 사항의 차이점을 표시하여, 파일을 포맷을 함:

`autopep8 --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 제자리에서, 포맷하고 변경 사항을 저장함:

`autopep8 --in-place `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 디렉토리의 모든 파일을 재귀적으로 포맷하고, 변경 사항을 저장:

`autopep8 --in-place --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>
