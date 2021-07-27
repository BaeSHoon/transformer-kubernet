pipeline {
  agent any
  stages {
    stage("lint") {
      agent {
        dockerfile {
          filename 'jenkins/Dockerfile.test'
          reuseNode true
        }
      }
      when {
        // expression { env.BRANCH_NAME =~ "(.*)-patch-*" }
        // expression { env.BRANCH_NAME =~ "PR-*" }
        changeset pattern: "*.py"
      }
      steps {
        sh "sh jenkins/launch.sh lint bandit"
      }
    }
  }
}
