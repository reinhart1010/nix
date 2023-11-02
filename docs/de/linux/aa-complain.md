---
layout: page
title: linux/aa-complain (Deutsch)
description: "Setze eine AppArmor-Richtlinie in den Beschwerde-Modus."
content_hash: 44f61505fab5c840bc0cbf0845400b62e2c54cdf
last_modified_at: 2023-11-02
related_topics:
  - title: English version
    url: /en/linux/aa-complain.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aa-complain

Setze eine AppArmor-Richtlinie in den Beschwerde-Modus.
Siehe auch: `aa-disable`, `aa-enforce`, `aa-status`.
Weitere Informationen: <https://gitlab.com/apparmor/apparmor/-/wikis/manpage_aa-complain.8>.

- Setze eine Richtlinie in den Beschwerde-Modus:

`sudo aa-complain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/profil</span>

- Setze Richtlinien in den Beschwerde-Modus:

`sudo aa-complain --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zum/profil</span>
