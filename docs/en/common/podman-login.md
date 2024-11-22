---
layout: page
title: common/podman-login (English)
description: "Log in to a container registry."
content_hash: 7d1cf17925a030f01310672184f2af30f8b06475
last_modified_at: 2024-11-22
tldri18n_status: 2
---
# podman login

Log in to a container registry.
Note: the default authfile path on Linux is `$XDG_RUNTIME_DIR/containers/auth.json`, which is usually stored in a `tmpfs` (in RAM).
More information: <https://docs.podman.io/en/latest/markdown/podman-login.1.html>.

- Log in to a registry (non-persistent on Linux; persistent on Windows/macOS):

`podman login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.example.org</span>

- Log in to a registry persistently on Linux:

`podman login --authfile $HOME/.config/containers/auth.json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.example.org</span>

- Log in to an insecure (HTTP) registry:

`podman login --tls-verify false `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.example.org</span>
