---
layout: page
title: linux/mknod (Nederlands)
description: "Maak speciale bestanden voor blok- of tekenapparaten aan."
content_hash: d9ea8a278ea0d256587eed250f65e940fe041692
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/linux/mknod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mknod

Maak speciale bestanden voor blok- of tekenapparaten aan.
Meer informatie: <https://www.gnu.org/software/coreutils/mknod>.

- Maak een blokapparaat aan:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groot_apparaatnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klein_apparaatnummer</span>

- Maak een tekenapparaat aan:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groot_apparaatnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klein_apparaatnummer</span>

- Maak een FIFO (queue) apparaat aan:

`sudo mknod `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` p`

- Maak een apparaatbestand aan met de standaard SELinux-beveiligingscontext:

`sudo mknod -Z `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">groot_apparaatnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">klein_apparaatnummer</span>
