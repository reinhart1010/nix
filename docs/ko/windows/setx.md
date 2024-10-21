---
layout: page
title: windows/setx (한국어)
description: "영구적인 환경 변수를 설정합니다."
content_hash: 5288a4243617a9237a24e4d34b0750b3e9701160
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/windows/setx.html
    icon: bi bi-globe
tldri18n_status: 2
---
# setx

영구적인 환경 변수를 설정합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/setx>.

- 현재 사용자에 대한 환경 변수 설정:

`setx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 현재 컴퓨터에 대한 환경 변수 설정:

`setx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` /M`

- 원격 컴퓨터의 사용자에 대한 환경 변수 설정:

`setx /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트명</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">암호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 레지스트리 키 값에서 환경 변수 설정:

`setx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">변수</span>` /k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레지스트리\키\경로</span>
