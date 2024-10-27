---
layout: page
title: osx/gcrane-completion (Nederlands)
description: "Genereer het autocompletion script voor gcrane voor de opgegeven shell."
content_hash: 1fbc3b9ac0768469650d81a3f0a6fdcb349934a8
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/osx/gcrane-completion.html
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

- Laad completions in je huidige shellsessie (bash/zsh):

`source <(gcrane completion bash/zsh)>`

- Laad completions in je huidige shellsessie (fish):

`gcrane completion fish | source`

- Laad completions voor elke nieuwe sessie (bash):

`gcrane completion bash > $(brew --prefix)/etc/bash_completion.d/gcrane`

- Laad completions voor elke nieuwe sessie (zsh):

`gcrane completion zsh > $(brew --prefix)/share/zsh/site-functions/_gcrane`

- Laad completions voor elke nieuwe sessie (fish):

`gcrane completion fish > ~/.config/fish/completions/gcrane.fish`

- Toon help:

`gcrane completion `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">shell_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
