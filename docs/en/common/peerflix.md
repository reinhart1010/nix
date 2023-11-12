---
layout: page
title: common/peerflix (English)
description: "Stream video- or audio-based torrents to a media player."
content_hash: a74e3adb435d5d6b62df1986d11df51796d8fed3
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# peerflix

Stream video- or audio-based torrents to a media player.
More information: <https://github.com/mafintosh/peerflix>.

- Stream the largest media file in a torrent:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_url|magnet_link</span>`"`

- List all streamable files contained in a torrent (given as a magnet link):

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">magnet:?xt=urn:btih:0123456789abcdef0123456789abcdef01234567</span>`" --list`

- Stream the largest file in a torrent, given as a torrent URL, to VLC:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.net/music.torrent</span>`" --vlc`

- Stream the largest file in a torrent to MPlayer, with subtitles:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_url|magnet_link</span>`" --mplayer --subtitles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subtitle-file.srt</span>

- Stream all files from a torrent to Airplay:

`peerflix "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">torrent_url|magnet_link</span>`" --all --airplay`
