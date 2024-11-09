---
layout: page
title: common/todo (한국어)
description: "간단하고 표준 기반의 CLI 할 일 관리 도구."
content_hash: 282c36e8308637d0b8ac816bd423557ba9c26ba4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/todo.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/todo.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/todo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/todo.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/todo.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/todo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/todo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># todo

간단하고 표준 기반의 CLI 할 일 관리 도구.
더 많은 정보: <https://todoman.readthedocs.io>.

- 시작할 수 있는 작업 목록:

`todo list --startable`

- 작업 목록에 새 작업 추가:

`todo new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">할_일</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_목록</span>

- 지정된 ID의 작업에 위치 추가:

`todo edit --location `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">위치_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 작업에 대한 세부 정보 표시:

`todo show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 지정된 ID의 작업 완료로 표시:

`todo done `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID1 작업_ID2 ...</span>

- 작업 삭제:

`todo delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">작업_ID</span>

- 완료된 작업 삭제 및 남은 작업 ID 초기화:

`todo flush`
