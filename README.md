# Copy shell environment to remote machine with Ansible

These playbooks are for copying my default shell environment to remote machines and VMs.

## Tests

To run a test that checks if the infrastructure was deployed successfully, you need to install the Python modules `testinfra` and `paramiko`. Then you can run

    testinfra --hosts=user@hostname test_dotfiles.py
