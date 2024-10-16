---
layout: page
title: common/expose (한국어)
description: "웹 사이트 공유를 위한 오픈 소스 터널 애플리케이션."
content_hash: 72b9262eab1976f7917985b1b8d188ec07c318a9
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/expose.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/expose.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># expose

웹 사이트 공유를 위한 오픈 소스 터널 애플리케이션.
더 많은 정보: <https://beyondco.de/docs/expose>.

- 인증 토큰을 등록:

`expose token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>

- 현재 작업 디렉터리를 공유:

`expose`

- 현재 작업 디렉터리를 특정 하위 도메인과 공유:

`expose --subdomain=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위도메인</span>

- 로컬 URL 공유:

`expose share `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- Expose 서버를 실행:

`expose serve`

- 특정 호스트 이름으로 Expose 서버를 실행:

`expose serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>
