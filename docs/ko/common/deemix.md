---
layout: page
title: common/deemix (한국어)
description: "Deezloader Remix의 나머지를 바탕으로 구축된 베어본 deezer 다운로드 라이브러리."
content_hash: 834fb405eeb87921c1dea41f2fe978ad31d89409
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/deemix.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/deemix.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># deemix

Deezloader Remix의 나머지를 바탕으로 구축된 베어본 deezer 다운로드 라이브러리.
독립형 CLI 앱 또는 API를 사용하여 UI에서 구현 가능.
더 많은 정보: <https://gitlab.com/RemixDev/deemix-py>.

- 트랙이나 재생목록 다운로드:

`deemix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.deezer.com/us/track/00000000</span>

- 특정 비트전송률로 트랙/재생 목록 다운로드:

`deemix --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FLAC|MP3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 특정 경로로 다운로드:

`deemix --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비트전송률</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>

- 현재 디렉터리에 휴대용 deemix 구성 파일을 생성:

`deemix --portable --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비트전송률</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>
