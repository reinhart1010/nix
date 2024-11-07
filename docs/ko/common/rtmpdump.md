---
layout: page
title: common/rtmpdump (한국어)
description: "RTMP 프로토콜을 통해 스트리밍되는 미디어 콘텐츠 덤프."
content_hash: d1c453229cc70f554485c6c2bc1919a470017de3
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/rtmpdump.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/rtmpdump.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rtmpdump

RTMP 프로토콜을 통해 스트리밍되는 미디어 콘텐츠 덤프.
더 많은 정보: <https://rtmpdump.mplayerhq.hu/>.

- 파일 다운로드:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.ext</span>

- Flash 플레이어에서 파일 다운로드:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` --swfVfy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/player</span>` --flashVer "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">LNX 10,0,32,18</span>`" -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.ext</span>

- 연결 매개변수가 올바르게 감지되지 않는 경우 지정:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` --app `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">앱_이름</span>` --playpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비디오</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.ext</span>

- 참조자를 요구하는 서버에서 파일 다운로드:

`rtmpdump --rtmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rtmp://example.com/path/to/video</span>` --pageUrl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/webpage</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일.ext</span>
