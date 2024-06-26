---
layout: page
title: common/mods (English)
description: "AI for the command-line, built for pipelines."
content_hash: bd834d031b6da6719e365990b189f52a3fbe43c0
last_modified_at: 2024-06-17
tldri18n_status: 2
---
# mods

AI for the command-line, built for pipelines.
More information: <https://github.com/charmbracelet/mods>.

- Ask a generic question:

`mods "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">write me a poem about platypuses</span>`"`

- Open settings in your `$EDITOR`:

`mods --settings`

- Ask for comments on your code, in markdown format:

`mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">what are your thoughts on improving this code?</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Ask for help with your documentation, in markdown format:

`mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">write a new section to this readme for a feature that sends you a free rabbit if you hit r</span>`" < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">README.md</span>

- Organize your videos, in markdown format:

`ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/videos</span>` | mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organize these by decade and summarize</span>`"`

- Read through raw HTML and summarize the contents, in markdown format:

`curl "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://api.open-meteo.com/v1/forecast?latitude=29.00&longitude=-90.00&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m</span>`" | mods --format "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">summarize this weather data for a human</span>`"`

- Display help:

`mods --help`
