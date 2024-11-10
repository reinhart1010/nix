---
layout: page
title: linux/uuidgen (한국어)
description: "고유 식별자(UUID)를 생성합니다."
content_hash: 08e5b8c767674e0e88d5cc348440e5a957bcb7d5
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/uuidgen.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/uuidgen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uuidgen

고유 식별자(UUID)를 생성합니다.
같이 보기: `uuid`.
더 많은 정보: <https://manned.org/uuidgen>.

- 무작위 UUIDv4 생성:

`uuidgen --random`

- 현재 시간을 기반으로 UUIDv1 생성:

`uuidgen --time`

- 지정된 네임스페이스 접두사를 가진 이름의 UUIDv5 생성:

`uuidgen --sha1 --namespace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@dns|@url|@oid|@x500</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_이름</span>
