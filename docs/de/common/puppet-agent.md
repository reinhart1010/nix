---
layout: page
title: common/puppet-agent (Deutsch)
description: "Ruft die Client-Konfiguration eines Puppetservers ab und setzt diese auf dem System um."
content_hash: eb194c7ac2f5db1770b0a994b11d721c19664048
related_topics:
  - title: English version
    url: /en/common/puppet-agent.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/puppet-agent.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># puppet agent

Ruft die Client-Konfiguration eines Puppetservers ab und setzt diese auf dem System um.
Weitere Informationen: <https://puppet.com/docs/puppet/7/man/agent.html>.

- Registriere die Node bei einem Puppetserver und wende den empfangenen Katalog an:

`puppet agent --test --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">puppetserver_fqdn</span>` --serverport `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>` --waitforcert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poll_zeit</span>

- Führe den Agenten im Hintergrund aus (nutzt die Einstellungen von `/opt/puppetlabs/puppet/puppet.conf`):

`puppet agent`

- Führe den Agenten einmal im Vordergrund aus und beende:

`puppet agent --test`

- Führe den Agenten im Dry-Modus aus:

`puppet agent --test --noop`

- Protokolliere jede ausgewertete Ressource (selbst wenn sich nichts geändert hat):

`puppet agent --test --evaltrace`

- Deaktiviere den Agenten:

`puppet agent --disable "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nachricht</span>`"`

- Aktiviere den Agenten:

`puppet agent --enable`
