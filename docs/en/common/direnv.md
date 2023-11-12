---
layout: page
title: common/direnv (English)
description: "Shell extension to load and unload environment variables depending on the current directory."
content_hash: c6b0657e7261a2ec4cfa7f7c4f17ceb1b09cd78d
last_modified_at: 2023-11-12
related_topics:
  - title: italiano version
    url: /it/common/direnv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# direnv

Shell extension to load and unload environment variables depending on the current directory.
More information: <https://github.com/direnv/direnv>.

- Grant direnv permission to load the `.envrc` present in the current directory:

`direnv allow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Revoke the authorization to load the `.envrc` present in the current directory:

`direnv deny `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Edit the `.envrc` file in the default text editor and reload the environment on exit:

`direnv edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Trigger a reload of the environment:

`direnv reload`

- Print some debug status information:

`direnv status`
