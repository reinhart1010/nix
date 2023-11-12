---
layout: page
title: common/b2sum (한국어)
description: "BLACK2 암호화 체크섬을 계산하십시오."
content_hash: c3d6dab7855feb2b90002ff6bef0e7c1b5bf31c0
last_modified_at: 2023-11-12
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
  - title: தமிழ் version
    url: /ta/common/b2sum.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># b2sum

BLACK2 암호화 체크섬을 계산하십시오.
더 많은 정보: <https://www.gnu.org/software/coreutils/b2sum>.

- 파일의 BLACKE2 체크섬 계산:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename1</span>

- 여러 파일의 BLACKE2 체크섬 계산:

`b2sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename2</span>

- BLAKE2 합계 파일 및 파일 이름을 읽고 모든 파일에 일치하는 체크섬이 있는지 확인:

`b2sum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.b2</span>

- `stdin`에서 BLACK2 체크섬 계산:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">somecommand</span>` | b2sum`
