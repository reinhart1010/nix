---
layout: page
title: common/takeout (English)
description: "A Docker-based development-only dependency manager."
content_hash: baed2b248d5d519308043e40119fe312bab71b27
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# takeout

A Docker-based development-only dependency manager.
More information: <https://github.com/tighten/takeout>.

- Display a list of available services:

`takeout enable`

- Enable a specific service:

`takeout enable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Enable a specific service with the default parameters:

`takeout enable --default `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Display a list of enabled services:

`takeout disable`

- Disable a specific service:

`takeout disable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Disable all services:

`takeout disable --all`

- Start a specific container:

`takeout start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_id</span>

- Stop a specific container:

`takeout stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_id</span>
