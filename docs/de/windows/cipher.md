---
layout: page
title: windows/cipher (Deutsch)
description: "Zeigt oder Verändert die Verschlüsselung von Verzeichnissen und Dateien auf NTFS-Laufwerken."
content_hash: 2c2034b6b46670bbfc3749d4e669416165683888
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/cipher.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cipher.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cipher.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cipher

Zeigt oder Verändert die Verschlüsselung von Verzeichnissen und Dateien auf NTFS-Laufwerken.
Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/cipher>.

- Informationen über die Verschlüsselung einer bestimmten Datei oder eines Verzeichnisses anzeigen lassen:

`cipher /c:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Verschlüssle eine Datei oder ein Verzeichnis (nachträglich hinzugefügte Dateien werden ebenfalls verschlüsselt, da das Verzeichnis markiert ist):

`cipher /e:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Entschlüssle eine Datei oder ein Verzeichnis:

`cipher /d:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>

- Entferne eine Datei oder ein Verzeichnis sicher:

`cipher /w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_oder_verzeichnis</span>
