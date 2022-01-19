---
layout: page
title: common/vagrant (English)
description: "Manage lightweight, reproducible, and portable development environments."
content_hash: d21dd1e8aa66519dea9769894cd5e46b5ad43e54
---
# vagrant

Manage lightweight, reproducible, and portable development environments.
More information: <https://www.vagrantup.com>.

- Create Vagrantfile in current directory with the base Vagrant box:

`vagrant init`

- Create Vagrantfile with the Ubuntu 20.04 (Focal Fossa) box from HashiCorp Atlas:

`vagrant init ubuntu/focal64`

- Start and provision the vagrant environment:

`vagrant up`

- Suspend the machine:

`vagrant suspend`

- Halt the machine:

`vagrant halt`

- Connect to machine via SSH:

`vagrant ssh`

- Output the SSH configuration file of the running Vagrant machine:

`vagrant ssh-config`
