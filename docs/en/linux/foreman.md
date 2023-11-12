---
layout: page
title: linux/foreman (English)
description: "Manage Procfile-based applications."
content_hash: 95e447e2804561fad9d208ad748623ef406a1301
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# foreman

Manage Procfile-based applications.
More information: <https://manned.org/foreman>.

- Start an application with the Procfile in the current directory:

`foreman start`

- Start an application with a specified Procfile:

`foreman start -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Procfile</span>

- Start a specific application:

`foreman start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">process</span>

- Validate Procfile format:

`foreman check`

- Run one-off commands with the process's environment:

`foreman run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>

- Start all processes except the one named "worker":

`foreman start -m all=1,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker</span>`=0`
