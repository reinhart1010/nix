---
layout: page
title: linux/isosize (한국어)
description: "ISO 파일의 크기를 표시합니다."
content_hash: 925a05bbfd0593e824614e93bb3e6f86d0af0b05
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/isosize.html
    icon: bi bi-globe
tldri18n_status: 2
---
# isosize

ISO 파일의 크기를 표시합니다.
더 많은 정보: <https://manned.org/isosize>.

- ISO 파일의 크기 표시:

`isosize `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>

- ISO 파일의 블록 수와 블록 크기 표시:

`isosize --sectors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>

- 주어진 수로 나눈 ISO 파일의 크기 표시 (--sectors 옵션이 없는 경우에만 사용 가능):

`isosize --divisor=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.iso</span>
