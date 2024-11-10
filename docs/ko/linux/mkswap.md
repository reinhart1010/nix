---
layout: page
title: linux/mkswap (한국어)
description: "디바이스나 파일에 Linux 스왑 영역을 설정합니다."
content_hash: bbb0920684d55e7c96811d0a3269b872fa7e08fa
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mkswap.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkswap

디바이스나 파일에 Linux 스왑 영역을 설정합니다.
참고: `path/to/file`은 일반 파일 또는 스왑 파티션을 가리킬 수 있습니다.
더 많은 정보: <https://manned.org/mkswap>.

- 지정된 스왑 영역 설정:

`sudo mkswap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 스왑 영역을 생성하기 전에 파티션의 불량 블록 확인:

`sudo mkswap -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파티션에 레이블 지정 (레이블을 사용하여 `swapon` 사용 가능):

`sudo mkswap -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
