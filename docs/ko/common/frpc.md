---
layout: page
title: common/frpc (한국어)
description: "현재 호스트에서 프록시 연결을 시작하려면 `frps`서버에 연결."
content_hash: e553dcd93efa18a6f8d69c20a55fa90ba1fb1e68
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/frpc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/frpc.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/frpc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/frpc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# frpc

현재 호스트에서 프록시 연결을 시작하려면 `frps`서버에 연결.
`frp`의 부분.
더 많은 정보: <https://github.com/fatedier/frp>.

- 기본 구성 파일(현재 디렉터리의 `frps.ini`로 가정)을 사용하여 서비스를 시작:

`frpc`

- 현재 디렉터리에서 최신 TOML 구성 파일 (`frps.ini` 대신 `frps.toml`)을 사용하여 서비스를 시작:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` ./frps.toml`

- 특정 구성 파일을 사용하여, 서비스를 시작:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 구성 파일이 유효한지 확인:

`frpc verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-c|--config</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- Bash, fish, PowerShell 또는 Zsh에 대한 자동 완성 설정 스크립트를 출력:

`frpc completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|powershell|zsh</span>

- 버전 정보 표시:

`frpc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--version</span>
