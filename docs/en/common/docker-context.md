---
layout: page
title: common/docker-context (English)
description: "Switch between contexts to manage multiple Docker environments."
content_hash: 09bb21af506707a518910daaff551039d00cf4c0
last_modified_at: 2024-12-09
tldri18n_status: 2
---
# docker context

Switch between contexts to manage multiple Docker environments.
More information: <https://docs.docker.com/reference/cli/docker/context/>.

- Create a context using a specific Docker endpoint:

`docker context create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_context</span>` --docker "host=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp://remote-host:2375</span>`"`

- Create a context based on the `DOCKER_HOST` environment variable:

`docker context create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_context</span>

- Switch to a context:

`docker context use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my_context</span>

- List all contexts:

`docker context ls`
