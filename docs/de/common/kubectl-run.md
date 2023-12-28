---
layout: page
title: common/kubectl-run (Deutsch)
description: "Pods in Kubernetes ausführen. Gibt den Pod-Generator an, um einen deprecation Fehler in einigen Kubernetes Versionen zu vermeiden."
content_hash: fd5bc097991c31153683e196913a45474b8aed16
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/kubectl-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# kubectl run

Pods in Kubernetes ausführen. Gibt den Pod-Generator an, um einen deprecation Fehler in einigen Kubernetes Versionen zu vermeiden.
Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#run>.

- Starte einen nginx-Pod und gib Port 80 frei:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --port 80`

- Starte einen nginx-Pod und setze die Umgebungsvariable TEST_VAR:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --env="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">TEST_VAR</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testing</span>`"`

- Zeige API-Aufrufe an, die zur Erstellung eines Nginx-Containers erfolgen würden:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nginx-dev</span>` --image=nginx --dry-run=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|server|client</span>

- Führe einen Ubuntu-Pod interaktiv aus, starte ihn nie neu und entferne ihn, wenn er beendet wird:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temp-ubuntu</span>` --image=ubuntu:22.04 --restart=Never --rm -- /bin/bash`

- Führe einen Ubuntu-Pod aus, überschreibe den Standardbefehl mit echo und gib eigene Argumente an:

`kubectl run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">temp-ubuntu</span>` --image=ubuntu:22.04 --command -- echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>
