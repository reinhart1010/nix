---
layout: page
title: linux/gcrane-completion (Nederlands)
description: "Genereer het autocompletion script voor gcrane voor de opgegeven shell."
content_hash: 80ea65c1a3f7d62736cffcdf8fb39e232441dd6d
last_modified_at: 2024-10-26
related_topics:
  - title: English version
    url: /en/linux/gcrane-completion.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/gcrane-completion.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gcrane completion

Genereer het autocompletion script voor gcrane voor de opgegeven shell.
De beschikbare shells zijn `bash`, `fish`, `powershell` en `zsh`.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Genereer het autocompletion script voor je shell:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>

- Zet de completion beschrijvingen uit:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>` --no-descriptions`

- Laad completions in je huidige shellsessie (bash/zsh):

`source <(gcrane completion bash/zsh)>`

- Laad completions in je huidige shellsessie (fish):

`gcrane completion fish | source`

- Laad completions voor elke nieuwe sessie (bash):

`gcrane completion bash > /etc/bash_completion.d/gcrane`

- Laad completions voor elke nieuwe sessie (zsh):

`gcrane completion zsh > "${fpath[1]}/_gcrane"`

- Laad completions voor elke nieuwe sessie (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- Toon help:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
