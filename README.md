# Ansible Role: christiangda.amazon_inspector_agent

[![Build Status](https://travis-ci.org/christiangda/ansible-role-amazon-inspector-agent.svg?branch=master)](https://travis-ci.org/christiangda/ansible-role-amazon-inspector-agent)
[![Ansible Role](https://img.shields.io/ansible/role/40095.svg)](https://galaxy.ansible.com/christiangda/amazon_inspector_agent)

This role [Install AWS Inspector Agent](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_introduction.html)

**Features:**
* Downloads and installs AWS Inspector Agent from AWS distribution package
* Rotate the Agent Log file

## Requirements

This role work on RedHat, CentOS, Amazon Linux, Debian and Ubuntu distributions

* RedHat
  * 6
  * 7
* CentOS
  * 6
  * 7
* Amazon Linux
  * 1
  * 2
* Ubuntu
  * 14.*
  * 16.*
  * 18.*
* Debian
  * jessie
  * stretch

To see the compatibility matrix of Python vs. Ansible see the project [Travis-CI build matrix](https://travis-ci.org/christiangda/ansible-role-amazon-inspector-agent)

## Role Variables

```yaml
# posible values:
# - true
# - false
# default value: true
# notes:
# * set value to false when you don't want to enable auto update the agent
# Reference: https://docs.aws.amazon.com/inspector/latest/userguide/inspector_agents.html#agent-updates
ia_auto_update: true
```

```yaml
# posible values:
# - https://docs.aws.amazon.com/inspector/latest/userguide/inspector_agents-on-linux.html
# default value: ""
ia_http_proxy: ""
```

```yaml
# posible values:
# - https://docs.aws.amazon.com/inspector/latest/userguide/inspector_agents-on-linux.html
# default value: ""
ia_https_proxy: ""
```

```yaml
# posible values:
# - https://docs.aws.amazon.com/inspector/latest/userguide/inspector_agents-on-linux.html
# default value: "169.254.169.254"
# notes:
# * Always disable proxy for aws metadata ip (169.254.169.254)
ia_no_proxy: "169.254.169.254"
```
## Dependencies

None

## Example Playbook

### RedHat/CentOS, Ubuntu and Debian

**Using default vars values**

```yaml
- hosts: servers
    gather_facts: True
    roles:
    - role: christiangda.amazon_inspector_agent
```

**Disabling auto update and using proxy configuration**

```yaml
- hosts: servers
    gather_facts: True
    roles:
    - role: christiangda.amazon_inspector_agent
        vars:
            ia_auto_update: false
            ia_http_proxy: "192.168.2.253:3128"
            ia_https_proxy: "192.168.2.253:3128"
            ia_no_proxy: "169.254.169.254,192.168.2.1"
```

###  Amazon Linux 1/2 (my-playbook.yml)

```yaml
- hosts: all
    gather_facts: True
    become: true
    become_user: root
    become_method: sudo
    remote_user: ec2-user
    roles:
    - role: christiangda.amazon_inspector_agent
```

**Inventory file sample (inventory)**

```ini
[all]
10.14.x.y
10.14.v.z

[amazon-1]
10.14.x.y

[amazon-2]
10.14.v.z
```

**How to used it**

```bash
ansible-playbook my-playbook.yml \
    --inventory inventory \
    --private-key [~/location of my key.pem] \
    --become \
    --become-user=ec2-user \
    --user ec2-user
```

## Development / Contributing

This role is tested using [Molecule](https://molecule.readthedocs.io/en/latest/) and was developed using
[Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

**Prepare your environment**

**Python 3**

```bash
mkdir ansible-roles
cd ansible-roles/

python3 -m venv venv
source venv/bin/activate
pip install pip --upgrade
pip install ansible
pip install molecule">=2.22rc1"
pip install selinux
pip install docker
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install flake8
```

**Python 2.7**

Dependencies

```bash
sudo dnf install redhat-rpm-config
sudo dnf install python-devel
sudo dnf install libselinux-python
```

```bash
mkdir ansible-roles
cd ansible-roles/

python2.7 -m virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install ansible
pip install molecule">=2.22rc1"
pip install selinux
pip install docker
pip install pytest
pip install pytest-mock
pip install pylint
pip install rope
pip install autopep8
pip install yamllint
pip install flake8
```

**Clone the role repository and create symbolic link**

```bash
git clone https://github.com/christiangda/ansible-role-amazon-inspector-agent.git
ln -s ansible-role-amazon-inspector-agent christiangda.amazon_inspector_agent
cd christiangda.amazon_inspector_agent
```

**Execute the test**

Using docker in local

```bash
molecule test [--scenario-name default]
```

Using vagrant in local

```bash
molecule create --scenario-name vagrant
molecule converge --scenario-name vagrant
molecule verify --scenario-name vagrant
```

or

```bash
molecule test --scenario-name vagrant
```

**Additionally if you want to test using VMs, I have a very nice [ansible-playground project](https://github.com/christiangda/ansible-playground) that use Vagrant and VirtualBox, try it!.**

## License

This module is released under the GNU General Public License Version 3:

* [http://www.gnu.org/licenses/gpl-3.0-standalone.html](http://www.gnu.org/licenses/gpl-3.0-standalone.html)

## Author Information

* [Christian González Di Antonio](https://github.com/christiangda)
