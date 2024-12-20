---
layout: page
title: common/borg (한국어)
description: "중복제거 백업 도구. 파일 시스템으로 마운트할 수 있는 로컬 또는 원격 저장소를 제작."
content_hash: 0db8b61a6f1fcdd4e7e44d7ec9af7b6064f35837
last_modified_at: 2024-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/borg.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/borg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/borg.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/borg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# borg

중복제거 백업 도구. 파일 시스템으로 마운트할 수 있는 로컬 또는 원격 저장소를 제작.
더 많은 정보: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- (로컬) 저장소 초기화:

`borg init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/저장소_디렉토리/의/경로</span>

- 디렉토리를 저장소에 백업하여, "Monday"라는 아카이브 생성:

`borg create --progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/저장소_디렉토리/의/경로</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Monday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/소스_디렉토리/의/경로</span>

- 저장소의 모든 아카이브 나열:

`borg list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/저장소_디렉토리/의/경로</span>

- *.ext 파일을 제외하고 원격 저장소의 "Monday" 아카이브에서 특정 디렉토리 추출:

`borg extract `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">host</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/저장소_디렉토리/의/경로</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Monday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/타겟_디렉토리/의/경로</span>` --exclude '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>`'`

- 7일이 지난 아카이브를 모두 삭제하고, 변경 사항을 나열하여 저장소 정리:

`borg prune --keep-within `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7d</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/저장소_디렉토리/의/경로</span>

- 저장소를 FUSE 파일 시스템으로 마운트:

`borg mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/저장소_디렉토리/의/경로</span>`::`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Monday</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/마운트포인트/의/경로</span>

- 아카이브 작성에 대한 도움말 표시:

`borg create --help`
