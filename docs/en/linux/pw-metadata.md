---
layout: page
title: linux/pw-metadata (English)
description: "Monitor, set, and delete metadata on PipeWire objects."
content_hash: 8fece3bef704896be932731b0400db0b9846b083
last_modified_at: 2024-06-05
tldri18n_status: 2
---
# pw-metadata

Monitor, set, and delete metadata on PipeWire objects.
See also: `pipewire`, `pw-mon`, `pw-cli`.
More information: <https://docs.pipewire.org/page_man_pw-metadata_1.html>.

- Show metadata in `default` name:

`pw-metadata`

- Show metadata with ID 0 in `settings`:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-n|--name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">settings</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>

- List all available metadata objects:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--list</span>

- Keep running and log the changes to the metadata:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--monitor</span>

- Delete all metadata:

`pw-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--delete</span>

- Set `log.level` to 1 in `settings`:

`pw-metadata --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">settings</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log.level</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>

- Display help:

`pw-metadata --help`
