# Balancer

## Development

### Create and activate virtual environment

```bash
conda create --name balancer python=3.10
conda activate balancer
```


### Install packages

```shell
pip install -r engine/requirements.txt
```

### Run script locally

```shell
python engine/src/main.py --fronius-url http://192.168.1.10/ --influxdb-url http://localhost:8086
```

### Prepare Docker images

When you change the engine Dockerfile you have to rebuild the engine docker image with the command below! docker compose up does not rebuild the image itself!
```shell
docker compose build
```

## Run

```shell
docker compose up
```
