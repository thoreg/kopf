# Alternatives

## Metacontroller

The closest equivalent of Kopf is [Metacontroller](https://metacontroller.github.io/metacontroller/).
It targets the same goal as Kopf does:
to make the development of Kubernetes operators easy,
with no need for in-depth knowledge of Kubernetes or Go.

However, it does that in a different way than Kopf does:
with a few YAML files describing the structure of your operator
(besides the custom resource definition),
and by wrapping your core domain logic into the Function-as-a-Service
or into the in-cluster HTTP API deployments,
which in turn react to the changes in the custom resources.

An operator developer still has to implement the infrastructure
of the API calls in these HTTP APIs and/or Lambdas.
The APIs must be reachable from inside the cluster,
which means that they must be deployed there.

Kopf, on the other hand, attempts to keep things explicit
(as per the [Zen of Python](https://www.python.org/dev/peps/pep-0020/): *explicit is better than implicit*),
keeping the whole operator’s logic in one place, in one syntax (Python).

Kopf also makes the effort to keep the operator development human-friendly,
which means at least the ease of debugging (e.g. with the breakpoints,
running in a local IDE, not in the cloud), the readability of the logs,
and other little pleasant things.

And also Kopf allows to write *any* arbitrary domain logic of the resources,
especially if it spans over long periods (hours, days if needed),
and is not limited to the timeout restrictions of the HTTP APIs with their
expectation of nearly-immediate outcome (i.e. in seconds or milliseconds).

Metacontroller, however, is more mature, 1.5 years older than Kopf,
and is backed by Google, who originally developed Kubernetes itself.

Unlike Kopf, Metacontroller supports the domain logic in any languages
due to its language-agnostic nature of HTTP APIs.

## Side8’s k8s-operator

Side8’s [k8s-operator](https://github.com/side8/k8s-operator) is another direct equivalent.
It was the initial inspiration for writing Kopf.

Side8’s k8s-operator is written with Python3 and allows to write
the domain logic in the apply/delete scripts in any language.
The scripts run locally on the same machine where the controller is running
(usually the same pod, or a developer’s computer).

However, the interaction with the script relies on stdout output
and the environment variables as the input,
which is only good if the scripts are written in shell/bash.
Writing the complicated domain logic in bash can be troublesome.

The scripts in other languages, such as Python, are supported but require
the inner infrastructure logic to parse the input and to render the output
and to perform the logging properly:
e.g., so that no single byte of garbage output is ever printed to stdout,
or so that the resulting status is merged with the initial status, etc –
which kills the idea of pure domain logic and no infrastructure logic
in the operator codebase.

## CoreOS Operator SDK & Framework

[CoreOS Operator SDK](https://github.com/operator-framework/operator-sdk) is not an operator framework.
It is an SDK, i.e. a Software Development Kit,
which generates the skeleton code for the operators-to-be,
and users should enrich it with the domain logic code as needed.

[CoreOS Operator Framework](https://coreos.com/operators/), of which the abovementioned SDK is a part,
is a bigger, more powerful, but very complicated tool for writing operators.

Both are developed purely for Go-based operators.
No other languages are supported.

From the CoreOS’es point of view, an operator is a method of packaging
and managing a Kubernetes-native application (presumably of any purpose,
such as MySQL, Postgres, Redis, ElasticSearch, etc) with Kubernetes APIs
(e.g. the custom resources of ConfigMaps) and `kubectl` tooling.
They refer to operators as
“*the runtime that manages this type of application on Kubernetes*.”

Kopf uses a more generic approach,
where the operator *is* the application with the domain logic in it.
Managing other applications inside of Kubernetes is just one special case
of such a domain logic, but the operators could also be used to manage
the applications outside of Kubernetes (via their APIs), or to implement
the direct actions without any supplementary applications at all.

#### SEE ALSO
* [https://coreos.com/operators](https://coreos.com/operators)
* [https://coreos.com/blog/introducing-operator-framework](https://coreos.com/blog/introducing-operator-framework)
* [https://enterprisersproject.com/article/2019/2/kubernetes-operators-plain-english](https://enterprisersproject.com/article/2019/2/kubernetes-operators-plain-english)
