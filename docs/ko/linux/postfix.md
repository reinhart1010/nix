---
layout: page
title: linux/postfix (한국어)
description: "Postfix 메일 전송 에이전트(MTA) 제어 프로그램."
content_hash: 8d3845f613c9b61e044e8d42ddda2830c59a6e97
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/postfix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# postfix

Postfix 메일 전송 에이전트(MTA) 제어 프로그램.
Postfix와 통합되는 메일 전달 에이전트(MDA)인 `dovecot`도 참고하세요.
더 많은 정보: <https://www.postfix.org>.

- 설정 확인:

`sudo postfix check`

- Postfix 데몬 상태 확인:

`sudo postfix status`

- Postfix 시작:

`sudo postfix start`

- Postfix를 정상적으로 중지:

`sudo postfix stop`

- 메일 큐 비우기:

`sudo postfix flush`

- 설정 파일 다시 로드:

`sudo postfix reload`
