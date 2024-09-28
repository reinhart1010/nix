---
layout: page
title: common/bfs (한국어)
description: "파일에 대한 너비 우선 검색."
content_hash: 173caa363bbc22cf4c5fa64488057f0845b71cba
last_modified_at: 2024-09-28
related_topics:
  - title: English version
    url: /en/common/bfs.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bfs

파일에 대한 너비 우선 검색.
더 많은 정보: <https://manned.org/bfs>.

- 확장자로 파일 찾기:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- 여러 경로/이름 패턴과 일치하는 파일 찾기:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">**/경로/**/*.ext</span>`' -or -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*패턴*</span>`'`

- 대소문자를 구분하지 않는 모드에서, 주어진 이름과 일치하는 디렉터리를 찾음:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -type d -iname '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*lib*</span>`'`

- 특정 경로를 제외하고 주어진 패턴과 일치하는 파일을 찾음:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.py</span>`' -not -path '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/사이트-패키지/*</span>`'`

- 재귀 깊이를 "1"로 제한하여 지정된 크기 범위와 일치하는 파일을 찾음:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -maxdepth 1 -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+500k</span>` -size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-10M</span>

- 각 파일에 대해 명령을 실행 (파일 이름에 접근하려면 명령 내에서 `{}` 사용):

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -name '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`' -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l</span>` {} \;`

- 오늘 수정된 모든 파일을 찾아, 결과를 단일 명령에 인수로 전달:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -daystart -mtime `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1</span>` -exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tar -cvf archive.tar</span>` {} \+`

- 빈 파일 (0 바이트) 또는 디렉터리를 찾아 상세하게 삭제:

`bfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">루트_경로</span>` -type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f|d</span>` -empty -delete -print`
