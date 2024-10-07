---
layout: page
title: common/git-cola (한국어)
description: "강력하고 직관적인 사용자 인터페이스를 갖춘 Git GUI."
content_hash: d66c80414f6e394c607b478b64567ef3ddb8b969
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/common/git-cola.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-cola.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/git-cola.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-cola.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git cola

강력하고 직관적인 사용자 인터페이스를 갖춘 Git GUI.
더 많은 정보: <https://git-cola.readthedocs.io>.

- GUI 시작:

`git cola`

- 수정 모드에서 GUI 시작:

`git cola --amend`

- Git 저장소를 묻기. 기본값은 현재 디렉토리:

`git cola --prompt`

- 지정된 경로의 Git 저장소 열기:

`git cola --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/git-저장소</span>

- 상태 위젯에 경로 필터 적용:

`git cola --status-filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필터</span>
