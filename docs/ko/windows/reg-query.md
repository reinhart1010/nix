---
layout: page
title: windows/reg-query (한국어)
description: "레지스트리의 키와 하위 키의 값을 표시."
content_hash: b4591ceec1963cedcfa1a6cd9b0ca15c561cc5df
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/reg-query.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg query

레지스트리의 키와 하위 키의 값을 표시.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- 키의 모든 값 표시:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>

- 키의 특정 [값] 표시:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 키와 하위 키의 모든 값 표시:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /s`

- 특정 패턴과 일치하는 키와 값을 [검색]:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`"`

- 지정된 데이터 [형식]과 일치하는 키의 값 표시:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /t REG_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SZ|MULTI_SZ|EXPAND_SZ|DWORD|BINARY|NONE</span>

- 데이터에서만 검색:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /d`

- 키 이름에서만 검색:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_패턴</span>`" /k`

- [대소문자] 구분하여 [정확히] 일치하는 값 검색:

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /c /e`
