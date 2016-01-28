#git 简介

```
分布式的版本控制系统
强大的分支功能
```
#git设置

```
安装完成之后，进行设置 在命令行中输入：
 git config --global user.name "your name"
 git config --global user.email "name@example.com"
```
#基本流程

```
git init 
git add  把文件添加到缓存区，
git commit -m ""把暂存区的内容提交到当前分支
git status
git diff 查看修改了但是没有git add的文件
git log 查看从近到远的提交日志 HEAD表示当前版本，HEAD^表示上一个版本
git reset --hard commi-id 用来表示回到们哥版本
git reflog可以查看命令历史，以便确定要回到未来的哪个版本
```

#管理修改

```
git checkout -- filename （一定要有两个－）把文件在工作区的修改全部撤销，这里有两种情况：1.文件修改后没有放入暂存区，现在撤销修改就是将文件恢复到和版本库一模一样的状态 2. 文件修改后放入暂存区，又做了修改，撤销修改就会到添加暂存区后的状态，  总之，就是让文件回到最近一次git commit 或git add时的状态
git reset HEAD filename 当文件修改了之后，并且提交到了暂存区，调用此命令可以将暂存区的修改撤销，重新放回工作区，如果要将工作区的修改撤销，就需要使用命令 git checkout -- filename
场景1： 当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令 git checkout --file
场景2:  当你不但更改了某个文件的内容，还添加到了暂存区，想丢弃修改，分两步，第一步用命令 git reset HEAD file第二步 按照场景1操作
场景3: 当你提交了不合适的修改到版本库时，想要撤销本次提交，就可以版本回退
```

#删除文件

```
要删除版本库中的文件：1. rm filename 2. git rm filename 3. git commit 
如果文件删除错误，想要恢复文件，可以使用git checkout -- filename 进行文件恢复，十几上就是将版本库中的版本替换工作区的文件，不管工作区是修改还是删除，都可以恢复
```

# 分支
**git branch**:查看分支
**git branch name**: 创建分支
**git checkout name**: 切换分支
**git checkout -b name**:创建分支并且切换分支
**git merge name** 合并分支到当前分支
**git branch -d name**:删除分支
#远程分支
**传输协议：**
1. ssh
2. https速度慢，并且每次都必须输入口令

```
1. 由于本地分支和github之间使用过ssh加密进行通信的，1.在本地生成密钥，在用户主目录下，有个.ssh目录，生成 SSH KEY： **ssh-keygen -t rsa -C 'youremail@example.com'** 2.将公钥id_rsa.pub放入到github上的，
2. git remote add origin git@github.com:youraccount/learn.git  将origin绑定到一个远程库上
3. git clone git@github.com:youraccount/learn.git 克隆远程库到本地
```

