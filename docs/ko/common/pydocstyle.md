---
layout: page
title: common/pydocstyle (한국어)
description: "Python 스크립트가 Python 도크스트링 규칙을 준수하는지 정적 검사합니다."
content_hash: a8a0ebf9c8bd95eb197586c79f97a56fc5fb861e
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pydocstyle.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/pydocstyle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pydocstyle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pydocstyle

Python 스크립트가 Python 도크스트링 규칙을 준수하는지 정적 검사합니다.
더 많은 정보: <https://www.pydocstyle.org/en/latest/>.

- Python 스크립트 또는 특정 디렉터리의 모든 Python 스크립트 분석:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>

- 각 오류에 대한 설명 표시:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--explain</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>

- 디버그 정보 표시:

`pydocstyle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--debug</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>

- 총 오류 수 표시:

`pydocstyle --count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>

- 특정 구성 파일 사용:

`pydocstyle --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/구성_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>

- 하나 이상의 오류 무시:

`pydocstyle --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">D101,D2,D107,...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>

- 특정 규약의 오류 검사:

`pydocstyle --convention `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pep257|numpy|google</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.py|경로/대상/폴더</span>
