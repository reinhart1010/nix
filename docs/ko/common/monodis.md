---
layout: page
title: common/monodis (한국어)
description: "Mono 공용 중간 언어(CIL) 디스어셈블러."
content_hash: 5a708d4c45009b892387dfb5a9dd4600572a9747
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/monodis.html
    icon: bi bi-globe
tldri18n_status: 2
---
# monodis

Mono 공용 중간 언어(CIL) 디스어셈블러.
더 많은 정보: <https://www.mono-project.com/docs/tools+libraries/tools/monodis/>.

- 어셈블리를 텍스트 CIL로 디스어셈블:

`monodis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.exe</span>

- 출력 결과를 파일로 저장:

`monodis --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.il</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.exe</span>

- 어셈블리에 대한 정보 표시:

`monodis --assembly `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>

- 어셈블리의 참조 목록:

`monodis --assemblyref `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.exe</span>

- 어셈블리의 모든 메서드 나열:

`monodis --method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.exe</span>

- 어셈블리에 내장된 리소스 나열:

`monodis --manifest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>

- 모든 내장 리소스를 현재 디렉터리로 추출:

`monodis --mresources `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/어셈블리.dll</span>
