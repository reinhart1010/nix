---
layout: page
title: linux/mt (한국어)
description: "자기 테이프 드라이브 작동 제어 (일반적으로 LTO 테이프)."
content_hash: f848b6d1cb3a6cc6399f9f24a834b2d5f86a15fa
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mt

자기 테이프 드라이브 작동 제어 (일반적으로 LTO 테이프).
더 많은 정보: <https://manned.org/mt>.

- 테이프 드라이브 상태 확인:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` status`

- 테이프를 처음으로 되감기:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` rewind`

- 주어진 파일 수만큼 앞으로 이동한 후, 다음 파일의 첫 번째 블록에 테이프 위치:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` fsf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>

- 테이프를 되감은 후, 주어진 파일의 시작 부분에 테이프 위치:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` asf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">개수</span>

- 유효한 데이터 끝 부분에 테이프 위치:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` eod`

- 테이프를 되감고 언로드/배출:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` eject`

- 현재 위치에 EOF (파일 끝) 마크 작성:

`mt -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/nstX</span>` eof`
