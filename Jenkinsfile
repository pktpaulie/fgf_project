pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    // Pull the Docker image
                    docker.image('nekiwanuka/fgf-app-drepo').pull()
                }
            }
        }

        // stage('Test') {
        //     steps {
        //         script {
        //             // Run tests for your Django application within the Docker container
        //             docker.image('nekiwanuka/fgf-app-drepo').inside('-p 8000:8000') {
        //                 sh 'python manage.py test'
        //             }
        //         }
        //     }
        // }

        stage('Deploy') {
            steps {
                script {
                    // Run the Docker container
                    docker.image('nekiwanuka/fgf-app-drepo').run('-p 8000:8000 -d')
                }
            }
        }
    }
}
