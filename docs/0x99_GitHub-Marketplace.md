# GitHub Marketplace

GitHub Marketplace 是一个集成市场，提供了各种应用程序、工具和服务，可以轻松地集成到您的 GitHub 工作流程中，以提高效率和质量。

以下是在 GitHub Marketplace 上安装集成的步骤：

1. 打开 GitHub 的官方网站：https://github.com/
2. 点击页面右上角的“Marketplace”按钮。
3. 在市场中，您可以浏览和搜索各种应用程序和服务，例如 CI/CD 工具、代码质量分析、通知和警报等等。您可以根据您的需求和偏好进行筛选和排序。
4. 选择一个应用程序或服务，并单击其图标以了解更多详细信息。您可以查看其功能、价格和评级，并查看其他用户的评价和评论。
5. 如果您决定安装该应用程序或服务，则可以单击“Get it free”或“Buy it”按钮。您需要授权该应用程序或服务访问您的 GitHub 账户，并选择一个适当的访问范围和权限。
6. 安装完成后，您可以返回 GitHub 工作流程，并将该应用程序或服务集成到您的工作流程中。例如，您可以在 GitHub Actions 中使用该应用程序或服务的预定义操作，或者在您的代码中使用其 API 或 SDK。
使用 GitHub Marketplace 安装集成可以大大提高您的开发效率和质量，同时也可以加速您的工作流程和改进您的团队协作。

## 配置 circleci

选择项目

![image-20230423101746463](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230423101746463.png)

选择template模板进行配置

<img src="/Users/mac/Library/Application Support/typora-user-images/image-20230423101815980.png" alt="image-20230423101815980" style="zoom:50%;" />

生成的模板内容如下：

```yml
# Use the latest 2.1 version of CircleCI pipeline process engine.
# See: https://circleci.com/docs/2.0/configuration-reference
version: 2.1
# Orbs are reusable packages of CircleCI configuration that you may share across projects, enabling you to create encapsulated, parameterized commands, jobs, and executors that can be used across multiple projects.
# See: https://circleci.com/docs/2.0/orb-intro/
orbs:
  # The python orb contains a set of prepackaged CircleCI configuration you can use repeatedly in your configuration files
  # Orb commands and jobs help you with common scripting around a language/tool
  # so you dont have to copy and paste it everywhere.
  # See the orb documentation here: https://circleci.com/developer/orbs/orb/circleci/python
  python: circleci/python@1.5.0
# Define a job to be invoked later in a workflow.
# See: https://circleci.com/docs/2.0/configuration-reference/#jobs
jobs:
  build-and-test: # This is the name of the job, feel free to change it to better match what you're trying to do!
    # These next lines defines a Docker executors: https://circleci.com/docs/2.0/executor-types/
    # You can specify an image from Dockerhub or use one of the convenience images from CircleCI's Developer Hub
    # A list of available CircleCI Docker convenience images are available here: https://circleci.com/developer/images/image/cimg/python
    # The executor is the environment in which the steps below will be executed - below will use a python 3.10.2 container
    # Change the version below to your required version of python
    docker:
      - image: cimg/python:3.10.2
    # Checkout the code as the first step. This is a dedicated CircleCI step.
    # The python orb's install-packages step will install the dependencies from a Pipfile via Pipenv by default.
    # Here we're making sure we use just use the system-wide pip. By default it uses the project root's requirements.txt.
    # Then run your tests!
    # CircleCI will report the results back to your VCS provider.
    steps:
      - checkout
      - python/install-packages:
          pkg-manager: pip
          # app-dir: ~/project/package-directory/  # If your requirements.txt isn't in the root directory.
          # pip-dependency-file: test-requirements.txt  # if you have a different name for your requirements file, maybe one that combines your runtime and test requirements.
      - run:
          name: Run tests
          # This assumes pytest is installed via the install-package step above
          command: pytest
# Invoke jobs via workflows
# See: https://circleci.com/docs/2.0/configuration-reference/#workflows
workflows:
  sample: # This is the name of the workflow, feel free to change it to better match your workflow.
    # Inside the workflow, you define the jobs you want to run.
    jobs:
      - build-and-test

```

编辑代码推送到新创建的 circleci-project-setup 分支，ci成功

