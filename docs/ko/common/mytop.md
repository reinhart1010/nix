---
layout: page
title: common/mytop (한국어)
description: "MySQL 서버 성능 정보를 `top`처럼 표시."
content_hash: 4d15da1e4dada204764efae24bb311ae3ae19c5f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mytop.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mytop.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mytop

MySQL 서버 성능 정보를 `top`처럼 표시.
더 많은 정보: <https://jeremy.zawodny.com/mysql/mytop/mytop.html>.

- `mytop` 시작:

`mytop`

- 지정된 사용자 이름과 비밀번호로 연결:

`mytop -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 지정된 사용자 이름으로 연결 (비밀번호 입력이 요청됨):

`mytop -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --prompt`

- 유휴(대기) 스레드를 표시하지 않음:

`mytop -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --noidle`
