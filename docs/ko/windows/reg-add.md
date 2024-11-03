---
layout: page
title: windows/reg-add (한국어)
description: "레지스트리에 새 키와 값을 추가."
content_hash: c7fb5b21d9b664ebac2bc99a9344fc0e7705e3d1
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/reg-add.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-add.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg add

레지스트리에 새 키와 값을 추가.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- 새 레지스트리 키 추가:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>

- 특정 키 아래에 새 [v]alue 추가:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 특정 [d]ata로 새 값 추가:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터</span>

- 특정 데이터 [t]ype으로 키에 새 값 추가:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /t REG_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SZ|MULTI_SZ|DWORD_BIG_ENDIAN|DWORD|BINARY|DWORD_LITTLE_ENDIAN|LINK|FULL_RESOURCE_DESCRIPTOR|EXPAND_SZ</span>

- [f]orcefully (프롬프트 없이) 기존 레지스트리 값 덮어쓰기:

`reg add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` /f`
