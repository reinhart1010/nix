---
layout: page
title: common/mkfile (한국어)
description: "원하는 크기의 빈 파일을 생성."
content_hash: 5efa77a0ebd29030bc8d6585d293d7eec88ca6a2
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mkfile.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mkfile.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfile

원하는 크기의 빈 파일을 생성.
더 많은 정보: <https://manned.org/mkfile>.

- 15킬로바이트의 빈 파일 생성:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">15k</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 주어진 크기와 단위(바이트, KB, MB, GB)의 파일 생성:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">크기</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">b|k|m|g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 각각 4메가바이트의 두 파일 생성:

`mkfile -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">첫번째_파일명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">두번째_파일명</span>
