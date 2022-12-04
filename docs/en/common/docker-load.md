---
layout: page
title: common/docker-load (English)
description: "Load Docker images from files or `stdin`."
content_hash: 97144afb960cfb33cafe160103e664add2958fc4
last_modified_at: 2022-12-04
---
# docker load

Load Docker images from files or `stdin`.
More information: <https://docs.docker.com/engine/reference/commandline/load/>.

- Load a Docker image from `stdin`:

`docker load < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.tar</span>

- Load a Docker image from a specific file:

`docker load --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.tar</span>

- Load a Docker image from a specific file in quiet mode:

`docker load --quiet --input `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file.tar</span>
