---
layout: page
title: common/pip-install (한국어)
description: "Python 패키지 설치."
content_hash: 7fe88311f4e29af888b93cdd6a82eb5098c177d9
last_modified_at: 2024-11-07
related_topics:
  - title: Deutsch version
    url: /de/common/pip-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip-install.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pip-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pip-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pip install

Python 패키지 설치.
더 많은 정보: <https://pip.pypa.io>.

- 패키지 설치:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 특정 버전의 패키지 설치:

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 파일에 나열된 패키지 설치:

`pip install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/requirements.txt</span>

- URL 또는 로컬 파일 아카이브(.tar.gz | .whl)에서 패키지 설치:

`pip install --find-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>

- 현재 디렉토리에 있는 로컬 패키지를 개발(수정 가능) 모드로 설치:

`pip install --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
