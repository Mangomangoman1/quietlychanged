#!/usr/bin/env bash
# Packs the built site (docs/) into one base64 tarball for the Vercel standby host, and stages the repo-root vercel.json
# (301 redirects for thin service pages folded into services.html, written by the build).
# Then deploy with the Vercel connector's create_deployment: team team_r6G6NiBTTNruKJSsAJYcvWNW,
# name "quietlychanged", target "production", two files (utf-8) from the paths printed below: "site.b64" and "vercel.json",
# projectSettings: framework null, installCommand "true",
# buildCommand "mkdir -p public && base64 -d site.b64 | tar xz -C public", outputDirectory "public".
set -euo pipefail
cd "$(dirname "$0")/docs"
mkdir -p /workspace/vercel-stage
tar czf /workspace/vercel-stage/site.tgz --exclude=CNAME --exclude=.nojekyll .
base64 -w0 /workspace/vercel-stage/site.tgz > /workspace/vercel-stage/site.b64
cp ../vercel.json /workspace/vercel-stage/vercel.json
echo /workspace/vercel-stage/site.b64
echo /workspace/vercel-stage/vercel.json
