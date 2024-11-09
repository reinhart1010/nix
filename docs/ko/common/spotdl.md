---
layout: page
title: common/spotdl (한국어)
description: "Spotify 재생목록 및 노래를 메타데이터와 함께 다운로드."
content_hash: ed79bd019ede657dec667ff385d58fd164e6d2f4
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/spotdl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/spotdl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># spotdl

Spotify 재생목록 및 노래를 메타데이터와 함께 다운로드.
더 많은 정보: <https://github.com/spotDL/spotify-downloader>.

- 제공된 URL에서 노래를 다운로드하고 메타데이터를 포함:

`spotdl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open.spotify.com/playlist/playlistId open.spotify.com/track/trackId ...</span>

- 개별 노래를 다운로드할 수 있는 웹 인터페이스 시작:

`spotdl web`

- 아무것도 다운로드하지 않고 메타데이터만 저장:

`spotdl save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open.spotify.com/playlist/playlistId ...</span>` --save-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장_파일.spotdl</span>
