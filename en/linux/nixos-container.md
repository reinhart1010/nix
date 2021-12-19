---
layout: page
title: linux/nixos-container (English)
description: "Starts NixOS containers using Linux containers."
content_hash: 144a2021d9b7257a6a86d070f75846e8b2c1deb1
---
# nixos-container

Starts NixOS containers using Linux containers.
More information: <https://nixos.org/manual/nixos/stable/#ch-containers>.

- List running containers:

`sudo nixos-container list`

- Create a NixOS container with a specific configuration file:

`sudo nixos-container create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` --config-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nix_config_file_path</span>

- Start, stop, terminate, or destroy a specific container:

`sudo nixos-container `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop|terminate|destroy|status</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Run a command in a running container:

`sudo nixos-container run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command_arguments</span>

- Update a container configuration:

`sudo $EDITOR /var/lib/container/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>`/etc/nixos/configuration.nix && sudo nixos-container update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>

- Enter an interactive shell session on an already-running container:

`sudo nixos-container root-login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">container_name</span>
