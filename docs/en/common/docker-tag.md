---
layout: page
title: common/docker-tag (English)
description: "Assign tags to existing Docker images."
content_hash: 44d8755b336ff17f021a0759db0a0746f8ef4fb3
last_modified_at: 2024-09-28
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/docker-tag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker tag

Assign tags to existing Docker images.
More information: <https://docs.docker.com/reference/cli/docker/image/tag/>.

- Assign a name and tag to a specific image ID:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Assign a tag to a specific image:

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">current_tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_tag</span>

- Display help:

`docker tag`
