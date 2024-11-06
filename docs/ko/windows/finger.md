---
layout: page
title: windows/finger (한국어)
description: "지정된 시스템의 사용자 정보 반환."
content_hash: 59e83ef7fca3f0a7fac55cb2c05beb02a1d1cace
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/finger.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/finger.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/finger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# finger

지정된 시스템의 사용자 정보 반환.
원격 시스템은 Finger 서비스를 실행 중이어야 합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/finger>.

- 특정 사용자에 대한 정보 표시:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 지정된 호스트의 모든 사용자에 대한 정보 표시:

`finger @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 더 긴 형식으로 정보 표시:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -l`

- 도움말 정보 표시:

`finger /?`
