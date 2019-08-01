def ORG = "mayadataio"
pipeline {
    agent any
    stages {
        stage('Updating Version') {
            steps {
            echo "Workspace dir is ${pwd()}"  
            script {
               if (env.BRANCH_NAME == 'master'){
                  BN = sh(
                    returnStdout: true,
                    script: "./version_override ${REPO}"
                  ).trim()
                echo "${BN}"
                echo "This image will be tagged with ${BN}" 
               }else  {
                echo "This is not a master branch, tagging skipped!!" 
                }           
            }        
          }
        }
        stage('Build') {
            steps {
	        script {
	            GIT_SHA = sh(
		                 returnStdout: true,
				 script: "git log -n 1 --pretty=format:'%h'"
				).trim()
                TAG = sh (
                        returnStdout: true,
                        script: 'git tag --points-at HEAD | awk NF'
                       ).trim()
                      sh "echo ${TAG}"    

		    sh 'env > env.txt'
		    for (String i : readFile('env.txt').split("\r?\n")) {
		        println i
		    }

		    echo "Checked out branch: ${env.BRANCH_NAME}"

                    sh "docker build -t ${ORG}/${REPO}:${GIT_SHA}"
	         }
        }
    }
        stage('Push to DockerHub') {
            steps {
		    script {
		        echo "Checked out build number: ${env.BUILD_NUMBER}"
		        withCredentials([usernamePassword( credentialsId: 'f4e122bb-f119-42e0-9a2e-577b2cedfbd6', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                            if ( env.BRANCH_NAME == 'master') {
                                sh "docker login  -u${USERNAME} -p${PASSWORD}"
                                sh "docker push  ${ORG}/${REPO}:${GIT_SHA}"
		                echo "Pushing the image with the tag..."
				DOCKER_IMAGE.push()
                            } else {
			        echo "WARNING: Not pushing image"
                            }
		        }
		    }
	    }
    }

}
}
