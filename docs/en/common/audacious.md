---
layout: page
title: common/audacious (English)
description: "An open-source audio player. Indirectly based on XMMS."
content_hash: 3e95bf2f8894ca53f290782deeccb2695de0309f
last_modified_at: 2024-04-04
related_topics:
  - title: español version
    url: /es/common/audacious.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/audacious.html
    icon: bi bi-globe
tldri18n_status: 2
---
# audacious

An open-source audio player. Indirectly based on XMMS.
See also: `clementine`, `mpc`, `ncmpcpp`.
More information: <https://audacious-media-player.org>.

- Launch the GUI:

`audacious`

- Start a new instance and play an audio:

`audacious --new-instance `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio</span>

- Enqueue a specific directory of audio files:

`audacious --enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Start or stop playback:

`audacious --play-pause`

- Skip forwards ([fwd]) or backwards ([rew]) in the playlist:

`audacious --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|rew</span>

- Stop playback:

`audacious --stop`

- Start in CLI mode (headless):

`audacious --headless`

- Exit as soon as playback stops or there is nothing to playback:

`audacious --quit-after-play`
