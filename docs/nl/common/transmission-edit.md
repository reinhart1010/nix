---
layout: page
title: common/transmission-edit (Nederlands)
description: "Wijzig aankondigings URL's van torrentbestanden."
content_hash: 6a9f2ae9273176b7ea149825eeeb9ae7ed8fda7e
last_modified_at: 2023-12-02
related_topics:
  - title: English version
    url: /en/common/transmission-edit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-edit

Wijzig aankondigings URL's van torrentbestanden.
Bekijk ook: `transmission`.
Meer informatie: <https://manned.org/transmission-edit>.

- Voeg een URL toe aan of verwijder deze uit de aankondigingslijst van een torrent:

`transmission-edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>

- Werk de toegangscode van een tracker bij in een torrentbestand:

`transmission-edit --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oude-toegangscode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe-toegangscode</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.torrent</span>
