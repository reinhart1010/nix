---
layout: page
title: osx/say (English)
description: "Converts text to speech."
content_hash: aa54133ba78877fb1f94434e283ff9b53435dfbc
related_topics:
  - title: 中文 version
    url: /zh/osx/say.html
    icon: bi bi-globe
---
# say

Converts text to speech.
More information: <https://ss64.com/osx/say.html>.

- Say a phrase aloud:

`say "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">I like to ride my bike.</span>`"`

- Read a file aloud:

`say -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.txt</span>

- Say a phrase with a custom voice and speech rate:

`say -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voice</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">words_per_minute</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">I'm sorry Dave, I can't let you do that.</span>`"`

- List the available voices:

`say -v "?"`

- Create an audio file of the spoken text:

`say -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename.aiff</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Here's to the Crazy Ones.</span>`"`
