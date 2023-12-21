---
layout: page
title: common/pio-update (Nederlands)
description: "Update geïnstalleerde PlatformIO Core pakketten, ontwikkelplatformen en globale bibliotheken."
content_hash: facf406d1954fd90181a34802c91b9fe60ce4a1f
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-update.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio update

Update geïnstalleerde PlatformIO Core pakketten, ontwikkelplatformen en globale bibliotheken.
Bekijk ook: `pio platform update`, `pio lib update`.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/cmd_update.html>.

- Voer een volledige update uit van alle pakketten, ontwikkelplatformen en globale bibliotheken:

`pio update`

- Update alleen kern pakketten (sla platformen en bibliotheken over):

`pio update --core-packages`

- Controleer voor nieuwe versies van pakketten, platformen en bibliotheken, maar update ze niet:

`pio update --dry-run`
