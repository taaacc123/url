pipeline 
{
	//agent { docker { image 'maven:3.6.3'} }
	//agent { docker { image 'girireddychinnu/hello-world-python:0.0.4.RELEASE'}}
	agent { dockerfile true }
	environment {
		dockerHome = tool 'myDocker'
		//mavenHome = tool 'myMaven'
		//PATH = "$dockerHome/bin:$mavenHome/bin:$PATH"
		PATH = "$dockerHome/bin:$PATH"
		//add docker bin anf maven bi n to path
	}
	stages {
		// stage('Checkout') {
		// 	steps {
		// 		sh 'mvn --version'
		// 		sh 'docker --version'
        //        	echo "Build"
		// 		echo "$PATH"
		// 		echo "BUILD_NUMBER - $env.BUILD_NUMBER"
		// 		echo "BUILD_ID - $env.BUILD_ID"
		// 		echo "JOB_NAME - $env.JOB_NAME"
		// 		echo "BUILD_TAG - $env.BUILD_TAG"
		// 		echo "BUILD_URL - $env.BUILD_URL"
				
		// 	}
		// }
		// stage('Compile') {
		// 	steps {
		// 		sh "mvn clean compile"
		// 	}
		// }
		// stage('Test') {
		// 	steps {
		// 		sh "mvn test"
		// 	}
		// }
		// stage('Integration Test') {
		// 	steps {
		// 		sh "mvn failsafe:integration-test failsafe:verify"
		// 	}
		// }
		// stage('Package') {
		// 	steps {
		// 		sh "mvn package -DskipTests"
		// 	}
		// }
		stage('Build Docker Image') {
			steps {
				//"docker build -t girireddychinnu/currency-exchange-devops:$env.BUILD_TAG"
				script {
					dockerImage = docker.build("girireddychinnu/hello-world-python:${env.BUILD_TAG}")
				}
			}
		}
		stage('Push docker Image') {
			steps {
				script {
					docker.withRegistry('', 'docker-creds'){
					dockerImage.push();
					dockerImage.push('latest');
					dockerImage.run();
					}
				}
				sh "docker run -d \
            --name ${IMAGE_NAME} \
            --publish 5000:5000 \
            ${IMAGE_NAME}:${BUILD_ID}"
			}
		}
	} 
	post {
		always {
			echo "im always"
		}
		success {
			echo "im success"
		}
		failure {
			echo "im failed"
		}
	}
}
	

