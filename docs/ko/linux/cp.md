---
layout: page
title: linux/cp (한국어)
description: "파일과 디렉터리를 복사합니다."
content_hash: 31511e2241c2498ea72dcc12f1d53a6b76f6f8f8
last_modified_at: 2024-11-08
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

파일과 디렉터리를 복사합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/cp>.

- 파일을 다른 위치로 복사:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_파일.ext</span>

- 파일의 이름을 유지하면서 다른 디렉토리로 복사:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_파일.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_부모_디렉터리</span>

- 디렉터리의 내용을 재귀적으로 다른 위치로 복사 (대상이 존재하면, 디렉터리 안에 복사됨):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_디렉터리</span>

- 디렉터리를 재귀적으로 복사하며, 자세히 모드로 파일이 복사되는 동안 표시:

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/원본_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_디렉터리</span>

- 여러 파일을 한 번에 디렉터리로 복사:

`cp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목적_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 ...</span>

- 특정 확장자를 가진 모든 파일을 대화형 모드로 다른 위치에 복사 (덮어쓰기 전에 사용자에게 확인 요청):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_디렉터리</span>

- 심볼릭 링크를 복사하기 전에 따라가기:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">링크</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_디렉터리</span>

- 소스 파일의 전체 경로를 사용하여, 복사할 때 누락된 중간 디렉터리를 생성:

`cp --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">소스/경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/대상_파일</span>
