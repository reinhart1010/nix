---
layout: page
title: common/devenv (한국어)
description: "Nix를 사용하여 빠르고, 선언적이며, 재현 가능하고 구성 가능한 개발자 환경을 의미."
content_hash: 540cacc8d21eead5cb83f5fc86204fcf16f767bb
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/devenv.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/devenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# devenv

Nix를 사용하여 빠르고, 선언적이며, 재현 가능하고 구성 가능한 개발자 환경을 의미.
더 많은 정보: <https://devenv.sh>.

- 환경 초기화:

`devenv init`

- 완화된 기밀성 (밀폐된 상태)로 개발 환경에 진입:

`devenv shell --impure`

- 현재 환경에 대한 자세한 정보를 얻기:

`devenv info --verbose`

- `devenv`로 프로세스를 시작:

`devenv up --config /`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>`/`

- 환경 변수를 정리하고 오프라인 모드에서 쉘을 재입력:

`devenv --clean --offline`

- 이전 쉘 세대를 삭제:

`devenv gc`
