# BUILD: docker build --force-rm=true -t concourse-fake-resource .

FROM python:3.5-alpine

# install assets
RUN mkdir -p /opt/resource
ADD assets/* /opt/resource/
