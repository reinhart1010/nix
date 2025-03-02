---
layout: page
title: linux/pw-dump (한국어)
description: "PipeWire의 현재 상태를 노드, 장치, 모듈, 포트 및 기타 객체 정보를 포함하여 JSON 형식으로 덤프."
content_hash: c9574b18587c1375a4e268f825b1b5e9affe74f2
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/pw-dump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-dump.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># pw-dump

PipeWire의 현재 상태를 노드, 장치, 모듈, 포트 및 기타 객체 정보를 포함하여 JSON 형식으로 덤프.
같이 보기: `pw-mon`.
더 많은 정보: <https://docs.pipewire.org/page_man_pw-dump_1.html>.

- 기본 PipeWire 인스턴스의 현재 상태를 JSON 형식으로 출력:

`pw-dump`

- 현재 상태를 덤프하고, 변경 사항을 [m]onitoring하여 다시 출력:

`pw-dump --monitor`

- 원격 인스턴스의 현재 상태를 [r]emote하여 파일에 덤프:

`pw-dump --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/덤프_파일.json</span>

- [C]olor 설정 구성:

`pw-dump --color `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">never|always|auto</span>

- 도움말 표시:

`pw-dump --help`
