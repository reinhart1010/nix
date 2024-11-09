---
layout: page
title: linux/foreman (한국어)
description: "Procfile 기반 애플리케이션 관리 도구."
content_hash: 46d05faf05c88acfbb48ad4a2859418f9d38a9c1
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/foreman.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/foreman.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># foreman

Procfile 기반 애플리케이션 관리 도구.
더 많은 정보: <https://manned.org/foreman>.

- 현재 디렉토리의 Procfile로 애플리케이션 시작:

`foreman start`

- 지정된 Procfile로 애플리케이션 시작:

`foreman start -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Procfile</span>

- 특정 애플리케이션 시작:

`foreman start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스</span>

- Procfile 형식 검증:

`foreman check`

- 프로세스 환경과 함께 일회성 명령 실행:

`foreman run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- "worker"라는 이름의 프로세스를 제외한 모든 프로세스 시작:

`foreman start -m all=1,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker</span>`=0`
