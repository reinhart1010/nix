---
layout: page
title: common/b2sum (한국어)
description: "BLACK2 암호화 체크섬을 계산."
content_hash: 126d101bbda7cbc94c1da9d224b3da85401b4f1d
last_modified_at: 2024-12-10
related_topics:
  - title: English version
    url: /en/common/b2sum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/b2sum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/b2sum.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/b2sum.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># b2sum

BLACK2 암호화 체크섬을 계산.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- 하나 이상의 파일에 대해 BLAKE2 체크섬을 계산:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- BLAKE2 체크섬 목록을 계산하고 파일에 저장:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>

- `stdin`에서 BLAKE2 체크섬을 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | b2sum`

- BLAKE2 합계 및 파일이름의 파일을 읽고 모든 파일에 일치하는 체크섬을 확인:

`b2sum --check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>

- 누락된 파일이 있거나 확인에 실패한 경우에만 메시지를 표시:

`b2sum --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>

- 누락된 파일은 무시하고, 확인에 실패한 경우에만 메시지를 표시:

`b2sum --ignore-missing --check --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.b2</span>
