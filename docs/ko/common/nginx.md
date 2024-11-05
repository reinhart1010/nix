---
layout: page
title: common/nginx (한국어)
description: "Nginx 웹 서버."
content_hash: 90e07b6be6067100f048bdae51a25d9902a2fef8
last_modified_at: 2024-11-05
related_topics:
  - title: Deutsch version
    url: /de/common/nginx.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nginx.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nginx.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/nginx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nginx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nginx

Nginx 웹 서버.
더 많은 정보: <https://nginx.org/en/>.

- 기본 설정 파일로 서버 시작:

`nginx`

- 사용자 정의 설정 파일로 서버 시작:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일</span>

- 설정 파일 내 모든 상대 경로에 접두사를 붙여 서버 시작:

`nginx -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">설정_파일</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사/대상/상대/경로</span>

- 실행 중인 서버에 영향을 주지 않고 설정 테스트:

`nginx -t`

- 서버 중단 없이 설정 다시 로드:

`nginx -s reload`
