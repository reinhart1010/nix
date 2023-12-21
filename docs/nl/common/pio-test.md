---
layout: page
title: common/pio-test (Nederlands)
description: "Voer lokale testen uit op een PlatformIO project."
content_hash: 8e95bbd72b3bfde04e8d3374ced439b87cf4a5f3
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio test

Voer lokale testen uit op een PlatformIO project.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- Voer alle testen in alle omgevingen uit van het huidige PlatformIO project:

`pio test`

- Test alleen op specifieke omgevingen:

`pio test --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving1</span>` --environment `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">omgeving2</span>

- Voer alleen testen uit die qua naam overeenkomen met een specifiek glob patroon:

`pio test --filter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patroon</span>`"`

- Negeer testen die qua naam overeenkomen met een specifiek glob patroon:

`pio test --ignore "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patroon</span>`"`

- Specificeer een poort voor firmware uploading:

`pio test --upload-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">upload_poort</span>

- Specificeer een aangepast configuratiebestand voor het uitvoeren van de testen:

`pio test --project-conf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/platformio.ini</span>
