node('UBUNTU') {
  echo 'Hello World'
  checkout scm
  docker.image('lasote/conangcc49').inside('-d') {
    stage('apt-update') {
      sh 'sudo gpg --keyserver keyserver.ubuntu.com --recv-key 5BB92C09DB82666C'
      sh 'sudo gpg -a --export 5BB92C09DB82666C | sudo apt-key add -'
      sh 'sudo mv /etc/apt/sources.list /etc/apt/sources.list.bk'
      sh 'sudo mv sources.list.trusty /etc/apt/sources.list'
      sh 'sudo apt-get update'
    }
    stage('git') {
      sh 'git config --global user.email "chinadaihongjun@gmail.com"'
      sh 'git config --global user.name "cppbitman"'
      sh 'rm -rf cerbero;mkdir cerbero;'
      dir('cerbero') {
        git branch: '1.14', url: 'https://github.com/cppbitman/cerbero.git'
        sh './cerbero-uninstalled -c config/linux.config bootstrap'
        sh './cerbero-uninstalled -c config/linux.config package gstreamer-1.0'
        sh 'pwd; ls -a;'
      }
    }
  }
}
