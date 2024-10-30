---
layout: page
title: common/grip (한국어)
description: "GitHub 기반 Markdown 파일을 로컬에서 미리 볼 수 있음."
content_hash: dcb98059414dc53e7e5320b4661bde8abf6e8f28
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/grip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/grip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># grip

GitHub 기반 Markdown 파일을 로컬에서 미리 볼 수 있음.
더 많은 정보: <https://github.com/joeyespo/grip>.

- 서버를 시작하고 현재 디렉터리의 렌더링된 `README` 파일을 제공:

`grip`

- 서버를 시작하고 특정 Markdown 파일을 제공:

`grip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.md</span>

- 서버를 시작하고 브라우저에서 현재 디렉터리의 `README` 파일을 열기:

`grip --browser`

- 지정된 포트에서 서버를 시작하고 현재 디렉터리의 렌더링된 `README` 파일을 제공:

`grip `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
