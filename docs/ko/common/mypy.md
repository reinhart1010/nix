---
layout: page
title: common/mypy (한국어)
description: "Python 코드의 타입을 검사."
content_hash: da80a0881939824a1d51e4cb86cf258f9d9a6813
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mypy.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/mypy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mypy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mypy

Python 코드의 타입을 검사.
더 많은 정보: <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- 특정 파일의 타입 검사:

`mypy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 특정 [m]모듈의 타입 검사:

`mypy -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 특정 [p]패키지의 타입 검사:

`mypy -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_이름</span>

- 코드 문자열의 타입 검사:

`mypy -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코드</span>`"`

- 누락된 import 무시:

`mypy --ignore-missing-imports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 자세한 오류 메시지 표시:

`mypy --show-traceback `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 사용자 지정 구성 파일 지정:

`mypy --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>

- [h]도움말 표시:

`mypy -h`
