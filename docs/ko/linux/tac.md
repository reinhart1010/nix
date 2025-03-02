---
layout: page
title: linux/tac (한국어)
description: "파일의 내용을 역순으로 표시하고 연결합니다."
content_hash: 87fa35e67c3a7b9e95cc1a1a3744a0ce0c431299
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/tac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/tac.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/tac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tac

파일의 내용을 역순으로 표시하고 연결합니다.
같이 보기: `cat`.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- 특정 파일들을 역순으로 연결:

`tac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- `stdin`을 역순으로 표시:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat 경로/대상/파일</span>` | tac`

- 특정 구분자 사용:

`tac --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 정규식을 구분자로 사용:

`tac --regex --separator `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[,;]</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 각 파일 앞에 구분자 사용:

`tac --before `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>
