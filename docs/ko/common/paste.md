---
layout: page
title: common/paste (한국어)
description: "파일의 라인을 병합."
content_hash: 38d7c7f94ab47d84136b2852bb1b1ab3a91651a7
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/paste.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/paste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paste

파일의 라인을 병합.
더 많은 정보: <https://www.gnu.org/software/coreutils/paste>.

- 모든 라인을 TAB을 구분자로 사용하여 하나의 라인으로 합치기:

`paste -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 지정한 구분자를 사용하여 모든 라인을 하나의 라인으로 합치기:

`paste -s -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 두 파일을 각각의 열로 나란히 병합하고, TAB을 구분자로 사용하기:

`paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 두 파일을 각각의 열로 나란히 병합하고, 지정한 구분자를 사용하기:

`paste -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구분자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 두 파일을 번갈아 가며 라인을 추가하여 병합하기:

`paste -d '\n' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>
