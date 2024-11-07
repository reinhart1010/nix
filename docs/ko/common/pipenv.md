---
layout: page
title: common/pipenv (한국어)
description: "간단하고 통합된 Python 개발 워크플로우."
content_hash: 6f4c134875e28f99e11f78d0d87813e403a8a495
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pipenv.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pipenv.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pipenv.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pipenv

간단하고 통합된 Python 개발 워크플로우.
프로젝트의 패키지 및 가상 환경 관리.
더 많은 정보: <https://pypi.org/project/pipenv>.

- 새 프로젝트 생성:

`pipenv`

- Python 3를 사용하여 새 프로젝트 생성:

`pipenv --three`

- 패키지 설치:

`pipenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 프로젝트의 모든 의존성 설치:

`pipenv install`

- 프로젝트의 모든 의존성 설치 (개발 패키지 포함):

`pipenv install --dev`

- 패키지 제거:

`pipenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 생성된 가상 환경에서 쉘 시작:

`pipenv shell`

- 프로젝트의 `requirements.txt` (의존성 목록) 생성:

`pipenv lock --requirements`
