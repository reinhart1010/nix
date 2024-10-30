---
layout: page
title: windows/prompt (한국어)
description: "명령 창의 기본 DOS 스타일 프롬프트를 변경합니다."
content_hash: 14c8647775796afde7d3688a1ed5a3dafc9bc6e4
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/windows/prompt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/prompt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># prompt

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
