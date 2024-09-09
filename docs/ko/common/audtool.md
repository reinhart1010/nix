---
layout: page
title: common/audtool (한국어)
description: "명령을 사용해 Audacious 제어."
content_hash: 809e9bcf8b36eeeb0001da8ce485bab5c4c0c7bf
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/audtool.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/audtool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/audtool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># audtool

명령을 사용해 Audacious 제어.
참고: `audacious`.
더 많은 정보: <https://manned.org/audtool>.

- 오디오 재생/일시 중지:

`audtool playback-playpause`

- 현재 재생 중인 노래의 아티스트, 앨범, 노래 제목을 출력:

`audtool current-song`

- 오디오 재생 볼륨 설정:

`audtool set-volume `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100</span>

- 다음 노래로 건너뛰기:

`audtool playlist-advance`

- 현재 노래의 비트레이트를 킬로비트 단위로 출력:

`audtool current-song-bitrate-kbps`

- 숨겨진 경우, 전체 화면으로 Audacious 열기:

`audtool mainwin-show`

- 도움말 표시:

`audtool help`

- 설정 표시:

`audtool preferences-show`
