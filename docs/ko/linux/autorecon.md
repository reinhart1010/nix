---
layout: page
title: linux/autorecon (한국어)
description: "다중 스레드 네트워크 정찰 도구로, 서비스의 자동 열거를 수행합니다."
content_hash: 66d81062e69ad0d68dd17dfb1ca2bef4066031e2
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/autorecon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# autorecon

다중 스레드 네트워크 정찰 도구로, 서비스의 자동 열거를 수행합니다.
더 많은 정보: <https://github.com/Tib3rius/AutoRecon>.

- 대상 호스트에 대해 정찰 수행 (`./results`에 자세한 스캔 결과가 저장됩니다):

`sudo autorecon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_또는_IP1,호스트_또는_IP2,...</span>

- 파일에 지정된 [t]대상에 대해 정찰 수행:

`sudo autorecon --target-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다른 디렉토리에 [o]출력 결과 저장:

`sudo autorecon --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/결과</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_또는_IP1,호스트_또는_IP2,...</span>

- 특정 [p]포트 및 프로토콜로 스캔 제한 (`T`는 TCP, `U`는 UDP, `B`는 둘 다):

`sudo autorecon --ports `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">T:21-25,80,443,U:53,B:123</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_또는_IP1,호스트_또는_IP2,...</span>
