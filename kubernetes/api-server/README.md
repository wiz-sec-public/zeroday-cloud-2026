# Kubernetes API Server

## Objective and eligibility

Achieve remote code execution in the Kubernetes API Server without client credentials and execute `/flag.sh k8s-apiserver` in the API Server static pod. Authentication bypasses count only when the complete exploit begins without a token, certificate, or kubeconfig.

The target is the Kubernetes API Server and its default in-process stack. The Docker host, container runtime, node kernel, and other control-plane components are excluded.

## Local environment

For your convenience, we have provided a KinD (Kubernetes in Docker) setup that replicates the official competition environment. An exploit that functions correctly against this local setup is highly likely to succeed during the live demonstration.

```bash
kind create cluster --name zdc-api-server --wait 120s --config - <<'EOF'
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
EOF

api_server="$(kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}')"
curl -k "${api_server}/healthz"
```

## Submission & Eligibility Guidelines

If your exploit requires a configuration different from the one provided or has other specific prerequisites, you must contact the competition organizers in advance to ensure the exploit's eligibility for scoring.

For all inquiries and clarifications, please contact us at zerodaycloud@wiz.io
