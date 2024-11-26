---
layout: page
title: common/chmod (한국어)
description: "파일이나 디렉토리의 연결 권한 변경."
content_hash: bcdc3c48c26e18e0c195413d337d5a35aaed59ff
last_modified_at: 2024-11-26
related_topics:
  - title: Deutsch version
    url: /de/common/chmod.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chmod.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/chmod.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/chmod.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chmod.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/chmod.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chmod.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/chmod.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/chmod.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/chmod.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/chmod.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/chmod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/chmod.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/chmod.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># chmod

파일이나 디렉토리의 연결 권한 변경.
더 많은 정보: <https://www.gnu.org/software/coreutils/chmod>.

- 파일을 소유한 사용자[u]에게 실행[x] 권한 부여:

`chmod u+x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일/디렉토리에 읽기[r] 와 쓰기[w] 사용자 권한 부여:

`chmod u+rw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일명_또는_디렉토리명</span>

- 그룹[g]에서 실행 권한 제거:

`chmod g-x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 모든[a] 사용자에게 읽기 및 실행 권한 부여:

`chmod a+rx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다른[o] 사람(파일 소유자의 그룹이 아님)에게 그룹과 동일한 권한 부여:

`chmod o=g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 다른[o] 사람에게 모든 권한 제거:

`chmod o= `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 그룹[g] 및 다른 사람[o]에 대한 쓰기[w]에 대한 권한을 재귀적으로 변경:

`chmod -R g+w,o+w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>

- 모든 사용자[a]에게 파일에 대한 읽기[r] 권한과 디렉토리에 대한 실행[X] 권한 재귀적으로 부여:

`chmod -R a+rX `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>
