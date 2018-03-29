# Concourse fake resource

This is a dummy resource for Concourse CI.
The resource will always return the same reference id.

## Usage

Example pipeline definition
```yml
resource_types:
  - name: fake
    type: docker-image
    source:
        repository: sispheor/concourse-fake-resource
        tag: latest

resources:
  - name: fake-resource
    type: fake

jobs:
  - name: hello
    plan:
      - get: fake-resource
      - task: hello-world
        config:
          platform: linux
          image_resource:
            type: docker-image
            source: {repository: alpine}
          run:
            path: echo
            args: ["Hello, world!"]
      - put: fake-resource
```

## Docker

How to build this image
```
docker build --force-rm=true -t concourse-fake-resource .
```

## Development

Concourse will call each script in the assets folder (check, in, out) by passing the resource config as a json in stdin and other parameters like target directory as argument.

Run `check`
```
cat tests/check.json | python assets/check
```

Run `in`
```
cat tests/in.json | python assets/in
```

Run `out`
```
cat tests/out.json | python assets/out
```
