---
layout: page
title: common/pgmkernel (한국어)
description: "`pnmconvol`과 함께 사용할 합성 커널을 생성."
content_hash: 16093d80a88fcaa4ff70f6381ea53aced4579535
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/pgmkernel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pgmkernel

`pnmconvol`과 함께 사용할 합성 커널을 생성.
같이 보기: `pnmconvol`.
더 많은 정보: <https://netpbm.sourceforge.net/doc/pgmkernel.html>.

- 합성 커널 생성:

`pgmkernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 정사각형 합성 커널 생성:

`pgmkernel `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>

- 생성된 커널의 중앙 무게 지정:

`pgmkernel -weight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">너비</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">높이</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pgm</span>
