---
layout: page
title: osx/valet (English)
description: "A Laravel development environment that allows hosting sites via local tunnels on `http://<example>.test`."
content_hash: fa1353e3091bc8d1f691537c8ca7ea0ec9c64aee
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/osx/valet.html
    icon: bi bi-globe
tldri18n_status: 2
---
# valet

A Laravel development environment that allows hosting sites via local tunnels on `http://<example>.test`.
More information: <https://laravel.com/docs/valet>.

- Start the valet daemon:

`valet start`

- Register the current working directory as a path that Valet should search for sites:

`valet park`

- View 'parked' paths:

`valet paths`

- Serve a single site instead of an entire directory:

`valet link `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">application_name</span>

- Share a project via an Ngrok tunnel:

`valet share`
