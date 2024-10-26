---
layout: page
title: common/crane-registry (English)
description: "This command serves a registry implementation on an automatically chosen port (:0), $PORT or --address."
content_hash: 0f2be6ba3467ae6fbec926c27f88f0008714391c
last_modified_at: 2024-10-26
related_topics:
  - title: 한국어 version
    url: /ko/common/crane-registry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane registry

This command serves a registry implementation on an automatically chosen port (:0), $PORT or --address.
The command blocks while the server accepts pushes and pulls and contents are can be stored in memory, and disk.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

- Serve a registry implementation:

`crane registry serve`

- Address to listen on:

`crane registry serve --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">address_name</span>

- Path to a directory where blobs will be stored:

`crane registry serve --disk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/store_dir</span>

- Display help for `crane registry`:

`crane registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>

- Display help for `crane registry serve`:

`crane registry serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
