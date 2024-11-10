---
layout: page
title: common/sum (한국어)
description: "파일의 체크섬과 블록 수를 계산."
content_hash: dfeced22756441af1132a99702e537e503748e8e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/sum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sum

파일의 체크섬과 블록 수를 계산.
더 현대적인 `cksum`의 전신.
더 많은 정보: <https://www.gnu.org/software/coreutils/sum>.

- BSD 호환 알고리즘과 1024바이트 블록으로 체크섬 계산:

`sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- System V 호환 알고리즘과 512바이트 블록으로 체크섬 계산:

`sum --sysv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
