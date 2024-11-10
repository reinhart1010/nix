---
layout: page
title: common/tree (한국어)
description: "현재 디렉토리의 내용을 트리 형태로 표시."
content_hash: 9814c2e24a9bfdbd7f1a926893ed35d0cba74565
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tree.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tree

현재 디렉토리의 내용을 트리 형태로 표시.
더 많은 정보: <https://manned.org/tree>.

- 'num' 수준 깊이까지 파일 및 디렉토리 표시 (1은 현재 디렉토리를 의미):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수준</span>

- 디렉토리만 표시:

`tree -d`

- 숨김 파일도 색상화하여 표시:

`tree -a -C`

- 들여쓰기 선 없이 전체 경로를 표시 (인쇄할 수 없는 문자를 이스케이프하지 않으려면 `-N` 사용):

`tree -i -f`

- 각 파일의 크기와 각 디렉토리의 누적 크기를 사람이 읽기 쉬운 형식으로 표시:

`tree -s -h --du`

- 와일드카드(글로벌) 패턴을 사용하여 트리 계층 내의 파일을 표시하고, 일치하는 파일이 없는 디렉토리는 제외:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- 와일드카드(글로벌) 패턴을 사용하여 트리 계층 내의 디렉토리를 표시하고, 원하는 디렉토리의 상위 디렉토리가 아닌 디렉토리는 제외:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리_이름</span>` --matchdirs --prune`

- 주어진 디렉토리를 무시하고 트리 표시:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리_이름1|디렉토리_이름2</span>`'`
