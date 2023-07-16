---
layout: page
title: common/whisper (English)
description: "Convert audio files to `txt`, `vtt`, `srt`, `tsv` and `json`."
content_hash: a1fde2f0b95449e0625768a9bbf9daca6c7da031
last_modified_at: 2023-07-16
---
# whisper

Convert audio files to `txt`, `vtt`, `srt`, `tsv` and `json`.
More information: <https://github.com/openai/whisper>.

- Convert a specific audio file to all of the given file formats:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio.mp3</span>

- Convert an audio file specifying the output format of the converted file:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio.mp3</span>` --output_format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- Convert an audio file using a specific model for conversion:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio.mp3</span>` --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large</span>

- Convert an audio file specifying which language the audio file is in to reduce conversion time:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio.mp3</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">english</span>

- Convert an audio file and save it to a specific location:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio.mp3</span>` --output_dir "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output</span>`"`

- Convert an audio file in quiet mode:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/audio.mp3</span>` --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">False</span>
