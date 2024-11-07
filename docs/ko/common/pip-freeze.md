---
layout: page
title: common/pip-freeze (한국어)
description: "설치된 패키지를 요구 사항 형식으로 나열."
content_hash: 5aef0d841cc820bc0c7c6cab7828cfdd20fd1810
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pip-freeze.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pip-freeze.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pip freeze

설치된 패키지를 요구 사항 형식으로 나열.
더 많은 정보: <https://pip.pypa.io/en/stable/cli/pip_freeze>.

- 설치된 패키지 나열:

`pip freeze`

- 설치된 패키지를 나열하고 `requirements.txt` 파일에 작성:

`pip freeze > requirements.txt`

- 가상 환경에서 설치된 패키지를 나열하고, 전역적으로 설치된 패키지를 제외:

`pip freeze --local > requirements.txt`

- 사용자 사이트에 설치된 패키지 나열:

`pip freeze --user > requirements.txt`

- `pip`, `distribute`, `setuptools`, `wheel`을 포함한 모든 패키지 나열 (기본적으로 생략됨):

`pip freeze --all > requirements.txt`
