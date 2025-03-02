---
layout: page
title: windows/gcrane-completion (Nederlands)
description: "Genereer het autocompletion script voor gcrane voor de opgegeven shell."
content_hash: 6c5f6bde0b503fd8cdb9f6f503bf81bd43641d16
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/windows/gcrane-completion.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/gcrane-completion.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane completion

Genereer het autocompletion script voor gcrane voor de opgegeven shell.
De beschikbare shells zijn `bash`, `fish`, `powershell` en `zsh`.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Genereer het autocompletion script voor je shell:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>

- Zet de completion beschrijvingen uit:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>` --no-descriptions`

- Laad completions in je huidige shellsessie (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Laad completions voor elke nieuwe sessie (powershell):

`gcrane completion powershell | Out-String | Invoke-Expression`

- Toon de help:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
