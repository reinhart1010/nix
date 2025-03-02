---
layout: page
title: common/printf (Nederlands)
description: "Formatteer en toon tekst."
content_hash: 9d700daa7cbed0834988e174b65d7bd95a75a072
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/printf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/printf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# printf

Formatteer en toon tekst.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- Toon een tekstbericht:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%s\n</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hallo wereld</span>`"`

- Toon een geheel getal in vetgedrukt blauw:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\e[1;34m%.3d\e[0m\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">42</span>

- Toon een drijvend-komma getal met het Unicode euroteken:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\u20AC %.2f\n</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">123.4</span>

- Toon een tekstbericht samengesteld met omgevingsvariabelen:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var1: %s\tvar2: %s\n</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$VAR1</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$VAR2</span>`"`

- Sla een geformatteerd bericht op in een variabele (werkt niet in Zsh):

`printf -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mijnvar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Dit is %s = %d\n" "een jaar" 2016</span>

- Toon een hexadecimaal, octaal en wetenschappelijk getal:

`printf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex=%x octal=%o scientific=%e</span>`" 0x`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">FF</span>` 0`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">377</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>
