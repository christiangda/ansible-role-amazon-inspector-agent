import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_amazon_inspector_agent_dependencies_are_installed(host):
    os = host.system_info.distribution.lower()
    rl = host.system_info.release

    redhat_6 = ('libcurl', 'libgcc', 'libstdc++',
                'openssl', 'libpcap', 'gnupg2')

    redhat_7 = ('libcurl', 'libgcc', 'libstdc++', 'openssl',
                'openssl-libs', 'libpcap', 'gnupg2')

    debian_8 = ('libcurl3', 'libgcc1', 'libc6', 'libstdc++6',
                'libssl1.0.0', 'libpcap0.8', 'gnupg')

    debian_9 = ('libcurl4-openssl-dev', 'libcurl3', 'libgcc1', 'libc6', 'libstdc++6',
                'libssl1.0.2', 'libpcap0.8', 'gnupg')

    ubuntu_14 = ('libcurl3', 'libgcc1', 'libc6', 'libstdc++6',
                 'libssl1.0.0', 'libpcap0.8', 'gnupg')

    ubuntu_18 = ('libcurl4', 'libgcc1', 'libc6', 'libstdc++6',
                 'libssl1.0.0', 'libpcap0.8', 'gnupg')

    if os == 'centos':
        key = 'redhat' + '_' + rl.split('.')[0]
    elif (os == 'amzn') and (rl.split('.')[0] == '1'):
        key = 'redhat_6'
    elif (os == 'amzn') and (rl.split('.')[0] == '2'):
        key = 'redhat_7'
    elif (os == 'ubuntu') and (rl.split('.')[0] == '16'):
        key = os + '_' + '14'
    else:
        key = os + '_' + rl.split('.')[0]

    for p in eval(key):
        pkg = host.package(p)
        assert pkg.is_installed
