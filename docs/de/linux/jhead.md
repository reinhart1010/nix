---
layout: page
title: linux/jhead (Deutsch)
description: "Manipulation der Zeitstempel und EXIF Daten in Bilddateien."
content_hash: 841bc9b140fc9e3f239cef1c74c2e02750b9b38f
last_modified_at: 2024-01-05
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/jhead.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># jhead

Manipulation der Zeitstempel und EXIF Daten in Bilddateien.
Weitere Informationen: <https://www.sentex.net/~mwandel/jhead/usage.html>.

- Zeige alle EXIF Daten eines JPEG Bildes:

`jhead `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.jpg</span>

- Setze die Dateizeit auf die EXIF Zeit (d.h. die Dateizeit wird geändert):

`jhead -ft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.jpg</span>

- Setze die EXIF Zeit auf die Dateizeit (d.h. die EXIF Zeit wird geändert):

`jhead -dsft `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.jpg</span>

- Benenne alle Dateinamen der JPEG Bilder nach EXIF Datum/Zeit um (Format: Jahr_Monat_Tag-Stunde_Minute_Sekunde.jpg):

`jhead -n%Y_%m_%d-%H_%M_%S *.jpg`

- Rotiere alle Bilder im aktuellen Ordner verlustfrei (Basierend auf dem EXIF Orientierungstag):

`jhead -autorot *.jpg`

- Korrigiere den EXIF Zeitstempel (Format: Stunden:Minuten:Sekunden). Im Beispiel wird jedes Bild eine Stunde in die Vergangenheit geschoben (z.B. Zeitumstellung vergessen):

`jhead -ta-1:00:00 *.jpg`

- Entferne alle Metadaten einschließlich der Vorschaubilder aus der JPEG Datei:

`jhead -purejpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/bild.jpg</span>
