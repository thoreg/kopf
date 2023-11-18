# Command-line options

Most of the options relate to `kopf run`, though some are shared by other
commands, such as `kopf freeze` and `kopf resume`.

## Scripting options

### -m, --module

A semantical equivalent to `python -m` — which importable modules
to import on startup.

## Logging options

### --quiet

Be quiet: only show warnings and errors, but not the normal processing logs.

### --verbose

Show what Kopf is doing, but hide the low-level asyncio & aiohttp logs.

### --debug

Extremely verbose: log all the asyncio internals too, so as the API traffic.

### --log-format (plain|full|json)

See more in [Configuration](configuration.md).

### --log-prefix, --no-log-prefix

Whether to prefix all object-related messages with the name of the object.
By default, the prefixing is enabled.

### --log-refkey

For JSON logs, under which top-level key to put the object-identifying
information, such as its name, namespace, etc.

## Scope options

### -n, --namespace

Serve this namespace or all namespaces mathing the pattern
(or excluded from patterns). The option can be repeated multiple times.

#### SEE ALSO
[Scopes](scopes.md) for the pattern syntax.

### -A, --all-namespaces

Serve the whole cluster. This is different from `--namespace *`:
with `--namespace *`, the namespaces are monitored, and every resource
in every namespace is watched separately, starting and stopping as needed;
with `--all-namespaces`, the cluster endpoints of the Kubernetes API
are used for resources, the namespaces are not monitored.

## Probing options

### --liveness

The endpoint where to serve the probes and health-checks.
E.g. `http://0.0.0.0:1234/`. Only `http://` is currently supported.
By default, the probing endpoint is not served.

#### SEE ALSO
[Health-checks](probing.md)

## Peering options

### --standalone

Disable any peering or auto-detection of peering. Run strictly as if
this is the only instance of the operator.

### --peering

The name of the peering object to use. Depending on the operator’s scope
([`--all-namespaces`](#cmdoption-A) vs. [`--namespace`](#cmdoption-n), see [Scopes](scopes.md)),
it is either `kind: KopfPeering` or `kind: ClusterKopfPeering`.

If specified, the operator will not run until that peering exists
(for the namespaced operators, until it exists in each served namespace).

If not specified, the operator checks for the name “default” and uses it.
If the “default” peering is absent, the operator runs in standalone mode.

### --priority

Which priority to use for the operator. An operator with the highest
priority wins the peering competitions and handlers the resources.

The default priority is `0`; [`--dev`](#cmdoption-dev) sets it to `666`.

#### SEE ALSO
[Peering](peering.md)

## Development mode

### --dev

Run in the development mode. Currently, this implies `--priority=666`.
Other meanings can be added in the future, such as automatic reloading
of the source code.
