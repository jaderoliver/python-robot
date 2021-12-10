pipeline {
    /* specify nodes for executing */
    agent any
 
    stages {
        /* checkout repo */
        stage('Checkout SCM') {
            steps {
                checkout changelog: false, poll: false, scm: [$class: 'GitSCM', branches: [[name: '*/master']], 
                extensions: [], userRemoteConfigs: [[credentialsId: 'github_user_pass', 
                url: 'https://github.com/jaderoliver/jenkins_pipeline_examples.git/']]]
            }
        }
         stage('Do the deployment') {
            steps {
                echo ">> Run deploy applications "
                script{
                    sh 'ls -lhart'
                    sh 'pwd'
                    echo " "
                    echo BRANCH_NAME
                }
            }
        }
    }
 
    /* Cleanup workspace */
    post {
       always {
           deleteDir()
       }
   }
}
