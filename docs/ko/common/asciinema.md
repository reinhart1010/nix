---
layout: page
title: common/asciinema (한국어)
description: "터미널 세션을 녹음하고 재생하며 선택적으로 asciinema.org에서 공유합니다."
content_hash: c8f32aacbb12c260117fc97f6c019e02584f0662
last_modified_at: 2024-02-15
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/asciinema.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciinema

터미널 세션을 녹음하고 재생하며 선택적으로 asciinema.org에서 공유합니다.
더 많은 정보: <https://docs.asciinema.org/manual/cli/usage>.

- `asciinema` 로컬 설치와 with an asciinema.org 계정을 연결하기:

`asciinema auth`

- 새로운 녹음을 작성 (한 번 완료되면 사용자는 업로드하거나 로컬로 저장하라는 메시지가 표시됩니다):

`asciinema rec`

- 새 녹음을 만들고 로컬 파일에 저장:

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>`.cast`

- 로컬 파일에서 녹음한 터미널을 재생:

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>`.cast`

- asciinema.org에서 호스트된 터미널 녹음을 재생:

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cast_id</span>

- 새로운 녹음을 만들어 유휴 시간을 최대 2.5초로 제한:

`asciinema rec -i 2.5`

- 로컬 저장 기록의 전체 출력을 인쇄:

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>`.cast`

- 로컬로 저장된 터미널 세션을 asciinema.org에 업로드하기:

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>`.cast`
