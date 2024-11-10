---
layout: page
title: linux/uuidparse (한국어)
description: "범용 고유 식별자(UUID) 파싱."
content_hash: c5b18b8705792d45af6241d7216880738ead3b04
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/uuidparse.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uuidparse

범용 고유 식별자(UUID) 파싱.
같이 보기: `uuidgen`.
더 많은 정보: <https://manned.org/uuidparse.1>.

- 지정된 UUID를 파싱하고 표 형식으로 출력:

`uuidparse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- `stdin`에서 UUID 파싱:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | uuidparse`

- JSON 출력 형식 사용:

`uuidparse --json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- 헤더 줄을 출력하지 않음:

`uuidparse --noheadings `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- 원시 출력 형식 사용:

`uuidparse --raw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid1 uuid2 ...</span>

- 출력할 네 가지 열을 지정:

`uuidparse --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID,VARIANT,TYPE,TIME</span>

- 도움말 표시:

`uuidparse -h`
