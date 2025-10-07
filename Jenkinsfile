pipeline {
    agent any

    environment {
        EC2_USER = 'ubuntu'
        EC2_HOST = '18.215.179.42'           // Your EC2 public IP
      //  SSH_KEY = credentials('github-token-forec2') // Jenkins credential ID
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', credentialsId: 'github-token-forec2', url: 'https://github.com/Shiny-Jenita/first_project.git'
                echo 'Repo cloned!'
            }
        }

       stage('Deploy to EC2') {
    steps {
        sshagent(['ec2-ssh-key']) {
            sh """
            ssh -o StrictHostKeyChecking=no ubuntu@18.215.179.42 '
                cd /home/ubuntu/app || mkdir -p /home/ubuntu/app
                cd /home/ubuntu/app
                git pull || git clone https://github.com/Shiny-Jenita/first_project.git .
                # Add app start commands
            '
            """
                      }
            }
          }

    }
}

