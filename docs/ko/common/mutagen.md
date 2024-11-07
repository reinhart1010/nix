---
layout: page
title: common/mutagen (한국어)
description: "실시간 파일 동기화 및 네트워크 전달 도구."
content_hash: c3d955904a102be76af0de153db05fe21ee7a62d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mutagen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mutagen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mutagen

실시간 파일 동기화 및 네트워크 전달 도구.
더 많은 정보: <https://mutagen.io>.

- 로컬 디렉토리와 원격 호스트 간의 동기화 세션 시작:

`mutagen sync create --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/로컬/폴더/</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/원격/폴더/</span>

- 로컬 디렉토리와 Docker 컨테이너 간의 동기화 세션 시작:

`mutagen sync create --name=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/로컬/폴더/</span>` docker://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">컨테이너_이름</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로/대상/원격/폴더/</span>

- 실행 중인 세션 중지:

`mutagen sync terminate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">세션_이름</span>

- 프로젝트 시작:

`mutagen project start`

- 프로젝트 중지:

`mutagen project terminate`

- 현재 프로젝트의 실행 중인 세션 나열:

`mutagen project list`
