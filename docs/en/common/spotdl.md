---
layout: page
title: common/spotdl (English)
description: "Download Spotify playlists and songs along with metadata."
content_hash: 9d56aed3c4678ba2a13e02c07c579975867af3e6
last_modified_at: 2023-05-05
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># spotdl

Download Spotify playlists and songs along with metadata.
More information: <https://github.com/spotDL/spotify-downloader>.

- Download songs from the provided URLs and embed metadata:

`spotdl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open.spotify.com/playlist/playlistId open.spotify.com/track/trackId ...</span>

- Start a web interface to download individual songs:

`spotdl web`

- Save only the metadata without downloading anything:

`spotdl save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">open.spotify.com/playlist/playlistId ...</span>` --save-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/save_file.spotdl</span>
