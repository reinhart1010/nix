---
layout: page
title: linux/mknod (Nederlands)
description: "Maak speciale bestanden voor blok- of tekenapparaten aan."
content_hash: 5a7650f058f7125c6eaab93b329f2da0b51d8ef6
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/mknod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mknod.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mknod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mknod

Maak speciale bestanden voor blok- of tekenapparaten aan.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/mknod-invocation.html>.

- Maak een blokapparaat aan:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groot_apparaatnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klein_apparaatnummer</span>

- Maak een tekenapparaat aan:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groot_apparaatnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klein_apparaatnummer</span>

- Maak een FIFO (queue) apparaat aan:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` p`

- Maak een apparaatbestand aan met de standaard SELinux-beveiligingscontext:

`sudo mknod -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groot_apparaatnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klein_apparaatnummer</span>
