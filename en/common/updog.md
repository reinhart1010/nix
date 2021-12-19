---
layout: page
title: common/updog (English)
description: "A replacement for Python's SimpleHTTPServer."
content_hash: e73319b5f41a24476f2c3eab64bf02e5a01d0292
---
# updog

A replacement for Python's SimpleHTTPServer.
It allows uploading and downloading via HTTP/S, can set ad hoc SSL certificates and use HTTP basic auth.
More information: <https://github.com/sc0tfree/updog>.

- Start a HTTP server for the current directory:

`updog`

- Start a HTTP server for a specified directory:

`updog --directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/path/to/directory</span>

- Start a HTTP server on a specified port:

`updog --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">port</span>

- Start a HTTP server with a password (To log in, leave the username blank and enter the password in the password field):

`updog --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Enable transport encryption via SSL :

`updog --ssl`
