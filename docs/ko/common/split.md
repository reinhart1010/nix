---
layout: page
title: common/split (한국어)
description: "파일을 여러 조각으로 분할."
content_hash: bb9c9cc19f727d81717d70d4b724402a624ff0b7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/split.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/split.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/split.html
    icon: bi bi-globe
tldri18n_status: 2
---
# split

파일을 여러 조각으로 분할.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html>.

- 파일을 10줄씩 분할 (마지막 조각 제외):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 5개의 파일로 분할. 각 조각이 동일한 크기를 갖도록 분할 (마지막 조각 제외):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 각 조각이 512바이트인 크기로 분할 (마지막 조각 제외; 킬로바이트 단위는 512k, 메가바이트 단위는 512m 사용):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 줄을 끊지 않고 각 조각이 최대 512바이트가 되도록 파일 분할:

`split -C 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
