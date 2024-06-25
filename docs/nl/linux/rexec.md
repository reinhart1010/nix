---
layout: page
title: linux/rexec (Nederlands)
description: "Voer een commando uit op een externe host."
content_hash: 039402d853c5fbeda9c277bbf5c748caa3a67bbd
last_modified_at: 2024-06-25
related_topics:
  - title: English version
    url: /en/linux/rexec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rexec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rexec

Voer een commando uit op een externe host.
Let op: Gebruik `rexec` met voorzichtigheid, omdat het gegevens in platte tekst verzendt. Overweeg veilige alternatieven zoals SSH voor versleutelde communicatie.
Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rexec-invocation.html>.

- Voer een commando uit op een externe [h]ost:

`rexec -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Specificeer de externe [g]ebruikersnaam op een externe [h]ost:

`rexec -username=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux</span>

- Redirect `stdin` van `/dev/null` op een externe [h]ost:

`rexec --no-err -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>

- Specificeer de externe [P]oort op een externe [h]ost:

`rexec -P=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` -h=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">remote_host</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls -l</span>
