VERSION=v1
DOCKERUSER=anushkumarv

build:
	docker build -f Dockerfile -t hyptaas-job-status-service .

push:
	docker tag hyptaas-job-status-service $(DOCKERUSER)/hyptaas-job-status-service:$(VERSION)
	docker push $(DOCKERUSER)/hyptaas-job-status-service:$(VERSION)
	docker tag hyptaas-job-status-service $(DOCKERUSER)/hyptaas-job-status-service:latest
	docker push $(DOCKERUSER)/hyptaas-job-status-service:latest