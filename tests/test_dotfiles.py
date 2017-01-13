import os

def test_dotfiles_dir(File, User):
    dotfiles = File( os.path.join( User().home, ".dotfiles" ) )
    assert dotfiles.exists
    assert dotfiles.is_directory

def test_alias(File, User):
    bashrc = File( os.path.join( User().home, "/home/vagrant/.alias" ) )
    assert bashrc.exists
    assert bashrc.is_file
