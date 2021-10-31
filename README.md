# docker-compose uWSGI nginx flask
Note that this was tested on CentOS 7

### Usage

```
sudo yum install docker
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
# if want to continue with root
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

### Run

```bash
sudo docker-compose build
sudo docker-compose up
```

refer to http://127.0.0.1