### F2.2.1

wslg还是太好用了，可以直接在windows上运行linux的GUI程序
我使用nixos，运行nix-shell -p logisim可以直接创建一个包含该软件所有依赖的shell

### F2.3.2

思考了一下，决定从现在开始使用git仓库记录学习过程
我计划使用nix的flake来管理所有依赖，使得环境具有可复现性

保存文件后，发现circ文件其实是一个xml文档

### F2.3.3

似乎是由于版本不同，内嵌的文档没有The graphical interfaces，但Menu reference还是有的

### F2.3.4

tutorial里用的输入是pin，按下后反转电平，分类在Wiring library
button则是按下为1，松开为0，分类在Input/Output library

Dip Switch似乎没有，可能是版本问题

LED，文档中描述：和输出pin没什么不同，除了好看一点XD
7-Segment Display，经典的7段数码管，经过测试，高电平点亮，是共阴极的（但我估计软件根本不考虑这个）

### F2.3.5

准被做一个简单的流水灯

核心是一个2bit timer

先画真值表
a: Q1
b: Q0
c: NQ1
d: NQ0

ab cd
00 01
01 10
10 11
11 00

然后列出表达式并化简
c=a'b+ab' 使用xor
d=a'b'+ab'= b' 一个非门（直接用D触发反向端也可以）
