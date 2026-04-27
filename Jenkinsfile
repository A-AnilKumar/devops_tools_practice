pipeline {

	agent any
	
	stages {
		stage('Checkout') {
			steps {
				echo "Code checked out from gitlab"
			}
			
		}

		stage('Install Dependencies') {
			steps {
				sh 'pip install -r requirements.txt'
			}
		}

		stage('Run Tests') {
			steps {
				sh 'pytest test/ -v --junitxml=results.xml'
			}
		}
		post {
			always {
				junit 'results.xml'
			}
		}

	}

	post {
		success { echo "Build passed!" }
		failure { echo "Build failed!" }
	}
}