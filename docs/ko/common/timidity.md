---
layout: page
title: common/timidity (한국어)
description: "MIDI 파일을 재생하고 변환합니다."
content_hash: ac1290c4aa7ba791c4f0a6e911f4c540c4f0fd38
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/timidity.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/timidity.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># timidity

MIDI 파일을 재생하고 변환합니다.
더 많은 정보: <https://timidity.sourceforge.net>.

- MIDI 파일 재생:

`timidity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mid</span>

- MIDI 파일을 반복 재생:

`timidity --loop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mid</span>

- 특정 조로 MIDI 파일 재생 (0 = 다장조/가단조, -1 = 바장조/라단조, +1 = 사장조/마단조 등):

`timidity --force-keysig=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-플랫|+샤프</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mid</span>

- MIDI 파일을 PCM (WAV) 오디오로 변환:

`timidity --output-mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">w</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mid</span>

- MIDI 파일을 FLAC 오디오로 변환:

`timidity --output-mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">F</span>` --output-file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.flac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mid</span>
