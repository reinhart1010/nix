---
layout: page
title: common/webtorrent (한국어)
description: "WebTorrent의 명령줄 인터페이스."
content_hash: c9e7739fd87b52c953a1f1efbb67a2bafe66eb45
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/webtorrent.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/webtorrent.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># webtorrent

WebTorrent의 명령줄 인터페이스.
마그넷, URL, 정보 해시 및 `.torrent` 파일을 지원.
더 많은 정보: <https://github.com/webtorrent/webtorrent-cli>.

- 토렌트 다운로드:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_id</span>`"`

- VLC 미디어 플레이어로 토렌트 스트리밍:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_id</span>`" --vlc`

- DLNA (Digital Living Network Alliance) 장치로 토렌트 스트리밍:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_id</span>`" --dlna`

- 특정 토렌트의 파일 목록 표시:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_id</span>`" --select`

- 다운로드할 토렌트에서 파일 색인 지정:

`webtorrent download "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_id</span>`" --select `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">색인</span>

- 특정 파일 또는 폴더 시드:

`webtorrent seed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- 지정된 파일 경로에 대한 새 토렌트 파일 생성:

`webtorrent create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 마그넷 URI 또는 `.torrent` 파일에 대한 정보 표시:

`webtorrent info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_마그넷</span>
