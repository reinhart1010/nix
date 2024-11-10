---
layout: page
title: linux/namei (한국어)
description: "경로명을 따라가면서 최종 지점(파일/디렉토리/문자 디바이스 등)을 찾습니다. 이 프로그램은 \"심볼릭 링크 수준이 너무 많음\" 문제를 찾는 데 유용합니다."
content_hash: dbed44333e03b38aa580f01a0c02093579308149
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/namei.html
    icon: bi bi-globe
tldri18n_status: 2
---
# namei

경로명을 따라가면서 최종 지점(파일/디렉토리/문자 디바이스 등)을 찾습니다. 이 프로그램은 "심볼릭 링크 수준이 너무 많음" 문제를 찾는 데 유용합니다.
더 많은 정보: <https://manned.org/namei>.

- 인수로 지정된 경로명을 분석:

`namei `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c</span>

- 결과를 긴 목록 형식으로 표시:

`namei --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c</span>

- 각 파일 유형의 모드 비트를 `ls` 스타일로 표시:

`namei --modes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c</span>

- 각 파일의 소유자와 그룹 이름을 표시:

`namei --owners `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c</span>

- 심볼릭 링크를 따라가지 않고 분석:

`namei --nosymlinks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/b</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/c</span>
