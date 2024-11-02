---
layout: page
title: common/pylint (한국어)
description: "Python 코드 린터."
content_hash: 33f6973d264d3348ef3affa08491fe9557948b6b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/pylint.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pylint.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pylint

Python 코드 린터.
더 많은 정보: <https://pylint.pycqa.org/en/latest/>.

- 파일 내 린트 오류 표시:

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 패키지 또는 모듈 린트 (import 가능해야 하며, `.py` 접미사 없이):

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지_또는_모듈</span>

- 디렉토리 경로에서 패키지 린트 (`__init__.py` 파일이 포함되어 있어야 함):

`pylint `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 파일을 린트하고 구성 파일 사용 (보통 `pylintrc`로 명명됨):

`pylint --rcfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/pylintrc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>

- 파일을 린트하고 특정 오류 코드를 비활성화:

`pylint --disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C,W,no-error,design</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
