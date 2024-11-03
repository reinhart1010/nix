---
layout: page
title: common/hexyl (한국어)
description: "터미널용 간단한 16진수 뷰어. 다양한 카테고리의 바이트를 구별하기 위해 컬러 출력을 사용."
content_hash: af378c8f41b57fc42a450b976679b0497494a6ac
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/hexyl.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/hexyl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/hexyl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexyl

터미널용 간단한 16진수 뷰어. 다양한 카테고리의 바이트를 구별하기 위해 컬러 출력을 사용.
더 많은 정보: <https://github.com/sharkdp/hexyl>.

- 파일의 16진수 표현을 출력:

`hexyl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 처음 n 바이트의 16진수 표현을 출력:

`hexyl -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 바이트 512부터 1024를 출력:

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 1024번째 바이트부터 512 바이트를 출력:

`hexyl -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>`:+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
