---
layout: page
title: common/crane-registry (English)
description: "This command serves a registry implementation on an automatically chosen port (:0), $PORT or --address."
content_hash: 9402dc042876f589e647de1afccd3d39fa1ce767
last_modified_at: 2024-10-04
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

- Display help:

`crane registry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>

- Display help:

`crane registry serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
