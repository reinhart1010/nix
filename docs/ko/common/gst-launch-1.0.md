---
layout: page
title: common/gst-launch-1.0 (한국어)
description: "GStreamer 파이프라인 빌드 및 실행."
content_hash: 3e4c91a1367c4a0dbf3e8cd3771281afbc9e2bd0
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gst-launch-1.0.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gst-launch-1.0.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gst-launch-1.0

GStreamer 파이프라인 빌드 및 실행.
더 많은 정보: <https://gstreamer.freedesktop.org/documentation/tools/gst-launch.html?gi-language=c>.

- 창에서 테스트 비디오 재생:

`gst-launch-1.0 videotestsrc ! xvimagesink`

- 창에서 미디어 파일 재생:

`gst-launch-1.0 playbin uri=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로토콜</span>`://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 미디어 파일을 다시 인코딩:

`gst-launch-1.0 filesrc location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_타입</span>`demux ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코덱_타입</span>`dec ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코덱_타입</span>`enc ! `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_타입</span>`mux ! filesink location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- RTSP 서버로 파일 스트리밍:

`gst-launch-1.0 filesrc location=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` ! rtspclientsink location=rtsp://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_아이피</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
