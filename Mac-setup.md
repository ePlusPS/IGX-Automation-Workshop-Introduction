# IGX-automation-workshop-foundation

## Mac specific workstation Setup

1. Installing Homebrew  

   * Install XCode dev tools or check they are installed  
   > xcode-select --install

   * If you get the following, it's already installed  
   > xcode-select: error: command line tools are already installed, use "Software Update" to install updates

   * Install homebrew  
   > /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

   * Check the install  
   > brew -v
   > \# example output  
   > Homebrew 1.8.2  

   * Install pyenv  
   > brew install pyenv

   * Install Cask
   > brew tap caskroom/cask

2. Install non system version of Python

   * Install python2  
   > brew install python@2

   * Install python3  
   > brew install python  

   * Install pyenv  
   > brew install pyenv  
   > brew install openssl readline sqlite3 xz zlib  
   > brew install pyenv-virtualenv  
   > pip install virtualenv

   * Add pyenv to the shell  
   > echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile  


Update....
https://medium.com/@briantorresgil/definitive-guide-to-python-on-mac-osx-65acd8d969d0  

Brian says dont use virtualenv but we need a consistent environment for both Win and Mac users.
