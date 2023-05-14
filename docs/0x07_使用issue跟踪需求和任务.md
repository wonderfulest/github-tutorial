# 使用 GitHub Issues 来跟踪需求和任务

## bug追踪系统

管理Issue的系统统称为 BTS（bug追踪系统）

应用场景：

- 发现bug并报告
- 有事向作者询问、探讨
- 事先列出今后准备实施的任务

## 什么是github的问题追踪？

GitHub提供了问题追踪工具，可以帮助你管理和解决项目中的问题。确保创建清晰、具体和易于理解的问题，以便其他开发人员能够快速理解和解决问题。

![image-20230410141653172](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230410141653172.png)

启用issue跟踪需求和任务

## 使用 GitHub Issues 的一些基本步骤

1. 打开 GitHub 上的项目，并转到“Issues”选项卡。
2. 单击“New issue”按钮创建新的问题。
3. 输入问题的标题和详细描述。尽可能详细地描述问题，包括重现步骤、期望行为和实际行为。
4. 标记问题。您可以使用标签、里程碑和分配来帮助组织问题。例如，您可以将问题标记为“bug”、“enhancement”或“help wanted”。
5. 提交问题并等待反馈。其他人可以在问题下面发表评论，您也可以与他们进行互动以更好地了解问题。
6. 解决问题。一旦您解决了问题，可以将其关闭并在描述中提供详细信息。如果您需要在未来再次打开问题，可以将其标记为“reopen”。
7. 跟踪问题。您可以使用筛选器和搜索来查找和跟踪问题，以便更好地组织和管理它们。

总之，GitHub Issues 是一种有助于团队管理项目的问题跟踪工具，通过标记、筛选和搜索等功能，使得团队成员可以更好地了解和处理项目中的问题。

### issue Labels

标签的划分规则一般有下面几种：

- 进度：todo、in progress、done、in review
- 功能：bug、discussion、docs、improvement
- 版本：1.x、2.3

### Milestones

管理项目版本

![image-20230410143450185](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230410143450185.png)

### 模板

settings > Features > Issues  > Set up templates

![image-20230410153610989](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230410153610989.png)

设置模板成功后 会在仓库 目录.github/ISSUE_TEMPLATE下创建模板文件：

![image-20230410153503366](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230410153503366.png)

## 用GitHub Projects看板管理 issue 和 PR

GitHub Projects 是一个强大的项目管理工具，它可以帮助您跟踪和组织问题和 pull request (PR)。以下是如何使用 GitHub Projects 的一些基本步骤：

1. 打开 GitHub 上的项目，并转到“Projects”选项卡。
2. 单击“New project”按钮创建一个新项目。可以选择三种类型的项目：“kanban”、“automated kanban”和“scrum”。
3. 创建一些列。在“kanban”项目类型中，您可以创建多个列，例如“Backlog”、“In progress”、“Review”和“Done”等。可以根据您的项目需求添加自定义列。
4. 将问题和PR添加到项目中。在每个列中，您可以通过拖放操作将问题和PR添加到适当的位置。您可以在“Add cards”对话框中选择要添加的问题和PR，或者您可以通过拖动现有的问题和PR来将它们添加到列中。
5. 组织和管理问题和PR。您可以使用“Projects”中的看板来跟踪问题和PR的状态。例如，您可以将问题和PR从“Backlog”列移到“In progress”列，并将其分配给特定的开发人员。
6. 查看统计信息和进度。您可以使用“Projects”中的统计信息和进度功能来查看项目的进展情况。例如，您可以查看每个列中的问题和PR的数量，或者查看在特定时间段内解决了多少问题和PR。
总之，GitHub Projects 是一个强大的项目管理工具，可以帮助您跟踪和组织问题和PR，并提供有关项目进展情况的统计信息和进度。通过使用看板功能，您可以更轻松地管理和协调您的团队成员的工作。

## 如何使用 commit关闭issue

您可以使用 GitHub 的特殊关键字将提交与问题相关联并自动关闭问题。以下是如何使用 commit 关闭 issue 的基本步骤：

1. 打开要与问题相关联的分支或拉取请求。
2. 在提交消息中包含一个特殊的关键字，该关键字告诉 GitHub 关闭相关的问题。例如，如果要关闭 issue #123，可以在提交消息中包含以下内容：
```shell
Fixed #123, issue resolved
```

在提交消息中包含 "Fixed #123" 就是告诉 GitHub 关联 issue #123，并且这个提交修复了它。

1. 将提交推送到您的仓库并等待 GitHub 自动关闭相关的问题。如果您在提交消息中正确使用了特殊关键字，GitHub 将自动将问题关闭并将提交与其相关联。

注意，必须在提交消息中使用精确的关键字才能关闭相关的问题。例如，使用 "Close #123" 或 "Fixed #123" 而不是 "Closes #123"，否则 GitHub 将不会自动关闭问题。

总之，通过在提交消息中包含特殊的关键字，您可以将提交与问题相关联并自动关闭问题。这是一个很方便的功能，可以帮助您更好地组织和管理您的工作流程。

## 高级搜索 - 问题和PR

https://docs.github.com/zh/search-github/searching-on-github/searching-issues-and-pull-requests

## 参考

- https://docs.github.com/en/issues
