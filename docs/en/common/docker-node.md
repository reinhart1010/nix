---
layout: page
title: common/docker-node (English)
description: "Manage Docker Swarm nodes."
content_hash: 4ffa14939c1d0bb2e37a9c57a00f0f6b81c4eab6
last_modified_at: 2024-11-14
tldri18n_status: 2
---
# docker node

Manage Docker Swarm nodes.
More information: <https://docs.docker.com/reference/cli/docker/node/>.

- List nodes in the swarm:

`docker node ls`

- List tasks running on one or more nodes, defaults to the current node:

`docker node ps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node1 node2 node3 ...</span>

- Display detailed information on one or more nodes:

`docker node inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node1 node2 node3 ...</span>

- Promote one or more nodes to manager in the swarm:

`docker node promote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node1 node2 node3 ...</span>

- Demote one or more nodes from manager in the swarm:

`docker node demote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node1 node2 node3 ...</span>

- Remove one or more nodes from the swarm:

`docker node rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node1 node2 node3 ...</span>

- Update metadata about a node, such as its availability, labels, or roles:

`docker node update --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">availability|role|label-add|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">active|worker|foo|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">node1</span>
