---
layout: page
title: common/dvc-config (한국어)
description: "DVC 저장소의 사용자 정의 구성 옵션을 관리하는 저수준 명령어입니다."
content_hash: a7e9bd564a01d6cb2978c70e7119138611a1cc98
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-config.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc config

DVC 저장소의 사용자 정의 구성 옵션을 관리하는 저수준 명령어입니다.
이러한 구성은 프로젝트, 로컬, 글로벌 또는 시스템 수준에서 가능합니다.
더 많은 정보: <https://dvc.org/doc/command-reference/config>.

- 기본 원격 저장소의 이름 확인:

`dvc config core.remote`

- 프로젝트의 기본 원격 저장소 설정:

`dvc config core.remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 프로젝트의 기본 원격 저장소 설정 해제:

`dvc config --unset core.remote`

- 현재 프로젝트에 대해 지정된 키의 구성 값 확인:

`dvc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 프로젝트 수준에서 키의 구성 값 설정:

`dvc config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 주어진 키에 대한 프로젝트 수준 구성 값 설정 해제:

`dvc config --unset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>

- 로컬, 글로벌 또는 시스템 수준에서 구성 값 설정:

`dvc config --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">local|global|system</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>
