---
layout: page
title: common/case (español)
description: "Construcción de Bash para crear sentencias condicionales multi-elección."
content_hash: 48138f253afe3e14156bde89cb2c4b5e55e876d7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/case.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/case.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/case.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/case.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/case.html
    icon: bi bi-globe
tldri18n_status: 2
---
# case

Construcción de Bash para crear sentencias condicionales multi-elección.
Más información: <https://www.gnu.org/software/bash/manual/bash.html#index-case>.

- Compara una variable con literales de cadena para decidir qué comando ejecutar:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$COUNTRULE</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">palabras</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w LEAME</span>` ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">líneas</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l LEAME</span>` ;; esac`

- Combina patrones con |, usa * como patrón de reserva:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$COUNTRULE</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[wW]|palabras</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w LEAME</span>` ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[lL]|líneas</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l LEAME</span>` ;; *) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "¿qué?"</span>` ;; esac`

- Permite la coincidencia de múltiples patrones:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$ANIMAL</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gato</span>`) echo "Es un gato" ;;& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gato|perro</span>`) echo "Es un gato o un perro" ;;& *) echo "Fallback" ;; esac`

- Continúa con los comandos del siguiente patrón sin comprobar el patrón:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$ANIMAL</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gato</span>`) echo "Es un gato" ;& `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">perro</span>`) echo "O es un perro o es un gato" ;& *) echo "Fallback" ;; esac`
