# 一台mac使用两个github账号

## 为两个账号生成公钥和私钥

```shell
>  ls -al ~/.ssh/
-rw-------  1 mac  staff   2.5K Oct 11  2022 id_rsa
-rw-r--r--  1 mac  staff   571B Oct 11  2022 id_rsa.pub
-rw-------  1 mac  staff   2.5K Apr 22 16:14 id_rsa_wond
-rw-r--r--  1 mac  staff   570B Apr 22 16:14 id_rsa_wond.pub
```

## 将公钥添加到github网站上

![image-20230424001723152](https://muyids.oss-cn-beijing.aliyuncs.com/img/image-20230424001723152.png)

## 配置 `config` 文件

编辑 `~/.ssh/config` 文件，如果没有就新建一个。内容如下：
 这里就用到了前面定义的标识符。
```jsx
Host muyids.github.com                 
    HostName github.com
    IdentityFile /Users/mac/.ssh/id_rsa
    PreferredAuthentications publickey
    User muyids
Host wonderfulest.github.com                 
    HostName github.com
    IdentityFile /Users/mac/.ssh/id_rsa_wond
    PreferredAuthentications publickey
    User wonderfulest
    
```

## 测试连接

```dart
// 测试第一个账号
ssh -T git@muyids.github.com     
// 测试第二个账号
ssh -T git@wonderfulest.github.com  
```
如果连接成功能看到以下输出：

```rust
Hi xxx！ You've successfully authenticated.but GitHub does not provide shell acess
```

即使ssh config中的文件路径配置错误，ssh -T也会通过，所以路径一定要自己检查清楚。

## 开心的使用

注意地址的变化，之前是

```bash
git clone git@muyids.github.com:xxx/yyyy.git
```

地址的 `github.com`需要被自定义的标识符替换掉，比如第一个账户是 muyids，那么命令就是

```ruby
git clone git@muyids.github.com:xxx/yyyy.git
```

clone到本地后，可以使用 `git remote -v` 查看远程地址，就是"git@muyids.github.com:xxx/yyyy.git"

## 参考

- [mac os 配置两个github账号](https://www.jianshu.com/p/48413e033de4)

---

