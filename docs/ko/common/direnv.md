---
layout: page
title: common/direnv (한국어)
description: "현재 디렉터리에 따라 환경 변수를 로드 및 언로드하는 쉘 확장."
content_hash: 2ec876bd7c3adfab43fb70706f5914baefb68f77
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/direnv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/direnv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/direnv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# direnv

현재 디렉터리에 따라 환경 변수를 로드 및 언로드하는 쉘 확장.
더 많은 정보: <https://github.com/direnv/direnv>.

- 현재 디렉터리에 있는 `.envrc`를 로드하려면 direnv 권한을 부여:

`direnv allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 현재 디렉터리에 있는`.envrc`를 로드하기 위한 인증을 취소:

`direnv deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 기본 텍스트 편집기에서 `.envrc` 파일을 편집하고 종료 시 환경을 다시 로드:

`direnv edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- 환경 다시 로드를 트리거:

`direnv reload`

- 일부 디버그 상태 정보를 출력:

`direnv status`
