---
layout: page
title: windows/invoke-webrequest (English)
description: "Performs a HTTP/HTTPS request to the Web."
content_hash: 7bf20856df5bfaa14bad61c146bb3eea866d82c0
---
# Invoke-WebRequest

Performs a HTTP/HTTPS request to the Web.
This command can only be used through PowerShell.
More information: <https://docs.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- Download the contents of a URL to a file:

`Invoke-WebRequest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -OutFile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filename</span>

- Send form-encoded data (POST request of type `application/x-www-form-urlencoded`):

`Invoke-WebRequest -Method Post -Body @{ name='bob' } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/form</span>

- Send a request with an extra header, using a custom HTTP method:

`Invoke-WebRequest -Headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">@{ X-My-Header = '123' </span>`} -Method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Send data in JSON format, specifying the appropriate content-type header:

`Invoke-WebRequest -Body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"name":"bob"}'</span>`  -ContentType 'application/json' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/users/1234</span>

- Pass a username and password for server authentication:

`Invoke-WebRequest -Headers @{ Authorization = "Basic "+ [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes("myusername:mypassword")) } `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
