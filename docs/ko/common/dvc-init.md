---
layout: page
title: common/dvc-init (한국어)
description: "새로운 로컬 DVC 저장소 초기화."
content_hash: 02cd41a75991e9fb3c97c28fc2f1d7077768a1ce
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/dvc-init.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dvc init

새로운 로컬 DVC 저장소 초기화.
더 많은 정보: <https://dvc.org/doc/command-reference/init>.

- 새로운 로컬 저장소 초기화:

`dvc init`

- Git 없이 DVC 초기화:

`dvc init --no-scm`

- 하위 디렉토리에서 DVC 초기화:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/하위_디렉토리</span>` && dvc init --sudir`
