---
layout: page
title: linux/nixos-rebuild (English)
description: "Reconfigure a NixOS machine."
content_hash: 495af7eab7d1193ddd25e224952ce0bbe7b6d135
---
# nixos-rebuild

Reconfigure a NixOS machine.
More information: <https://nixos.org/nixos/manual/#sec-changing-config>.

- Build and switch to the new configuration, making it the boot default:

`sudo nixos-rebuild switch`

- Build and switch to the new configuration, making it the boot default and naming the boot entry:

`sudo nixos-rebuild switch -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Build and switch to the new configuration, making it the boot default and installing updates:

`sudo nixos-rebuild switch --upgrade`

- Rollback changes to the configuration, switching to the previous generation:

`sudo nixos-rebuild switch --rollback`

- Build the new configuration and make it the boot default without switching to it:

`sudo nixos-rebuild boot`

- Build and activate the new configuration, but don't make a boot entry (for testing purposes):

`sudo nixos-rebuild test`

- Build the configuration and open it in a virtual machine:

`sudo nixos-rebuild build-vm`
