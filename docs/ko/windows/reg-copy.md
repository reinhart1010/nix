---
layout: page
title: windows/reg-copy (한국어)
description: "레지스트리에서 키와 그 값을 복사."
content_hash: 928b8ff9a5f1b458784496d03360dacd322a356a
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/windows/reg-copy.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/reg-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# reg copy

레지스트리에서 키와 그 값을 복사.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- 레지스트리 키를 새로운 레지스트리 위치로 복사:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>

- 레지스트리 키를 재귀적으로 (모든 [s]ubkeys 포함) 새로운 레지스트리 위치로 복사:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>` /s`

- [f]orcefully (프롬프트 없이) 레지스트리 키 복사:

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">old_key_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_key_name</span>` /f`
