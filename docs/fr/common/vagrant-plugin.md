---
layout: page
title: common/vagrant-plugin (français)
description: "Gère les plugiciels Vagrant."
content_hash: efc39aaf80d5f8e189fd486efdeba58bc238e6c3
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/vagrant-plugin.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vagrant-plugin.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vagrant plugin

Gère les plugiciels Vagrant.
Voir aussi : `vagrant`.
Plus d'informations : <https://developer.hashicorp.com/vagrant/docs/cli/plugin>.

- Liste tous les plugiciels actuellement installés :

`vagrant plugin list`

- Installe un plugiciel depuis des dépôts distants, généralement RubyGems :

`vagrant plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>

- Installe un plugiciel à partir d’un fichier local :

`vagrant plugin install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/plugiciel.gem</span>

- Met à jour tous les plugiciels installés vers leur dernière version :

`vagrant plugin update`

- Met à jour un plugiciel à la dernière version :

`vagrant plugin update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>

- Désinstalle un plugiciel spécifique :

`vagrant plugin uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vagrant_vbguest</span>
