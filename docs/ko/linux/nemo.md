---
layout: page
title: linux/nemo (한국어)
description: "Cinnamon 데스크탑 환경에서 파일과 디렉토리를 관리합니다."
content_hash: bc419f4bdeb5f37ab48ccdb78cd4c42e2e806a4a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/nemo.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/nemo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/nemo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nemo

Cinnamon 데스크탑 환경에서 파일과 디렉토리를 관리합니다.
더 많은 정보: <https://manned.org/nemo>.

- 현재 사용자 홈 디렉토리 열기:

`nemo`

- 특정 디렉토리를 각각의 창으로 열기:

`nemo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 특정 디렉토리를 탭으로 열기:

`nemo --tabs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더1 경로/대상/폴더2 ...</span>

- 특정 창 크기로 디렉토리 열기:

`nemo --geometry=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">600</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">400</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 모든 창 닫기:

`nemo --quit`
