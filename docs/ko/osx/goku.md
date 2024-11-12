---
layout: page
title: osx/goku (한국어)
description: "Karabiner 설정 관리."
content_hash: 189f7b844777e1e17bb16a18bd7eec809e6eec81
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/goku.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/goku.html
    icon: bi bi-globe
tldri18n_status: 2
---
# goku

Karabiner 설정 관리.
더 많은 정보: <https://github.com/yqrashawn/GokuRakuJoudo>.

- 기본 설정을 사용하여 `karabiner.json` 생성:

`goku`

- 특정 `config.edn` 파일을 사용하여 `karabiner.json` 생성:

`goku --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.edn</span>

- `karabiner.json`을 업데이트하는 대신 새로운 설정을 `stdout`으로 테스트 실행:

`goku --dry-run`

- `karabiner.json`을 업데이트하는 대신 전체 설정을 `stdout`으로 테스트 실행:

`goku --dry-run-all`

- 도움말 표시:

`goku --help`

- 버전 표시:

`goku --version`
