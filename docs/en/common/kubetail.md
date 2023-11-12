---
layout: page
title: common/kubetail (English)
description: "Utility to tail multiple Kubernetes pod logs at the same time."
content_hash: beb019b09baf5d24c0da06691b209fd0254e8bed
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# kubetail

Utility to tail multiple Kubernetes pod logs at the same time.
More information: <https://github.com/johanhaleby/kubetail>.

- Tail the logs of multiple pods (whose name starts with "my_app") in one go:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app</span>

- Tail only a specific container from multiple pods:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_container</span>

- To tail multiple containers from multiple pods:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_container_1</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_container_2</span>

- To tail multiple applications at the same time separate them by comma:

`kubetail `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app_1</span>`,`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_app_2</span>
