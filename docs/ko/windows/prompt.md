---
layout: page
title: windows/prompt (한국어)
description: "명령 창의 기본 DOS 스타일 프롬프트를 변경합니다."
content_hash: 14c8647775796afde7d3688a1ed5a3dafc9bc6e4
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/windows/prompt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# prompt

명령 창의 기본 DOS 스타일 프롬프트를 변경합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/prompt>.

- 기본 설정으로 프롬프트 재설정:

`prompt`

- 지정된 프롬프트로 설정:

`prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프롬프트</span>

- 현재 날짜를 먼저 표시하도록 프롬프트를 변경:

`prompt $D $P$G`

- 현재 시간을 먼저 표시하도록 프롬프트를 변경:

`prompt $T $P$G`

- 특정 텍스트를 먼저 표시하도록 프롬프트를 변경:

`prompt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">텍스트</span>` $P$G`
