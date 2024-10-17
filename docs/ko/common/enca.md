---
layout: page
title: common/enca (한국어)
description: "텍스트 파일의 인코딩을 감지하고 변환."
content_hash: 7649786a632a9ac0077c0b9c4058460889b6ab45
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/enca.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/enca.html
    icon: bi bi-globe
tldri18n_status: 2
---
# enca

텍스트 파일의 인코딩을 감지하고 변환.
더 많은 정보: <https://github.com/nijel/enca>.

- 시스템의 위치에 따라 파일 인코딩을 감지:

`enca `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- POSIX/C 위치 형식 (예: zh_CN, en_US)에서 언어를 지정하는 파일 인코딩을 감지:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 파일을 특정 인코딩으로 변환:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 다른 인코딩을 사용하여 기존 파일의 복사본을 만듬:

`enca -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>` -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인코딩</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_파일</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_파일</span>
