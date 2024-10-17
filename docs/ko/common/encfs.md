---
layout: page
title: common/encfs (한국어)
description: "암호화된 가상 파일 시스템을 마운트하거나 생성."
content_hash: 773bcb2c2ab73ebd711267dbfdfe34fe06fa08ab
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/encfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# encfs

암호화된 가상 파일 시스템을 마운트하거나 생성.
마운트된 파일 시스템을 마운트 해제할 수 있는 `fusermount`도 참조.
더 많은 정보: <https://github.com/vgough/encfs>.

- 암호화된 파일 시스템 초기화 또는 마운트:

`encfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/암호화_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트_지점</span>

- 표준 설정으로 암호화된 파일 시스템을 초기화:

`encfs --standard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/암호화_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트_지점</span>

- 데몬을 생성하는 대신 포어그라운드에서 encfs를 실행:

`encfs -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/암호화_폴더</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/마운트_지점</span>

- 일반 디렉터리의 암호화된 스냅샷을 마운트:

`encfs --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/일반_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화_폴더</span>
