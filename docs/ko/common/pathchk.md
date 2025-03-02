---
layout: page
title: common/pathchk (한국어)
description: "경로명의 유효성과 이식성을 확인합니다."
content_hash: 8043aed48c8b8b937ec8b78a26a3e8281e3f6399
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pathchk.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/pathchk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/pathchk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pathchk

경로명의 유효성과 이식성을 확인합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- 현재 시스템에서 경로명의 유효성을 확인:

`pathchk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>

- 더 넓은 범위의 POSIX 호환 시스템에서 경로명의 유효성을 확인:

`pathchk -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>

- 모든 POSIX 호환 시스템에서 경로명의 유효성을 확인:

`pathchk --portability `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>

- 빈 경로나 선행 대시(-)만 확인:

`pathchk -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로1 경로2 …</span>
