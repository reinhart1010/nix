---
layout: page
title: common/ffprobe (한국어)
description: "멀티미디어 스트림 분석기."
content_hash: e6f07721573a5f831919adf176ac972837d57591
last_modified_at: 2024-10-20
related_topics:
  - title: Deutsch version
    url: /de/common/ffprobe.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ffprobe.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ffprobe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ffprobe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ffprobe

멀티미디어 스트림 분석기.
더 많은 정보: <https://ffmpeg.org/ffprobe.html>.

- 미디어 파일에 대해 사용 가능한 모든 스트림 정보를 표시:

`ffprobe -v error -show_streams `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>

- 미디어 지속시간 표시:

`ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>

- 비디오의 프레임 속도 표시:

`ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>

- 비디오의 너비 또는 높이를 표시:

`ffprobe -v error -select_streams v:0 -show_entries stream=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">width|height</span>` -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>

- 비디오의 평균 비트 전송률 표시:

`ffprobe -v error -select_streams v:0 -show_entries stream=bit_rate -of default=noprint_wrappers=1:nokey=1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력.mp4</span>
