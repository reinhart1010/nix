---
layout: page
title: linux/mocp (English)
description: "Music on Console (MOC) audio player."
content_hash: c8f9325c28632448cdd8954ed258fcf350949ef5
---
# mocp

Music on Console (MOC) audio player.
More information: <https://manned.org/mocp>.

- Launch the MOC terminal UI:

`mocp`

- Launch the MOC terminal UI in a specific directory:

`mocp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start the MOC server in the background, without launching the MOC terminal UI:

`mocp --server`

- Add a specific song to the play queue while MOC is in the background:

`mocp --enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio_file</span>

- Add songs recursively to the play queue while MOC is in the background:

`mocp --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Clear the play queue while MOC is in the background:

`mocp --clear`

- Play or stop the currently queued song while MOC is in the background:

`mocp --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">play|stop</span>

- Stop the MOC server while it's in the background:

`mocp --exit`
