---
layout: page
title: linux/busctl (한국어)
description: "D-Bus 버스를 조사하고 모니터링합니다."
content_hash: 87e6acbde348dc65f96c45071ad9aa4101d7ef10
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/busctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# busctl

D-Bus 버스를 조사하고 모니터링합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/busctl.html>.

- 버스의 모든 피어를 서비스 이름으로 표시:

`busctl list`

- 버스 서비스, 프로세스 또는 버스 소유자의 프로세스 정보 및 자격 증명 표시 (매개변수를 지정하지 않으면):

`busctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스|프로세스_ID</span>

- 교환되는 메시지 덤프. 서비스를 지정하지 않으면 버스의 모든 메시지 표시:

`busctl monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스1 서비스2 ...</span>

- 하나 이상의 서비스(또는 서비스를 지정하지 않으면 모든 서비스)의 객체 트리 표시:

`busctl tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스1 서비스2 ...</span>

- 지정된 서비스의 특정 객체에 대한 인터페이스, 메서드, 속성 및 신호 표시:

`busctl introspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/객체</span>

- 하나 이상의 객체 속성의 현재 값 검색:

`busctl get-property `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/객체</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">속성_이름</span>

- 메서드를 호출하고 응답 표시:

`busctl call `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/객체</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메서드_이름</span>
