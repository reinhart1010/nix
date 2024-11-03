---
layout: page
title: windows/reg-save (한국어)
description: "레지스트리 키, 하위 키 및 값을 네이티브 `.hiv` 파일로 저장합니다."
content_hash: b37032a977080fad2e87b33433f889591f01f52f
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/reg-save.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-save.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg save

레지스트리 키, 하위 키 및 값을 네이티브 `.hiv` 파일로 저장합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-save>.

- 레지스트리 키, 하위 키 및 값을 특정 파일로 저장:

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.hiv</span>

- 기존 파일을 강제로 (예라고 가정) 덮어쓰기:

`reg save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.hiv</span>` /y`
