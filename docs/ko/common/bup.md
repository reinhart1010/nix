---
layout: page
title: common/bup (한국어)
description: "Git 팩 파일 형식을 기반으로 하는 백업 시스템, 빠른 증분 저장 및. 전역 중복 제거 기능 제공."
content_hash: 24d1924dcefd5958902c2fc32e4ba2d263f5a0d8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bup.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bup.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bup

Git 팩 파일 형식을 기반으로 하는 백업 시스템, 빠른 증분 저장 및. 전역 중복 제거 기능 제공.
더 많은 정보: <https://github.com/bup/bup>.

- 지정된 로컬 디렉토리에서 백업 저장소 초기화:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소/의/경로</span>` init`

- 백업을 수행하기 전에 지정된 디렉토리 준비:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소/의/경로</span>` index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>

- 저장소에 디렉토리 백업:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소/의/경로</span>` save -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백업명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>

- 현재 저장소에 저장된 백업 스냅샷 표시:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소/의/경로</span>` ls`

- 특정 백업 스냅샷을 목적 디렉토리에 복원:

`bup -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소/의/경로</span>` restore -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟_디렉토리/의/경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">백업명</span>
