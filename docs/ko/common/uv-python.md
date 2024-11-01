---
layout: page
title: common/uv-python (한국어)
description: "Python 버전 및 설치 관리."
content_hash: ed8bc539c16e63999655e8d3d8d29a0fdc150685
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/uv-python.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/uv-python.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uv-python.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uv python

Python 버전 및 설치 관리.
더 많은 정보: <https://docs.astral.sh/uv/reference/cli/#uv-python>.

- 사용 가능한 모든 Python 설치 목록:

`uv python list`

- Python 버전 설치:

`uv python install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- Python 버전 제거:

`uv python uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- Python 설치 검색:

`uv python find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 현재 프로젝트를 특정 Python 버전을 사용하도록 고정:

`uv python pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- `uv` Python 설치 디렉터리 표시:

`uv python dir`
