---
layout: page
title: common/eget (한국어)
description: "GitHub에서 사전 구축된 바이너리를 쉽게 설치 가능."
content_hash: c6140f0684ea7468a406005e0d088f1674b00704
last_modified_at: 2024-10-17
related_topics:
  - title: English version
    url: /en/common/eget.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eget

GitHub에서 사전 구축된 바이너리를 쉽게 설치 가능.
더 많은 정보: <https://github.com/zyedidia/eget>.

- GitHub 저장소에서 현재 시스템에 대해 사전 빌드된 바이너리를 다운로드:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>

- URL부터 다운로드:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://go.dev/dl/go1.17.5.linux-amd64.tar.gz</span>

- 다운로드한 파일을 저장할 위치를 지정:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 최신 버전을 사용하는 대신 Git 태그를 지정:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --tag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">v2.0.10</span>

- 최신 안정 버전 대신 최신 시험판을 설치:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --pre-release`

- 추출을 건너뛰고, 리소스만 다운로드:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --download-only`

- 현재 다운로드한 버전보다 회신 버전이 있는 경우에만 다운로드:

`eget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zyedidia/micro</span>` --upgrade-only`
