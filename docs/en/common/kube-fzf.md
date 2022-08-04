---
layout: page
title: common/kube-fzf (English)
description: "Shell commands for command-line fuzzy searching of Kubernetes Pods."
content_hash: 1c312a8295bacd821ad18136a308e64a992277c8
---
# kube-fzf

Shell commands for command-line fuzzy searching of Kubernetes Pods.
See also `kubectl` for related commands.
More information: <https://github.com/thecasualcoder/kube-fzf>.

- Get pod details (from current namespace):

`findpod`

- Get pod details (from all namespaces):

`findpod -a`

- Describe a pod:

`describepod`

- Tail pod logs:

`tailpod`

- Exec into a pod's container:

`execpod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_command</span>

- Port-forward a pod:

`pfpod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port_number</span>
