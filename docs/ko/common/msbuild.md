---
layout: page
title: common/msbuild (한국어)
description: "Visual Studio 프로젝트 솔루션을 위한 Microsoft 빌드 도구."
content_hash: b4a6ca9f117276966283c535835249ba8e2aa0f1
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/msbuild.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msbuild

Visual Studio 프로젝트 솔루션을 위한 Microsoft 빌드 도구.
더 많은 정보: <https://learn.microsoft.com/visualstudio/msbuild>.

- 현재 디렉토리의 첫 번째 프로젝트 파일 빌드:

`msbuild`

- 특정 프로젝트 파일 빌드:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>

- 빌드할 하나 이상의 세미콜론으로 구분된 타겟 지정:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>` /target:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타겟들</span>

- 하나 이상의 세미콜론으로 구분된 속성 지정:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>` /property:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름=값</span>

- 사용할 빌드 도구 버전 지정:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>` /toolsversion:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 프로젝트가 어떻게 구성되었는지에 대한 자세한 정보를 로그 끝에 표시:

`msbuild `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_파일</span>` /detailedsummary`

- 도움말 표시:

`msbuild /help`
