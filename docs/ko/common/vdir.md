---
layout: page
title: common/vdir (한국어)
description: "디렉토리 내용 나열."
content_hash: 0011e88f0c445a6e12ed9790877b0af881b9dab4
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/vdir.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vdir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vdir

디렉토리 내용 나열.
`ls -l`의 대체품.
더 많은 정보: <https://www.gnu.org/software/coreutils/vdir>.

- 현재 디렉토리의 파일 및 디렉토리를 한 줄에 하나씩 자세히 나열:

`vdir`

- 사람이 읽기 쉬운 단위(KB, MB, GB)로 크기를 표시하여 나열:

`vdir -h`

- 숨김 파일(점으로 시작하는 파일) 포함 나열:

`vdir -a`

- 크기별로 항목을 정렬하여 파일 및 디렉토리 나열 (가장 큰 것부터):

`vdir -S`

- 수정 시간별로 항목을 정렬하여 파일 및 디렉토리 나열 (가장 최근 것부터):

`vdir -t`

- 디렉토리를 먼저 그룹화하여 나열:

`vdir --group-directories-first`

- 특정 디렉토리의 모든 파일 및 디렉토리를 재귀적으로 나열:

`vdir --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
