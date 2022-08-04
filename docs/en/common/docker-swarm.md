---
layout: page
title: common/docker-swarm (English)
description: "A container orchestration tool."
content_hash: 66b32061afc06057857d6a521aa5e237b828c17b
related_topics:
  - title: Deutsch version
    url: /de/common/docker-swarm.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/docker-swarm.html
    icon: bi bi-globe
---
# docker swarm

A container orchestration tool.
More information: <https://docs.docker.com/engine/swarm/>.

- Initialize a swarm cluster:

`docker swarm init`

- Display the token to join a manager or a worker:

`docker swarm join-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">worker|manager</span>

- Join a new node to the cluster:

`docker swarm join --token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">manager_node_url:2377</span>

- Remove a worker from the swarm (run inside the worker node):

`docker swarm leave`

- Display the current CA certificate in PEM format:

`docker swarm ca`

- Rotate the current CA certificate and display the new certificate:

`docker swarm ca --rotate`

- Change the valid period for node certificates:

`docker swarm update --cert-expiry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hours</span>`h`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minutes</span>`m`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconds</span>`s`
