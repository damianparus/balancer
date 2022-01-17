# Balancer

Collect data from Fronius inverter and Fronius Smart Meter 63A-3 data and save in Influxdb for Grafana. 
The installation is based on docker images. Grafana presents the state of the energy storage in the grid to be used.

![Screenshot](docs/img/grafana1.png?raw=true "Screenshot")

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
docker-compose build
```

## Deploy

Clone repo and set fronius url. After installation set correct meters indications in grafana variables.

### Run

```shell
docker-compose up -d
```

### Run / Update

```shell
docker-compose down --volumes
git pull
docker-compose build
docker-compose up -d
```

### Grafana dashboards

![Screenshot](docs/img/grafana1.png?raw=true "Screenshot")
![Screenshot](docs/img/grafana2.png?raw=true "Screenshot")
![Screenshot](docs/img/grafana3.png?raw=true "Screenshot")