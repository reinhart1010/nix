---
layout: page
title: common/podman-login (español)
description: "Inicia sesión en un registro de contenedores (container registry)."
content_hash: ccc267fde5f4634ca69b27a38487ef942b42ba3f
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/podman-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# podman login

Inicia sesión en un registro de contenedores (container registry).
Nota: la ruta predeterminada de archivo de autenticación (authfile) en Linux es `$XDG_RUNTIME_DIR/containers/auth.json`, que generalmente se almacena en un `tmpfs` (en RAM).
Más información: <https://docs.podman.io/en/latest/markdown/podman-login.1.html>.

- Inicia sesión en un registro (no permanente en Linux; persistente en Windows/macOS):

`podman login `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.example.org</span>

- Inicia sesión en un registro persistentemente en Linux:

`podman login --authfile $HOME/.config/containers/auth.json `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.example.org</span>

- Inicia sesión en un registro inseguro (HTTP):

`podman login --tls-verify=false `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">registry.example.org</span>
