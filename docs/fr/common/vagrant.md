---
layout: page
title: common/vagrant (français)
description: "Gère des environnements de développement légers, reproductibles et portables."
content_hash: b0acc71bfd8599314e06f5b448344fad2b1e2a0d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/vagrant.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vagrant.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vagrant

Gère des environnements de développement légers, reproductibles et portables.
Plus d'informations : <https://www.vagrantup.com>.

- Crée un fichier Vagrantfile dans le répertoire actuel avec l'image Vagrant de base :

`vagrant init`

- Crée un fichier Vagrantfile avec l'image Ubuntu 20.04 (Focal Fossa) depuis HashiCorp Atlas :

`vagrant init ubuntu/focal64`

- Démarre et configure l’environnement Vagrant :

`vagrant up`

- Suspend la machine :

`vagrant suspend`

- Arrête la machine :

`vagrant halt`

- Se connecte à la machine via SSH :

`vagrant ssh`

- Affiche la configuration SSH de la machine Vagrant en cours d’exécution :

`vagrant ssh-config`

- Liste toutes les images locales :

`vagrant box list`
