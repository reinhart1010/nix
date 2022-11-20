---
layout: page
title: common/qmmp (English)
description: "An audio player."
content_hash: d74ce0e91330a6076a1b6d308fba3b577ee1d5d6
last_modified_at: 2022-11-20
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># qmmp

An audio player.
More information: <http://qmmp.ylsoftware.com>.

- Launch qmmp:

`qmmp`

- Start or stop the currently playing audio:

`qmmp --play-pause`

- Seek forwards or backward a specific amount of time in seconds:

`qmmp --seek-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|bwd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">time_in_seconds</span>

- Play the next audio file:

`qmmp --next`

- Play the previous audio file:

`qmmp --previous`

- Print the current volume:

`qmmp --volume-status`

- Increase or decrease the volume of the currently playing audio by 5 steps:

`qmmp --volume-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc|dec</span>
