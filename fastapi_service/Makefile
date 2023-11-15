build_faster_image:
	gcloud builds submit --pack image=us-central1-docker.pkg.dev/opentelemetry-demo-405200/cloud-run-source-deploy/faster

build_collector_image:
	gcloud builds submit collector --tag us-central1-docker.pkg.dev/opentelemetry-demo-405200/cloud-run-source-deploy/otel-collector-metrics

replace_service:
	gcloud run services replace service.yaml
