---
layout: page
title: common/zoxide (Deutsch)
description: "Behält den Überblick über die am häufigsten verwendeten Verzeichnisse."
content_hash: d67d830c6c83d029d15d7cd9ead0b84c2247bcf3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/zoxide.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/zoxide.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zoxide

Behält den Überblick über die am häufigsten verwendeten Verzeichnisse.
Verwendet einen Ranking-Algorithmus, um zum besten Treffer zu navigieren.
Weitere Informationen: <https://github.com/ajeetdsouza/zoxide>.

- Wechsel zu dem Verzeichnis mit dem höchsten Rang, das "foo" im Namen enthält:

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Wechsel in das höchstrangige Verzeichnis, das "foo" und danach "bar" enthält:

`zoxide query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bar</span>

- Starte eine interaktive Verzeichnissuche (erfordert `fzf`):

`zoxide query --interactive`

- Füge ein Verzeichnis hinzu oder erhöhe seinen Rang:

`zoxide add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Entferne interaktiv ein Verzeichnis aus der Datenbank von `zoxide`:

`zoxide remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` --interactive`

- Generiere Shell-Konfigurationen für Befehls-Aliase (`z`, `za`, `zi`, `zq`, `zr`) für die angegebene Shell:

`zoxide init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash|fish|zsh</span>
