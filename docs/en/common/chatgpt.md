---
layout: page
title: common/chatgpt (English)
description: "Shell script to use OpenAI's ChatGPT and DALL-E from the terminal."
content_hash: f65563a6d3b67ccb7dc61aa8cac38079b2753159
last_modified_at: 2024-09-17
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/chatgpt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chatgpt

Shell script to use OpenAI's ChatGPT and DALL-E from the terminal.
More information: <https://github.com/0xacx/chatGPT-shell-cli>.

- Start in chat mode:

`chatgpt`

- Give a [p]rompt to answer to:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">What is the regex to match an email address?</span>`"`

- Start in chat mode using a specific [m]odel (default is `gpt-3.5-turbo`):

`chatgpt --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gpt-4</span>

- Start in chat mode with an [i]nitial prompt:

`chatgpt --init-prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">You are Rick, from Rick and Morty. Respond to questions using his mannerism and include insulting jokes.</span>`"`

- Pipe the result of a command to `chatgpt` as a prompt:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">How to view running processes on Ubuntu?</span>`" | chatgpt`

- Generate an image using DALL-E:

`chatgpt --prompt "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image: A white cat</span>`"`
