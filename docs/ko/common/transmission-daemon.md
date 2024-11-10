---
layout: page
title: common/transmission-daemon (한국어)
description: "`transmission-remote` 또는 웹 인터페이스로 제어되는 데몬."
content_hash: 7be91d24737db1f14ca1c8991cd3c31094544ec3
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/transmission-daemon.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-daemon.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/transmission-daemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-daemon

`transmission-remote` 또는 웹 인터페이스로 제어되는 데몬.
같이 보기: `transmission`.
더 많은 정보: <https://manned.org/transmission-daemon>.

- 헤드리스 `transmission` 세션 시작:

`transmission-daemon`

- 특정 디렉터리를 감시하여 새로운 토렌트를 시작:

`transmission-daemon --watch-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- JSON 형식으로 데몬 설정 덤프:

`transmission-daemon --dump-settings > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.json</span>

- 웹 인터페이스에 대한 특정 설정으로 시작:

`transmission-daemon --auth --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9091</span>` --allowed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>
