---
layout: page
title: common/youtube-viewer (English)
description: "Command-line application for searching and playing videos from YouTube."
content_hash: 6830c1e57cabf6fe4fcdb469c24e9bf1d045aec6
---
# youtube-viewer

Command-line application for searching and playing videos from YouTube.
More information: <https://github.com/trizen/youtube-viewer>.

- Search for a video:

`youtube-viewer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">search_term</span>

- Log in to your YouTube account:

`youtube-viewer --login`

- Watch a video with a specific URL in VLC:

`youtube-viewer --player=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vlc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://youtube.com/watch?v=dQw4w9WgXcQ</span>

- Display a search prompt and play the selected video in 720p:

`youtube-viewer -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
