---
layout: page
title: linux/ndctl (English)
description: "Utility for managing Non-Volatile DIMMs."
content_hash: 1dce65e735eca09016e5f0cfee570d4878362d8d
---
# ndctl

Utility for managing Non-Volatile DIMMs.

- Create an 'fsdax' mode namespace:

`ndctl create-namespace --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fsdax</span>

- Change the mode of a namespace to 'raw':

`ndctl create-namespace --reconfigure=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>` --mode=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw</span>

- Check a sector mode namespace for consistency, and repair if needed:

`ndctl check-namespace --repair `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>

- List all namespaces, regions, and buses (including disabled ones):

`ndctl list --namespaces --regions --buses --idle`

- List a specific namespace and include lots of additional information:

`ndctl list -vvv --namespace=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>

- Run a monitor to watch for SMART health events for NVDIMMs on the 'ACPI.NFIT' bus:

`ndctl monitor --bus=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ACPI.NFIT</span>

- Remove a namespace (when applicable) or reset it to an initial state:

`ndctl destroy-namespace --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespaceX.Y</span>
