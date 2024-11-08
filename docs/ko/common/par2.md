---
layout: page
title: common/par2 (한국어)
description: "PAR 2.0 호환 패리티 아카이브(.par2 파일)를 사용한 파일 검증 및 복구."
content_hash: 221e9453a6e5758dfb7fa4bc3a547a7c4b236b9c
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/par2.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/par2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# par2

PAR 2.0 호환 패리티 아카이브(.par2 파일)를 사용한 파일 검증 및 복구.
더 많은 정보: <https://github.com/Parchive/par2cmdline/>.

- 설정된 비율의 여유를 사용하여 패리티 아카이브 생성:

`par2 create -r`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..100</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 선택한 수의 볼륨 파일(색인 파일 추가)을 사용하여 패리티 아카이브 생성:

`par2 create -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1..32768</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 패리티 아카이브로 파일 검증:

`par2 verify -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.par2</span>

- 패리티 아카이브로 파일 복구:

`par2 repair -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.par2</span>
