---
layout: page
title: linux/cp (한국어)
description: "파일 및 디렉토리 복사."
content_hash: 4e153d2c4deaa9db86e3ad1ecf8da6fc98dac576
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/cp.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

파일 및 디렉토리 복사.
더 많은 정보: <https://www.gnu.org/software/coreutils/cp>.

- 파일을 다른 위치로 복사:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/원본_파일.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_파일.ext</span>

- 파일의 이름을 유지하면서 다른 디렉토리로 복사:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/원본_파일.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_디렉토리</span>

- 디렉토리의 내용을 다른 위치에 재귀적으로 복사 (만일 목적 경로가 존재한다면 디렉토리는 해당 목적 경로 안에 복사됨):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/원본_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_디렉토리</span>

- 추가 정보를 제공하는 (verbose) 모드로 디렉토리를 재귀적으로 복사:

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/원본_디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_디렉토리</span>

- 상호작용 (덮어쓰기 전 사용자에게 질문) 모드로 txt 파일을 다른 위치로 복사:

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_디렉토리</span>

- 복사를 수행하기 전에 심볼릭 링크를 따라감:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">링크</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_디렉토리</span>

- 원본 파일의 전체 경로를 사용해 존재하지 않는 중간 디렉토리를 생성하며 복사:

`cp --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/원본_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/목적_파일</span>
