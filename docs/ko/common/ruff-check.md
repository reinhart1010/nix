---
layout: page
title: common/ruff-check (한국어)
description: "매우 빠른 Python 린터입니다. `check`는 기본 명령어로, 어디서든 생략 가능합니다."
content_hash: 15c2d539008fa5f5eaea5f384bd33ffd355528af
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ruff-check.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ruff-check.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ruff-check.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ruff check

매우 빠른 Python 린터입니다. `check`는 기본 명령어로, 어디서든 생략 가능합니다.
파일이나 디렉토리를 지정하지 않으면 기본적으로 현재 작업 디렉토리가 사용됩니다.
더 많은 정보: <https://docs.astral.sh/ruff/linter>.

- 지정된 파일이나 디렉토리에 대해 린터 실행:

`ruff check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...</span>

- 제안된 수정을 적용하여 파일을 직접 수정:

`ruff check --fix`

- 린터를 실행하고 변경 시 다시 린트:

`ruff check --watch`

- 설정 파일을 무시하고 지정된 규칙(또는 모든 규칙)만 활성화:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ALL|규칙_코드1,규칙_코드2,...</span>

- 추가로 지정된 규칙 활성화:

`ruff check --extend-select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_코드1,규칙_코드2,...</span>

- 지정된 규칙 비활성화:

`ruff check --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_코드1,규칙_코드2,...</span>

- `# noqa` 지시어를 추가하여 규칙의 모든 기존 위반 사항 무시:

`ruff check --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_코드</span>` --add-noqa`
