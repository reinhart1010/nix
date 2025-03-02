---
layout: page
title: common/speedtest (한국어)
description: "<https://speedtest.net>을 사용하여 인터넷 대역폭을 테스트하는 공식 명령줄 인터페이스."
content_hash: 283a72610fa5d97a8c2f64ed6518d034ad6fb3f1
last_modified_at: 2024-11-13
related_topics:
  - title: English version
    url: /en/common/speedtest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# speedtest

<https://speedtest.net>을 사용하여 인터넷 대역폭을 테스트하는 공식 명령줄 인터페이스.
참고: 일부 플랫폼에서는 `speedtest`를 `speedtest-cli`에 연결합니다. 이 페이지의 일부 예제가 작동하지 않는 경우, `speedtest-cli`를 참조하세요.
더 많은 정보: <https://www.speedtest.net/apps/cli>.

- 속도 테스트 실행:

`speedtest`

- 속도 테스트를 실행하고 출력 단위를 지정:

`speedtest --unit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes</span>

- 속도 테스트를 실행하고 출력 형식을 지정:

`speedtest --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">human-readable|csv|tsv|json|jsonl|json-pretty</span>

- 속도 테스트를 실행하고 소수점 자릿수를 지정 (0에서 8까지, 기본값은 2):

`speedtest --precision=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정밀도</span>

- 속도 테스트를 실행하고 진행 상황을 출력 (출력 형식이 `human-readable` 및 `json`일 때만 사용 가능):

`speedtest --progress=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yes|no</span>

- 거리에 따라 정렬된 모든 `speedtest.net` 서버 나열:

`speedtest --servers`

- 특정 `speedtest.net` 서버로 속도 테스트 실행:

`speedtest --server-id=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버_ID</span>
