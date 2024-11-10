---
layout: page
title: common/sdiff (한국어)
description: "두 파일의 차이점을 비교하고 선택적으로 병합."
content_hash: d134510bc0fa03fea448eef00627f226ea514b6b
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sdiff

두 파일의 차이점을 비교하고 선택적으로 병합.
더 많은 정보: <https://manned.org/sdiff>.

- 두 파일 비교:

`sdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 모든 탭과 공백을 무시하고 두 파일 비교:

`sdiff -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 줄 끝의 공백을 무시하고 두 파일 비교:

`sdiff -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 대소문자를 구분하지 않고 두 파일 비교:

`sdiff -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 비교 후 병합하고, 결과를 새 파일에 작성:

`sdiff -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/병합된_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>
