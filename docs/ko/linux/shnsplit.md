---
layout: page
title: linux/shnsplit (한국어)
description: "`.cue` 파일에 따라 오디오 파일을 분할합니다."
content_hash: 17cde30a6660dca1b78b2feeef4eaa7b64309a25
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/shnsplit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/shnsplit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/shnsplit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shnsplit

`.cue` 파일에 따라 오디오 파일을 분할합니다.
더 많은 정보: <http://shnutils.freeshell.org/shntool/>.

- `.wav` + `.cue` 파일을 여러 파일로 분할:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 지원되는 형식 표시:

`shnsplit -a`

- `.flac` 파일을 여러 파일로 분할:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cue</span>` -o flac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.flac</span>

- `.wav` 파일을 "트랙 번호 - 앨범 - 제목" 형식으로 분할:

`shnsplit -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.cue</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>` -t "%n - %a - %t"`
