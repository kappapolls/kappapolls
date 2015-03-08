from fabric.api import *
from fabsettings import hosts, key_location, shell, user

#env.hosts = hosts
#env.key_filename = key_location
#env.shell = shell
#env.user = user
env.use_ssh_config = True
env.hosts = ['kappapolls']

def tests():
    with prefix('workon kappapolls'):
        local('manage.py test')

def install_required_packages():
    required_packages = ['virtualenvwrapper',
                        'git',
                        'python-dev',
                        'postgresql',
                        'postgresql-contrib',
                        'libpq-dev',
                        'supervisor',
                        ]

    package_string = ' '.join(required_packages)
    sudo('apt-get update && apt-get -y install %s' % package_string)

def make_directories():
    with settings(warn_only=True):
        run('mkdir kappa')

    with cd('kappa'):
        run('git clone https://kappapolls@github.com/kappapolls/kappapolls.git')

def deploy(branch='master', remote='gh'):
    with cd('kappa/kappapolls'):
        run('git fetch %s' % remote)
        run('git checkout %s' % branch)
        run('git reset --hard %s/%s' % (remote, branch))
        with prefix("source /usr/share/virtualenvwrapper/virtualenvwrapper.sh; workon kappapolls"):
            run('./manage.py migrate')
            run('./manage.py collectstatic --noinput')
        sudo('service nginx restart')
        sudo('supervisorctl stop kappapolls')
        sudo('supervisorctl start kappapolls')

def remote_uname():
    run('uname -a')
