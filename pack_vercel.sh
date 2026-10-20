#!/usr/bin/env bash
# Packs the built site (docs/) into one base64 tarball for the Vercel standby host.
# Then deploy with the Vercel connector's create_deployment: team team_r6G6NiBTTNruKJSsAJYcvWNW,
# name "quietlychanged", target "production", one file "site.b64" (utf-8) from the path printed below,
# projectSettings: framework null, installCommand "true",
# buildCommand "mkdir -p public && base64 -d site.b64 | tar xz -C public", outputDirectory "public".
set -euo pipefail
cd "$(dirname "$0")/docs"
mkdir -p /workspace/vercel-stage
tar czf /workspace/vercel-stage/site.tgz --exclude=CNAME --exclude=.nojekyll .
base64 -w0 /workspace/vercel-stage/site.tgz > /workspace/vercel-stage/site.b64
echo /workspace/vercel-stage/site.b64
