---
layout: page
title: windows/invoke-webrequest (Nederlands)
description: "Voer een HTTP/HTTPS request uit naar het Web."
content_hash: 88302961460571da14789add7aeeac137d06ee72
last_modified_at: 2023-11-18
related_topics:
  - title: English version
    url: /en/windows/invoke-webrequest.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/invoke-webrequest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/invoke-webrequest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># Invoke-WebRequest

Voer een HTTP/HTTPS request uit naar het Web.
Dit commando kan alleen gebruikt worden via PowerShell.
Meer informatie: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Download de inhoud van een URL naar een bestand:

`Invoke-WebRequest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -OutFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>

- Stuur form-gecodeerde gegevens (POST request van het type `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- Stuur een request met een extra header, door gebruik te maken van een aangepast HTTP methode:

`Invoke-WebRequest -Headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@{ X-My-Header = '123' }</span>` -Method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Stuur gegevens in JSON formaat en specificieer de juiste content-type header:

`Invoke-WebRequest -Body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>` -ContentType 'application/json' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/users/1234</span>

- Stuur een gebruikersnaam en wachtwoord voor een server authenticatie:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
