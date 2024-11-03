---
layout: page
title: windows/mklink (한국어)
description: "심볼릭 링크를 생성합니다."
content_hash: 88fe6dba0a6bad2ac0ca2f8792e6e5dd9002c1d7
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/mklink.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/mklink.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/mklink.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mklink

심볼릭 링크를 생성합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/mklink>.

- 파일에 대한 심볼릭 링크 생성:

`mklink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\링크_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일</span>

- 디렉토리에 대한 심볼릭 링크 생성:

`mklink /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\링크_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_디렉토리</span>

- 파일에 대한 하드 링크 생성:

`mklink /h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\링크_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일</span>

- 디렉토리 교차점 생성:

`mklink /j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\링크_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\소스_파일</span>
