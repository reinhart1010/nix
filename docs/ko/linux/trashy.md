---
layout: page
title: linux/trashy (한국어)
description: "Rust로 작성된 `rm` 및 `trash-cli`의 대안."
content_hash: 521598358bfec65116d9ad020491fd017e94c173
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/trashy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# trashy

Rust로 작성된 `rm` 및 `trash-cli`의 대안.
더 많은 정보: <https://github.com/oberblastmeister/trashy>.

- 특정 파일을 휴지통으로 이동:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 특정 파일들을 휴지통으로 이동:

`trash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 휴지통의 항목 나열:

`trash list`

- 휴지통에서 특정 파일 복원:

`trash restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 휴지통에서 특정 파일 제거:

`trash empty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일</span>

- 휴지통에서 모든 파일 복원:

`trash restore --all`

- 휴지통에서 모든 파일 제거:

`trash empty --all`
