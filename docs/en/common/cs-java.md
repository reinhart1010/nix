---
layout: page
title: common/cs-java (English)
description: "The `java` and `java-home` commands fetch and install JVMs. The `java` command runs them too."
content_hash: 68416af321cd9dd952306e75171b71befd545df5
last_modified_at: 2024-01-30
tldri18n_status: 2
---
# cs java

The `java` and `java-home` commands fetch and install JVMs. The `java` command runs them too.
More information: <https://get-coursier.io/docs/cli-java>.

- Display Java version by using coursier:

`cs java -version`

- Call a specific Java version with custom properties using coursier:

`cs java --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_version</span>` -Xmx32m -X`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">another_jvm_opt</span>` -jar `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/jar_name.jar</span>

- List all the available JVM in the coursier default index:

`cs java --available`

- List all the installed JVM in the system with his own location:

`cs java --installed`

- Set the a specific JVM as one-off "default" for the shell instance:

`cs java --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_version</span>` --env`

- Revert the changes for the default JVM settings:

`eval "$(cs java --disable)"`

- Set a specific JVM as default for the whole system:

`cs java --jvm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_name</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jvm_version</span>` --setup`
