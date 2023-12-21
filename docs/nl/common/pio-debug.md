---
layout: page
title: common/pio-debug (Nederlands)
description: "Debug PlatformIO projecten."
content_hash: ae5f63bf0283c293962293289293d458f17d2420
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-debug.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio debug

Debug PlatformIO projecten.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_debug.html>.

- Debug het PlatformIO project in de huidige map:

`pio debug`

- Debug een specifiek PlatformIO project:

`pio debug --project-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/platformio_project</span>

- Debug een specifieke omgeving:

`pio debug --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving</span>

- Debug een PlatformIO project met een specifiek configuratiebestand:

`pio debug --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/platformio.ini</span>

- Debug een PlatformIO project door gebruik te maken van de `gdb` debugger:

`pio debug --interface=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gdb_opties</span>
