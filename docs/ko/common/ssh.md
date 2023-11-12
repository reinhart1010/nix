---
layout: page
title: common/ssh (한국어)
description: "보안 쉘은 원격 시스템에 안전하게 로그인하는 데 사용되는 프로토콜입니다."
content_hash: 996066f9fb51ffe8963355247348d60cc9636693
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/ssh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ssh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh

보안 쉘은 원격 시스템에 안전하게 로그인하는 데 사용되는 프로토콜입니다.
원격 서버에서 명령을 기록하거나 실행하는 데 사용할 수 있습니다.
더 많은 정보: <https://man.openbsd.org/ssh>.

- 원격 서버에 연결:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 특정 인증정보(개인 키)를 사용하여 원격 서버에 연결:

`ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 특정 포트를 사용하여 원격 서버에 연결:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>

- 원격 명령과의 상호 작용을 허용하는 [t]ty 할당을 사용하여 원격 서버에서 명령을 실행:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자</span>

- SSH 터널링: 동적 포트 전달 (`localhost:1080`의 SOCKS 프록시):

`ssh -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- SSH 터널링: 원격 명령의 의사-[T]ty 할당 및 실행(executio[N])의 비활성화와 함께 특정 포트(`localhost:9999`를 `example.org:80`):

`ssh -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -N -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- SSH 점프: 점프 호스트를 통해 원격 서버에 연결(여러 점프 홉은 쉼표 문자로 구분하여 지정):

`ssh -J `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">점프_호스트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>

- 에이전트 전달: 인증 정보를 원격 시스템으로 전달(사용 가능한 옵션은 `man ssh_config` 참조):

`ssh -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자 명</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_호스트</span>
