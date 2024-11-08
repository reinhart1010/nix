---
layout: page
title: common/psgrep (한국어)
description: "실행 중인 프로세스를 `grep`으로 검색."
content_hash: a3306ffca6d17e68a777b3d2855e814e87f99bb1
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/psgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# psgrep

실행 중인 프로세스를 `grep`으로 검색.
더 많은 정보: <https://jvz.github.io/psgrep>.

- 특정 문자열이 포함된 프로세스 라인 찾기:

`psgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 헤더를 제외하고 특정 문자열이 포함된 프로세스 라인 찾기:

`psgrep -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 간단한 형식으로 검색 (PID, 사용자, 명령어):

`psgrep -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>
