---
layout: page
title: linux/busctl (English)
description: "Introspect and monitor the D-Bus bus."
content_hash: ae5278719154758c4d4a95b3cac67ed416a0491a
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# busctl

Introspect and monitor the D-Bus bus.
More information: <https://www.freedesktop.org/software/systemd/man/busctl.html>.

- Show all peers on the bus, by their service names:

`busctl list`

- Show process information and credentials of a bus service, a process, or the owner of the bus (if no parameter is specified):

`busctl status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service|pid</span>

- Dump messages being exchanged. If no service is specified, show all messages on the bus:

`busctl monitor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service1 service2 ...</span>

- Show an object tree of one or more services (or all services if no service is specified):

`busctl tree `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service1 service2 ...</span>

- Show interfaces, methods, properties and signals of the specified object on the specified service:

`busctl introspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/object</span>

- Retrieve the current value of one or more object properties:

`busctl get-property `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/object</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">property_name</span>

- Invoke a method and show the response:

`busctl call `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">service</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/object</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">interface_name</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">method_name</span>
