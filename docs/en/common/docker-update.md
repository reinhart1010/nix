---
layout: page
title: common/docker-update (English)
description: "Update configuration of Docker containers."
content_hash: d30f71aaebbdb32a63e80ae5e8cd07fa1d3589d5
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/docker-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker update

Update configuration of Docker containers.
This command is not supported for Windows containers.
More information: <https://docs.docker.com/engine/reference/commandline/update/>.

- Update restart policy to apply when a specific container exits:

`docker update --restart=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">always|no|on-failure|unless-stopped</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Update the policy to restart up to three times a specific container when it exits with non-zero exit status:

`docker update --restart=on-failure:3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Update the number of CPUs available to a specific container:

`docker update --cpus `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Update the memory limit in [M]egabytes for a specific container:

`docker update --memory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">limit</span>`M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Update the maximum number of process IDs allowed inside a specific container (use `-1` for unlimited):

`docker update --pids-limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">count</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Update the amount of memory in [M]egabytes a specific container can swap to disk (use `-1` for unlimited):

`docker update --memory-swap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">limit</span>`M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
