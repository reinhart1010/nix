---
layout: page
title: common/chroot (Nederlands)
description: "Voer commando of interactieve shell uit met een speciale hoofdmap."
content_hash: 1c9131bb40da36617f53a28165921190db2ba1ab
last_modified_at: 2024-12-12
related_topics:
  - title: Deutsch version
    url: /de/common/chroot.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/chroot.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/chroot.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/chroot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/chroot.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/chroot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chroot

Voer commando of interactieve shell uit met een speciale hoofdmap.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/chroot-invocation.html>.

- Voer commando uit met gegeven hoofdmap:

`chroot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/nieuwe/hoofdmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Specificeer gebruiker en groep (ID of naam) om te gebruiken:

`chroot --userspec=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker:groep</span>
