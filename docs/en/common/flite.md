---
layout: page
title: common/flite (English)
description: "Speech synthesis engine."
content_hash: 4c07b96630989a705407e276a53b82046ea379db
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# flite

Speech synthesis engine.
More information: <http://www.festvox.org/flite/doc/>.

- List all available voices:

`flite -lv`

- Convert a text string to speech:

`flite -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>`"`

- Convert the contents of a file to speech:

`flite -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>

- Specify which voice to use:

`flite -voice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://path/to/filename.flitevox|url</span>

- Store output into a wav file:

`flite -voice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://path/to/filename.flitevox|url</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.txt</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output.wav</span>

- Display version:

`flite --version`
