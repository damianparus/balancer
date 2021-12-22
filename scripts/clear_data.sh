exit

find ./influxdb/data/ -not -name '.gitignore' -mindepth 1 -maxdepth 1 | xargs -I{} rm -r {}
find ./grafana/data/ -not -name '.gitignore' -mindepth 1 -maxdepth 1 | xargs -I{} rm -r {}

date
echo "Data cleared"
