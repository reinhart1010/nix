---
layout: page
title: common/tts (English)
description: "Synthesize speech."
content_hash: a59955963054c7b111bb7ff9a80da78d7918d6cf
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# tts

Synthesize speech.
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
