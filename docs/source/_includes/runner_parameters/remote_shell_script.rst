.. NOTE: This file has been generated automatically, don't manually edit it

* ``username`` (string) - Username used to log-in. If not provided, default username from config is used.
* ``private_key`` (string) - Private key used to log in. If not provided, private key from the config file is used.
* ``env`` (object) - Environment variables which will be available to the script(e.g. key1=val1,key2=val2)
* ``sudo`` (boolean) - The remote command will be executed with sudo.
* ``kwarg_op`` (string) - Operator to use in front of keyword args i.e. "--" or "-".
* ``password`` (string) - Password used to log in. If not provided, private key from the config file is used.
* ``parallel`` (boolean) - Default to parallel execution.
* ``port`` (integer) - SSH port. Note: This parameter is used only in ParamikoSSHRunner.
* ``hosts`` (string) - A comma delimited string of a list of hosts where the remote command will be executed.
* ``timeout`` (integer) - Action timeout in seconds. Action will get killed if it doesn't finish in timeout seconds.
* ``cwd`` (string) - Working directory where the script will be executed in.
* ``dir`` (string) - The working directory where the script will be copied to on the remote host.