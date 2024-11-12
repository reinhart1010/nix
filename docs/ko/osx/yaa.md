---
layout: page
title: osx/yaa (한국어)
description: "YAA 아카이브 생성 및 조작."
content_hash: 01cf71d4ec288c8c5e131fccfc8e8e0e0601ae12
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/yaa.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/yaa.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/yaa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/yaa.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yaa

YAA 아카이브 생성 및 조작.
더 많은 정보: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- 디렉터리에서 아카이브 생성:

`yaa archive -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.yaa</span>

- 파일에서 아카이브 생성:

`yaa archive -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.yaa</span>

- 현재 디렉터리에 아카이브 추출:

`yaa extract -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브_파일.yaa</span>

- 아카이브 내용 나열:

`yaa list -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/아카이브_파일.yaa</span>

- 특정 압축 알고리즘으로 아카이브 생성:

`yaa archive -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알고리즘</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.yaa</span>

- 8 MB 블록 크기로 아카이브 생성:

`yaa archive -b 8m -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.yaa</span>
