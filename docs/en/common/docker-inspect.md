---
layout: page
title: common/docker-inspect (English)
description: "Return low-level information on Docker objects."
content_hash: d61e4bf73d13816b215082b887d471e02248f06a
last_modified_at: 2024-09-24
related_topics:
  - title: Deutsch version
    url: /de/common/docker-inspect.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/docker-inspect.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/docker-inspect.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/docker-inspect.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-inspect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# docker inspect

Return low-level information on Docker objects.
More information: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Display help:

`docker inspect`

- Display information about a container, image, or volume using a name or ID:

`docker inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container|image|ID</span>

- Display a container's IP address:

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Display the path to the container's log file:

`docker inspect --format='\{\{.LogPath\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Display the image name of the container:

`docker inspect --format='\{\{.Config.Image\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Display the configuration information as JSON:

`docker inspect --format='\{\{json .Config\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>

- Display all port bindings:

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container</span>
