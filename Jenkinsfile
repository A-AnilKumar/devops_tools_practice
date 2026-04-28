pipeline {

	agent {
		docker {
			image 'python:3.11-slim'
			args '--user root'
		}
	}

	environment {
		PYTHONDONTWRITEBYTECODE = '1'
		PYTHONUNBUFFERED = '1'
		PYTHONPATH = "${WORKSPACE}" 
	}
	
	stages {
		stage('Checkout') {
			steps {
				echo "Running on : ${env.NODE_MAME}"
				echo "Branch : ${env.BRANCH_NAME}"
				echo "Build #: ${env.BUILD_NUMBER}"
			}
		}

		stage('Install Dependencies') {
			steps {
				sh 'pip install -r requirements.txt --quiet'
			}
		}

		stage('Run Tests') {
			steps {
				sh '''
					pytest tests/ -v \
					--junitxml=results.xml \
					--cov=app \
					--cov-report=xml:coverage.xml
				'''
			}

			post {
				always {
					junit 'results.xml'
				}
			}
		}

	}

	post {
        success { echo "✅ Build #${env.BUILD_NUMBER} passed!" }
        failure { echo "❌ Build #${env.BUILD_NUMBER} failed!" }
    }
}
