---
layout: page
title: linux/module (한국어)
description: "사용자의 환경을 module 명령어로 수정."
content_hash: 6eca5f8a2ae9b7b9bf8f848c5cd77b11b28b046f
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/module.html
    icon: bi bi-globe
tldri18n_status: 2
---
# module

사용자의 환경을 module 명령어로 수정.
더 많은 정보: <https://lmod.readthedocs.io/en/latest/010_user.html>.

- 사용 가능한 모듈 표시:

`module avail`

- 이름으로 모듈 검색:

`module avail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모듈 로드:

`module load `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 로드된 모듈 표시:

`module list`

- 특정 로드된 모듈 언로드:

`module unload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">모듈_이름</span>

- 모든 로드된 모듈 언로드:

`module purge`

- 사용자가 생성한 모듈 지정:

`module use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/모듈_파일1 경로/대상/모듈_파일2 ...</span>
