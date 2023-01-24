---
layout: page
title: common/tts (English)
description: "Synthesize speech on the command line."
content_hash: 9b926343d31a8ff1a0f238c2c76b2aed3f9d8a8d
last_modified_at: 2023-01-24
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># tts

Synthesize speech on the command line.
More information: <https://github.com/coqui-ai/TTS#command-line-tts>.

- Run text-to-speech with the default models, writing the output to "tts_output.wav":

`tts --text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`"`

- List provided models:

`tts --list_models`

- Query info for a model by idx:

`tts --model_info_by_idx `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model_type/model_query_idx</span>

- Query info for a model by name:

`tts --model_info_by_name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model_type/language/dataset/model_name</span>

- Run a text-to-speech model with its default vocoder model:

`tts --text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`" --model_name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">model_type/language/dataset/model_name</span>

- Run your own text-to-speech model (using the Griffin-Lim vocoder):

`tts --text "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">text</span>`" --model_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/model.pth</span>` --config_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/config.json</span>` --out_path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.wav</span>
