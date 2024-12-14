---
layout: page
title: common/comm (한국어)
description: "두 파일의 공통되는 줄을 선택하거나 거절합니다."
content_hash: eec7652f2b416d9fab23b8e0769136c24910309b
last_modified_at: 2024-12-14
related_topics:
  - title: English version
    url: /en/common/comm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/comm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/comm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comm

두 파일의 공통되는 줄을 선택하거나 거절합니다.
두 파일 모두 정렬되어 있어야합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>.

- 세 개의 탭으로 구분된 열을 생성합니다: 첫 번째 파일에는 줄만, 두 번째 파일에서는 줄들과 공통 줄:

`comm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 두 파일의 공통된 줄들만 출력:

`comm -12 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- `stdin`으로 읽어드린 하나의 파일과 나머지 파일의 공통된 줄들만 출력:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` | comm -12 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>

- 첫 번째 파일에서만 줄을 가져오고 결과를 세 번째 파일에 저장:

`comm -23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1_only</span>

- 파일이 정렬되지 않은 경우 두 번째 파일에서만 줄을 출력합니다:

`comm -13 <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>`) <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>`)`
