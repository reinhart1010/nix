---
layout: page
title: common/realpath (Nederlands)
description: "Toon het opgeloste absolute pad voor een bestand of map."
content_hash: 3e817152920c6aadad2f53d594f87082384d842a
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/realpath.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/realpath.html
    icon: bi bi-globe
tldri18n_status: 2
---
# realpath

Toon het opgeloste absolute pad voor een bestand of map.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html>.

- Toon het absolute pad voor een bestand of map:

`realpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Vereis dat alle padcomponenten bestaan:

`realpath --canonicalize-existing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Los ".." componenten op voordat symlinks worden gevolgd:

`realpath --logical `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Schakel symlink-uitbreiding uit:

`realpath --no-symlinks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Onderdruk foutmeldingen:

`realpath --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>
