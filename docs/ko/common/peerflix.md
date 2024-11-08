---
layout: page
title: common/peerflix (한국어)
description: "비디오 또는 오디오 기반 토렌트를 미디어 플레이어로 스트리밍."
content_hash: 2e8d942e6086a459adefc638d2bf04a4a9e3536e
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/peerflix.html
    icon: bi bi-globe
tldri18n_status: 2
---
# peerflix

비디오 또는 오디오 기반 토렌트를 미디어 플레이어로 스트리밍.
더 많은 정보: <https://github.com/mafintosh/peerflix>.

- 토렌트에서 가장 큰 미디어 파일 스트리밍:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_URL|마그넷_링크</span>`"`

- 마그넷 링크로 주어진 토렌트에 포함된 모든 스트리밍 가능한 파일 나열:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567</span>`" --list`

- 토렌트 URL로 주어진 토렌트에서 가장 큰 파일을 VLC로 스트리밍:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.net/music.torrent</span>`" --vlc`

- 자막과 함께 토렌트에서 가장 큰 파일을 MPlayer로 스트리밍:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_URL|마그넷_링크</span>`" --mplayer --subtitles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">자막_파일.srt</span>

- 토렌트의 모든 파일을 Airplay로 스트리밍:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토렌트_URL|마그넷_링크</span>`" --all --airplay`
