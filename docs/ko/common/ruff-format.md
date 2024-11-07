---
layout: page
title: common/ruff-format (한국어)
description: "매우 빠른 Python 코드 포매터."
content_hash: b76ec7566a1d9f60f2db04137b5964c582193784
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ruff-format.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ruff-format.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ruff-format.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ruff format

매우 빠른 Python 코드 포매터.
파일이나 디렉토리가 지정되지 않으면 기본적으로 현재 작업 디렉토리가 사용됩니다.
더 많은 정보: <https://docs.astral.sh/ruff/formatter>.

- 지정된 파일이나 디렉토리를 직접 포맷:

`ruff format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더1 경로/대상/파일_또는_폴더2 ...</span>

- 수정될 파일을 출력하고, 포맷이 필요한 파일이 있으면 0이 아닌 종료 코드를 반환하며, 그렇지 않으면 0을 반환:

`ruff format --check`

- 파일을 수정하지 않고 어떤 변경이 이루어질지 출력:

`ruff format --diff`
