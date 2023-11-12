---
layout: page
title: common/vgmstream_cli (English)
description: "Play a wide variety of audio formats used in video games and convert them into `wav`."
content_hash: 57068f57be1aae835d29fba368aaaf905e9d5353
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# vgmstream_cli

Play a wide variety of audio formats used in video games and convert them into `wav`.
More information: <https://vgmstream.org/doc/USAGE>.

- Decode an `adc` file to `wav`. (Default output name is `input.wav`):

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.adc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.wav</span>

- Print metadata without decoding the audio:

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.adc</span>` -m`

- Decode an audio file without loops:

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.adc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.wav</span>` -i`

- Decode with three loops, then add a 3s delay followed by a 5s fadeout:

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.adc</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.wav</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.0</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5.0</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3.0</span>

- Convert multiple files to `bgm_(original name).wav` (Default `-o` pattern is `?f.wav`):

`vgmstream_cli -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/bgm_?f.wav</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.adc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file2.adc</span>

- Play the file looping endlessly (`channels` and `rate` must match metadata):

`vgmstream_cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input.adc</span>` -pec | aplay --format cd --channels `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` --rate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">44100</span>
