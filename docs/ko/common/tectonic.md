---
layout: page
title: common/tectonic (한국어)
description: "현대적이고 독립적인 TeX/LaTeX 엔진."
content_hash: e486a0612b234cbe371c2f22a2f22a58e6412ea7
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tectonic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tectonic

현대적이고 독립적인 TeX/LaTeX 엔진.
더 많은 정보: <https://tectonic-typesetting.github.io/book/latest>.

- 독립적인 TeX/LaTeX 파일 컴파일:

`tectonic -X compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>

- SyncTeX 데이터를 사용하여 독립적인 TeX/LaTeX 파일 컴파일:

`tectonic -X compile --synctex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.tex</span>

- 현재 디렉토리에 tectonic 프로젝트 초기화:

`tectonic -X init`

- 지정된 디렉토리에 tectonic 프로젝트 초기화:

`tectonic -X new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로젝트_이름</span>

- 현재 디렉토리의 프로젝트 빌드:

`tectonic -X build`

- 변경 시 현재 디렉토리의 프로젝트를 빌드하는 감시자 시작:

`tectonic -X watch`
