---
layout: page
title: common/puppet-apply (Deutsch)
description: "Wende ein Puppet-Manifest lokal an."
content_hash: a2d26333c35181c5824dbdfe1eaec2b54251a5d4
related_topics:
  - title: English version
    url: /en/common/puppet-apply.html
    icon: bi bi-globe
---
# puppet apply

Wende ein Puppet-Manifest lokal an.
Weitere Informationen: <https://puppet.com/docs/puppet/7/man/apply.html>.

- Wende ein Manifest an:

`puppet apply `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/manifest</span>

- Führe Puppetcode aus:

`puppet apply --execute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">code</span>

- Benutze ein bestimmtes Modulverzeichnis und Hiera-Konfigurationsdatei:

`puppet apply --modulepath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/ordner</span>` --hiera_config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/manifest</span>
