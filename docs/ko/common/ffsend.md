---
layout: page
title: common/ffsend (한국어)
description: "쉽고 안전하게 파일을 공유."
content_hash: 3d4e4ccc28d303c1d47a3348544103966b153fb5
last_modified_at: 2024-10-21
related_topics:
  - title: Deutsch version
    url: /de/common/ffsend.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffsend.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ffsend.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ffsend.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ffsend

쉽고 안전하게 파일을 공유.
더 많은 정보: <https://gitlab.com/timvisee/ffsend>.

- 파일 업로드:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일 다운로드:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 비밀번호가 포함된 파일 업로드:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 비밀번호로 보호된 파일 다운로드:

`ffsend download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--password</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 파일을 업로드하고 4번의 다운로드를 허용:

`ffsend upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--downloads</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>
