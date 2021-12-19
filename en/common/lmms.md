---
layout: page
title: common/lmms (English)
description: "Free, open source, cross-platform digital audio workstation."
content_hash: 6bdb953b85c60b636cdbf1a8a3169bc088254b62
---
# lmms

Free, open source, cross-platform digital audio workstation.
Render a `.mmp` or `.mmpz` project file, dump a `.mmpz` as XML, or start the GUI.
More information: <https://lmms.io>.

- Start the GUI:

`lmms`

- Start the GUI and load external config:

`lmms --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.xml</span>

- Start the GUI and import MIDI or Hydrogen file:

`lmms --import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/midi/or/hydrogen/file</span>

- Start the GUI with a specified window size:

`lmms --geometry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_size</span>`x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_size</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">x_offset</span>`+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">y_offset</span>

- Dump a `.mmpz` file:

`lmms dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mmpz/file.mmpz</span>

- Render a project file:

`lmms render `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mmpz_or_mmp/file</span>

- Render the individual tracks of a project file:

`lmms rendertracks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/mmpz_or_mmp/file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/dump/directory</span>

- Render with custom samplerate, format, and as a loop:

`lmms render --samplerate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">88200</span>` --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ogg</span>` --loop --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output/file.ogg</span>
