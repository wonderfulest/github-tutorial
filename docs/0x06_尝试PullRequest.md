# Pull Request

## 什么是PR

首先需要知道，pull request不是Git核心特性。相反，是由使用的Git托管平台提供的，GitHub、GitLab、Bitbucket、AzureDevops以及其他平台都提供类似的内置功能。

## PR的好处

Pull request不仅改进了评审和反馈过程，还有助于跟踪和讨论代码变更。最后重要的一点是，pull request是向其他没有写访问权限的代码库贡献内容的理想方式。

## GitHub Flow

https://docs.github.com/zh/get-started/quickstart/github-flow

![GitHub-flow](https://muyids.oss-cn-beijing.aliyuncs.com/img/e725295ac764514088303ce8.png)

![Introdu](https://muyids.oss-cn-beijing.aliyuncs.com/img/GitHub-Flow.png)

### 创建分支

```shell
git checkout -b feature/xxx
git push --set-upstream origin feature/xxx
```
### 保护分支

#### 目的

GitHub设置保护分支的目的是为了保护重要分支免受意外或恶意更改的影响。当启用保护分支时，对分支的更改必须经过审查或满足其他指定的条件才能被合并到受保护的分支中。

保护分支可以帮助组织和团队确保代码的质量和稳定性，并防止非授权用户更改关键代码。此外，通过限制对保护分支的直接推送权限，也可以防止团队成员在未经他人审核的情况下推送代码，从而降低了潜在的错误和冲突。

保护分支功能可以与 GitHub 上的其他功能，如代码审查、CI/CD 流程集成等结合使用，进一步提高代码质量和安全性。

#### 操作

基本步骤：

1. 打开 GitHub 仓库并转到“Settings”选项卡。
2. 在侧边栏中选择“Branches”选项卡。
3. 在“Branch protection rules”下方单击“Add rule”。
4. 选择您要保护的分支。
5. 选择您要应用的保护规则，例如，要求每次推送都需要至少一个代码审查或需要CI/CD 流程成功运行。
6. 单击“Create”以创建保护分支规则。
![image-20230422170108908](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230422170108908.png)

现在，每当有人尝试推送到受保护的分支时，GitHub 将强制执行您选择的保护规则。如果推送未满足规则要求，则推送将被拒绝。

您还可以通过添加其他规则来进一步加强保护分支。例如，您可以设置分支的保护规则以仅允许特定的团队成员或个人对其进行更改，或者要求分支保持与主分支同步等等。

### 发起人

1. Fork 项目：进入项目页面，点击右上角的 Fork 按钮，将该项目复制到自己的账户下。

2. Clone 项目：在自己的账户下找到刚才 fork 的项目，点击 Clone or download 按钮，获取项目的仓库地址。使用 git clone 命令将该项目克隆到本地。

3. 创建分支：在本地项目的根目录下，使用 git branch 命令创建新的分支。比如，我们可以创建一个名为 feature 的分支来开发新功能。

   ```shell
   git branch feature
   git checkout feature
   ```
   也可以直接使用 fork出来的分支。

4. 修改代码：在新的分支上进行代码修改和提交。

   

5. 提交修改：使用 git add 命令将修改的文件添加到本地仓库，使用 git commit 命令提交修改信息。

   ```shell
   git add .
   git commit -m "提交信息"
   ```
6. 推送分支：使用 git push 命令将修改推送到自己的 GitHub 账户下。

   ```
   git push origin feature
   ```

7. 发起 Pull Request：在自己的 GitHub 账户下找到刚才推送的分支，点击 New pull request 按钮，进入发起 PR 的页面。选择 base 分支（一般是原项目的主分支，如 master 或 main），将 compare 分支设置为刚才推送的分支（如 feature），填写 PR 的标题和描述信息，最后点击 Create pull request 按钮。

   

   ![image-20230422174736505](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230422174736505.png)

   

   ![image-20230422174747044](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230422174747044.png)

   

   注意：在填写 PR 描述信息时，最好简要说明自己所做的修改，以及修改的原因和意义，以便项目维护者审核和合并。

8. 等待审核：等待项目维护者审核并处理 PR，如果有需要，可以在 PR 页面中进行讨论和修改。如果 PR 被接受并合并，恭喜你成为该项目的贡献者之一！

### 审核

如果你是审核者，需要审核并接受 Pull Request（PR）的步骤如下：

#### 查看 PR

进入 PR 页面，查看提交的代码和描述信息，了解修改的内容和意义。

![image-20230422175320066](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230422175320066.png)

#### 检查代码

下载并测试 PR 分支的代码，确保修改没有引入新的 bug 或破坏原有的功能。

#### 进行审查

点击进入PR 中的commits，进行Review：

对修改的代码进行审查，查看代码风格、命名规范、注释、可读性等方面是否符合项目要求和最佳实践。

![image-20230422175615038](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230422175615038.png)

review有三种操作进行选择：

- 仅评论

- 接受 PR 

- 请求修改

  > 这会要求反馈在合并前必须解决
  >
  > 当请求合并的commits需要修改时，可以使用这种方式进行沟通

#### 提交评论

对修改进行评价，并提出可能的问题或改进意见。如果有需要，可以在 PR 页面中进行讨论和交流，以便更好地理解和解决问题。

#### 接受 PR

如果对修改没有问题或者问题已经解决，可以点击 Merge 按钮，将修改合并到原项目的主分支中。同时，可以选择删除该 PR 分支或者保留它作为记录。

#### 完成 PR

PR 审核完成后，需要及时关闭该 PR，以便维护者和贡献者知道该 PR 的状态和结果。如果 PR 被接受并合并，可以在 PR 描述中说明合并的原因和意义，以便其他人了解和参考。

![celebrate](https://muyids.oss-cn-beijing.aliyuncs.com/img/68747470733a2f2f6f63746f6465782e6769746875622e636f6d2f696d616765732f636f6c6c61626f636174732e6a7067.jpeg)

## 参考

- [pull-requests](https://docs.github.com/zh/pull-requests/)
- [github-flow quickstart ](https://docs.github.com/zh/get-started/quickstart/github-flow)
