---
layout: page
title: common/bower (italiano)
description: "Un manager di pacchetti ottimizzato per sviluppo web front-end."
content_hash: 63457cba26418afe2a9434c6ee35ff4f63ebd00a
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/bower.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bower.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bower.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bower

Un manager di pacchetti ottimizzato per sviluppo web front-end.
Un pacchetto può essere una abbreviazione utente/repo GitHub, un endpoint Git, un URL o un pacchetto registrato.
Maggiori informazioni: <https://bower.io/>.

- Installa le dipendenze di un progetto, listate nel suo file `bower.json`:

`bower install`

- Installa pacchetti nella directory bower_components:

`bower install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Disinstalla pacchetti localmente rimuovendolo dalla directory bower_components:

`bower uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Elenca pacchetti locali e possibili aggiornamenti:

`bower list`

- Mostra aiuto per un comando di bower:

`bower help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Crea un file bower.json per i tuoi pacchetti:

`bower init`

- Installa unoa specifica versione di una dipendenza ed aggiungila al file `bower.json`:

`bower install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_locale</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versione</span>` --save`
