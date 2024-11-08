---
layout: page
title: common/meson (한국어)
description: "SCons와 유사한 빌드 시스템으로, Python을 프론트엔드 언어로 사용하고 Ninja를 빌드 백엔드로 사용합니다."
content_hash: 5b4c369e90f6287fd5d3aac867928b1fcb0f9d8f
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/meson.html
    icon: bi bi-globe
tldri18n_status: 2
---
# meson

SCons와 유사한 빌드 시스템으로, Python을 프론트엔드 언어로 사용하고 Ninja를 빌드 백엔드로 사용합니다.
더 많은 정보: <https://mesonbuild.com>.

- 주어진 이름과 버전으로 C 프로젝트 생성:

`meson init --language=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">c</span>` --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">내프로젝트</span>` --version=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>

- 기본값으로 `builddir` 구성:

`meson setup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">빌드_폴더</span>

- 프로젝트 빌드:

`meson compile -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/빌드_폴더</span>

- 프로젝트의 모든 테스트 실행:

`meson test`

- 도움말 표시:

`meson --help`

- 버전 표시:

`meson --version`
