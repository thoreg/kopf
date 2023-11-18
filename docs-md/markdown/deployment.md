# Deployment

Kopf can be executed out of the cluster, as long as the environment is
authenticated to access the Kubernetes API.
But normally, the operators are usually deployed directly to the clusters.

## Docker image

First of all, the operator must be packaged as a docker image with Python 3.8 or newer:

```dockerfile
FROM python:3.11
ADD . /src
RUN pip install kopf
CMD kopf run /src/handlers.py --verbose
```

Build and push it to some repository of your choice.
Here, we will use [DockerHub](https://hub.docker.com/)
(with a personal account “nolar” – replace it with your name or namespace;
you may also want to add the versioning tags instead of the implied “latest”):

```bash
docker build -t nolar/kopf-operator .
docker push nolar/kopf-operator
```

#### SEE ALSO
Read [DockerHub documentation](https://docs.docker.com/docker-hub/)
for how to use it to push & pull the docker images.

## Cluster deployment

The best way to deploy the operator to the cluster is via the [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
object: in that case, it will be properly maintained alive and the versions
will be properly upgraded on the re-deployments.

For this, create the deployment file:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kopfexample-operator
spec:
  replicas: 1
  strategy:
    type: Recreate
  selector:
    matchLabels:
      application: kopfexample-operator
  template:
    metadata:
      labels:
        application: kopfexample-operator
    spec:
      serviceAccountName: kopfexample-account
      containers:
      - name: the-only-one
        image: nolar/kopf-operator
```

Please note that there is only one replica. Keep it so. If there will be
two or more operators running in the cluster for the same objects,
they will collide with each other and the consequences are unpredictable.
In case of pod restarts, only one pod should be running at a time too:
use `.spec.strategy.type=Recreate` (see the [documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/#recreate-deployment)).

Deploy it to the cluster:

```bash
kubectl apply -f deployment.yaml
```

No services or ingresses are needed (unlike in the typical web-app examples),
as the operator is not listening for any incoming connections,
but only makes the outcoming calls to the Kubernetes API.

## RBAC

The pod where the operator runs must have the permissions to access
and to manipulate the objects, both domain-specific and the built-in ones.
For the example operator, those are:

* `kind: ClusterKopfPeering` for the cross-operator awareness (cluster-wide).
* `kind: KopfPeering` for the cross-operator awareness (namespace-wide).
* `kind: KopfExample` for the example operator objects.
* `kind: Pod/Job/PersistentVolumeClaim` as the children objects.
* And others as needed.

For that, the [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (Role-Based Access Control) could be used
and attached to the operator’s pod via a service account.

Here is an example of what an RBAC config should look like
(remove the parts which are not needed: e.g. the cluster roles/bindings
for the strictly namespace-bound operator):

```yaml
---
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: "{{NAMESPACE}}"
  name: kopfexample-account
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kopfexample-role-cluster
rules:

  # Framework: knowing which other operators are running (i.e. peering).
  - apiGroups: [kopf.dev]
    resources: [clusterkopfpeerings]
    verbs: [list, watch, patch, get]

  # Framework: runtime observation of namespaces & CRDs (addition/deletion).
  - apiGroups: [apiextensions.k8s.io]
    resources: [customresourcedefinitions]
    verbs: [list, watch]
  - apiGroups: [""]
    resources: [namespaces]
    verbs: [list, watch]

  # Framework: admission webhook configuration management.
  - apiGroups: [admissionregistration.k8s.io/v1, admissionregistration.k8s.io/v1beta1]
    resources: [validatingwebhookconfigurations, mutatingwebhookconfigurations]
    verbs: [create, patch]

  # Application: read-only access for watching cluster-wide.
  - apiGroups: [kopf.dev]
    resources: [kopfexamples]
    verbs: [list, watch]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: "{{NAMESPACE}}"
  name: kopfexample-role-namespaced
rules:

  # Framework: knowing which other operators are running (i.e. peering).
  - apiGroups: [kopf.dev]
    resources: [kopfpeerings]
    verbs: [list, watch, patch, get]

  # Framework: posting the events about the handlers progress/errors.
  - apiGroups: [""]
    resources: [events]
    verbs: [create]

  # Application: watching & handling for the custom resource we declare.
  - apiGroups: [kopf.dev]
    resources: [kopfexamples]
    verbs: [list, watch, patch]

  # Application: other resources it produces and manipulates.
  # Here, we create Jobs+PVCs+Pods, but we do not patch/update/delete them ever.
  - apiGroups: [batch, extensions]
    resources: [jobs]
    verbs: [create]
  - apiGroups: [""]
    resources: [pods, persistentvolumeclaims]
    verbs: [create]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kopfexample-rolebinding-cluster
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kopfexample-role-cluster
subjects:
  - kind: ServiceAccount
    name: kopfexample-account
    namespace: "{{NAMESPACE}}"
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  namespace: "{{NAMESPACE}}"
  name: kopfexample-rolebinding-namespaced
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: kopfexample-role-namespaced
subjects:
  - kind: ServiceAccount
    name: kopfexample-account
```

And the created service account is attached to the pods as follows:

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      serviceAccountName: kopfexample-account
      containers:
      - name: the-only-one
        image: nolar/kopf-operator
```

Please note that the service accounts are always namespace-scoped.
There are no cluster-wide service accounts.
They must be created in the same namespace as the operator is going to run in
(even if it is going to serve the whole cluster).
