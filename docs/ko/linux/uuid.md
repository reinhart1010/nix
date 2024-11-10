---
layout: page
title: linux/uuid (한국어)
description: "범용 고유 식별자(UUID) 생성 및 디코드."
content_hash: 90fb9ee0210729c24a93efc14924cfee4d350d58
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/uuid.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/uuid.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uuid

범용 고유 식별자(UUID) 생성 및 디코드.
같이 보기: `uuidgen`.
더 많은 정보: <https://manned.org/uuid>.

- UUIDv1 생성 (시간 및 시스템의 하드웨어 주소 기반, 사용 가능한 경우):

`uuid`

- UUIDv4 생성 (무작위 데이터 기반):

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>

- 여러 개의 UUIDv4를 한 번에 생성:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UUID_개수</span>

- UUIDv4를 생성하고 출력 형식 지정:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BIN|STR|SIV</span>

- UUIDv4를 생성하고 출력을 파일에 저장:

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 네임스페이스 접두사로 UUIDv5 생성 (제공된 객체 이름 기반):

`uuid -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` ns:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DNS|URL|OID|X500</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">객체_이름</span>

- 주어진 UUID 디코드:

`uuid -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>
