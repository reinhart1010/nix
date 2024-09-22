---
layout: page
title: common/basenc (한국어)
description: "지정된 인코딩을 사용하여 파일 또는 `stdin`을 `stdout`으로 인코딩하거나 디코딩함."
content_hash: 2b0bf4a2698a2619730e0a54d0d1f8d1ebd93131
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/basenc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/basenc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# basenc

지정된 인코딩을 사용하여 파일 또는 `stdin`을 `stdout`으로 인코딩하거나 디코딩함.
더 많은 정보: <https://www.gnu.org/software/coreutils/basenc>.

- base64 인코딩으로 파일을 인코딩:

`basenc --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- base64 인코딩으로 파일을 디코딩:

`basenc --decode --base64 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 42개의 열이 있는 base32 인코딩을 사용하여 `stdin`에서 인코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | basenc --base32 -w42`

- base32 인코딩을 사용하여 `stdin`에서 인코딩:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` | basenc --base32`
