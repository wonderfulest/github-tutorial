# [GitHub CLI](https://cli.github.com/)

GitHub CLI 是一个命令行工具，可将拉取请求、议题、GitHub Actions 和其他 GitHub 功能引入终端，使您可以在一个地方完成所有工作。

GitHub CLI 是用于从计算机的命令行使用 GitHub 的开源工具。 从命令行操作时，您可以使用 GitHub CLI 来节省时间并避免切换上下文。

GitHub CLI 包括 GitHub 功能，例如：

- 查看、创建、克隆和复刻仓库
- 创建、关闭、编辑和查看议题和拉取请求
- 审查、差异和合并拉取请求
- 运行、查看和列出工作流程
- 创建、列出、查看和删除版本
- 创建、编辑、列出、查看和删除 Gist
- 列出、创建、删除并连接到 codespace

## 授权

通过 环境变量GITHUB_TOKEN 授权；

### 获取 GITHUB_TOKEN：

要获取 Github Token，请按照以下步骤进行操作：

1. 登录到 Github 帐户，并转到“Settings”（设置）。
2. 转到“Developer settings”（开发者设置）选项卡，然后单击“Personal access tokens”（个人访问令牌）。
3. 单击“Generate new token”（生成新令牌）按钮。
4. 在“Token description”（令牌说明）中输入一个描述，以便您能够轻松记住该令牌的用途。
5. 选择所需的权限，例如读取库、管理存储库等。
6. 单击“Generate token”（生成令牌）按钮。
7. 复制生成的令牌并妥善保存。请注意，您只会看到该令牌一次。

请务必妥善保管您的令牌，并不要将其分享给他人，以免出现安全问题。

### 配置环境变量：

```
 export GITHUB_TOKEN=xxxx
```

### 可以使用 gh 命令进行操作了

```
gh --help
```

## 管理仓库

```shell
# 搜索感兴趣的仓库
gh s        

# fork 仓库
gh repo fork xxx
```

## 管理issue

```shell
# 查看问题列表
gh issue list 

# 在浏览器中打开
gh issue view 3 --web
# 编辑问题
gh issue edit 3         
```

