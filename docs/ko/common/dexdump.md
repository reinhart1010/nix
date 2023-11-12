---
layout: page
title: common/dexdump (한국어)
description: "안드로이드 DEX 파일들에 대한 정보 출력."
content_hash: 23a7b874637636a0a0360387f6fc61c5daaf9a7c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/dexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dexdump

안드로이드 DEX 파일들에 대한 정보 출력.
더 많은 정보: <https://manned.org/dexdump>.

- APK 파일으로부터 클래스들과 메서드들 추출:

`dexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.apk</span>

- APK 파일에 포함된 DEX 파일들의 헤더 정보 출력:

`dexdump -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.apk</span>

- 실행가능한 섹션의 분해된 결과 출력:

`dexdump -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.apk</span>

- 파일로 결과 출력:

`dexdump -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/파일명.apk</span>
