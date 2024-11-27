---
layout: page
title: common/chown (한국어)
description: "파일과 디렉토리의 사용자 및 그룹 소유권 변경."
content_hash: eb83ed12518148bc41c9f71b9ee412491f0503fb
last_modified_at: 2024-11-27
related_topics:
  - title: Deutsch version
    url: /de/common/chown.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chown.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chown.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chown.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chown.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/chown.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chown

파일과 디렉토리의 사용자 및 그룹 소유권 변경.
더 많은 정보: <https://www.gnu.org/software/coreutils/chown>.

- 파일/디렉토리를 소유한 사용자를 변경:

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>

- 파일/디렉토리를 소유한 사용자 및 그룹을 변경:

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>

- 소유한 사용자 및 그룹을 모두 `사용자`로 변경:

`chown `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>

- 디렉토리 및 그 내용의 소유한 사용자를 재귀적으로 변경:

`chown -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 심볼릭 링크의 소유한 사용자를 변경:

`chown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">심볼릭_링크</span>

- 파일/디렉토리의 소유한 사용자를 참조 파일과 일치시키기:

`chown --reference `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/참조_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리</span>
