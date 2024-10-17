---
layout: page
title: common/du (한국어)
description: "디스크 사용량: 파일 및 디렉터리 공간 사용량을 추정하고 요약."
content_hash: 85660be8c722428ce5978b1dd4e27704a6e2c5bd
last_modified_at: 2024-10-17
related_topics:
  - title: Deutsch version
    url: /de/common/du.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/du.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/du.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/du.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/du.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/du.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/du.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/du.html
    icon: bi bi-globe
tldri18n_status: 2
---
# du

디스크 사용량: 파일 및 디렉터리 공간 사용량을 추정하고 요약.
더 많은 정보: <https://www.gnu.org/software/coreutils/du>.

- 지정된 단위(B/KiB/MiB)로 디렉터리 및 하위 디렉터리의 크기를 나열:

`du -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 사람이 읽을 수 있는 형식으로 디렉터리 및 하위 디렉터리의 크기를 나열 (예: 각 크기에 적합한 단위 자동 선택 ):

`du -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 사람이 읽을 수 있는 단위로 단일 디렉터리의 크기를 표시:

`du -sh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 사람이 읽을 수 있는 디렉터리와 그 안에 있는 모든 파일 및 디렉터리의 크기를 나열:

`du -ah `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 사람이 읽을 수 있는 디렉터리 및 하위 디렉터리의 크기를 최대 N 수준까지 나열:

`du -h --max-depth=N `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 현재 디렉터리의 하위 디렉터리에 있는 모든 `.jpg` 파일의 사람이 읽을 수 있는 크기를 보여주고, 마지막에 누적 합계를 표시:

`du -ch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*/*.jpg</span>

- 특정 임계값([t]hreshold) 크기를 초과하는 모든 파일 및 디렉터리(숨겨진 디렉터리 포함)를 나열 (실제로 공간을 차지하는 것이 무엇인지 조사하는 데 유용):

`du --all --human-readable --threshold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1G|1024M|1048576K</span>` .[^.]* *`
