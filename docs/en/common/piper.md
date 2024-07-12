---
layout: page
title: common/piper (English)
description: "A fast, local neural text to speech system."
content_hash: b6d6307e5a88da9ea2bf85831c5132db2c3b6841
last_modified_at: 2024-07-12
tldri18n_status: 2
---
# piper

A fast, local neural text to speech system.
Try out and download speech models from <https://rhasspy.github.io/piper-samples>.
More information: <https://github.com/rhasspy/piper>.

- Output a WAV [f]ile using a text-to-speech [m]odel (assuming a config file at model_path + .json):

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Thing to say</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/model.onnx</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">outputfile.wav</span>

- Output a WAV [f]ile using a [m]odel and specifying its JSON [c]onfig file:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Thing to say'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/model.onnx</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/model.onnx.json</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">outputfile.wav</span>

- Select a particular speaker in a voice with multiple speakers by specifying the speaker's ID number:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Warum?'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de_DE-thorsten_emotional-medium.onnx</span>` --speaker `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">angry.wav</span>

- Stream the output to the mpv media player:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Hello world'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_GB-northern_english_male-medium.onnx</span>` --output-raw -f - | mpv -`

- Speak twice as fast, with huge gaps between sentences:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Speaking twice the speed. With added drama!'</span>` | piper -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo.onnx</span>` --length_scale `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.5</span>` --sentence_silence `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">drama.wav</span>
