---
layout: page
title: linux/runuser (한국어)
description: "사용자와 그룹으로 명령을 비밀번호 없이 실행 (루트 권한 필요)."
content_hash: 3a2e36ecf1289a6a8ecca938d4d0ace15402d243
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/runuser.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/runuser.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># runuser

사용자와 그룹으로 명령을 비밀번호 없이 실행 (루트 권한 필요).
더 많은 정보: <https://manned.org/runuser>.

- 다른 사용자로 명령 실행:

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`'`

- 다른 사용자 및 그룹으로 명령 실행:

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`'`

- 특정 사용자로 로그인 셸 시작:

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -l`

- 기본 셸 대신 특정 셸을 지정하여 실행 (로그인에도 작동):

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/sh</span>

- 루트의 전체 환경을 보존 (단, `--login`이 지정되지 않은 경우에만):

`runuser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` --preserve-environment -c '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>`'`
