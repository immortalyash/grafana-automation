# ![Ansible](https://upload.wikimedia.org/wikipedia/commons/0/05/Ansible_Logo.png) Automation for alpha using Ansible

### Description
___
It's for automated server configuration and monitoring system for alpha using Ansible. Currently works for adding monitoring system over it using carbon, graphite, collectd and grafana which is served over SSL managed by Let's Encrypt with auto renewable cron.

### File Tree
___
```
├── ansible.cfg                 # contains ansible configurations at lowest level
├── inventory                   # contains information on blocks of server
├── host.key                    # key to be used for host server
├── README.md
└── grafana                 	# playbook for downloading, installing, configuring monitoring system
    ├── defaults                # global variables dir
    │   └── main.yml
    ├── handlers                # global callbacks
    │   └── main.yml
    ├── install_monitoring.yml
    ├── tasks                   # various tasks to be performed
    │   ├── carbon.yml
    │   ├── cleanup.yml
    │   ├── collectd.yml
    │   ├── configure.yml
    │   ├── database.yml
    │   ├── essentials.yml
    │   ├── fetch_graphite.yml
    │   ├── grafana.yml
    │   ├── graphite.yml
    │   ├── letsencrypt_montoring.yml
    │   ├── letsencrypt.yml
    │   ├── monitoring.yml
    │   ├── virtualenv_graphite.yml
    │   └── whisper.yml
    ├── templates               # global templates for copying to various servers for config/install using Jinja2 templating
    │   ├── grafana_4.2.0_armhf.deb
    │   ├── graphite            # config for monitoring
    │   │   ├── carbon-cache
    │   │   ├── conf
    │   │   │   ├── carbon.conf
    │   │   │   ├── gunicorn_monitoring
    │   │   │   ├── nginx.conf
    │   │   │   ├── storage-aggregation.conf
    │   │   │   ├── storage-schemas.conf
    │   │   │   └── supervisor.conf
    │   │   └── webapp
    │   │       ├── graphite.wsgi
    │   │       └── local_settings.py
```

### Usage
___
Running cli commands to particular blocks
```
ansible <block_name> -m <command> -a <args>
```


Installing web monitoring system on production server with SSL
```
ansible-playbook grafana/install_monitoring.yml
```

### References
___
* **Django Docs-** https://docs.djangoproject.com/en/1.10/
* **Ansible Docs-** http://docs.ansible.com/ansible/intro.html
* **Graphite Docs-** http://graphite.readthedocs.io/en/latest/
* **Collectd Docs-** https://collectd.org/documentation/manpages/collectd.conf.5.shtml
* **Collectd Wiki-** https://collectd.org/wiki/index.php/Main_Page
* **Grafana Docs-** http://docs.grafana.org/
* **Let's Encrypt Docs-** https://letsencrypt.org/docs/
