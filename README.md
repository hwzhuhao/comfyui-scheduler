# comfyui-scheduler

### 介绍
comfyui-scheduler是基于ComfyUI_Lam做了轻量化裁剪适配改造开发的插件，主要用于支持comfyui多实例并发调度

#### 使用说明
下载插件放到comfyUI的插件目录，并执行相关脚本进行安装部署
1.cd ComfyUI/custom_nodes
2.git clone https://github.com/hwzhuhao/comfyui-scheduler.git
3.pip install -r requirement.txt
4.执行change.sh文件，未报错后就可以了
5.修改config/config.yaml中的redis配置
6.停止原有ComfyUI服务，使用新的配置参数进行启动，指定使用的gpu节点和主节点服务，如下：
```shell
python main.py --cuda-device 0 --listen 0.0.0.0 --port 9999 --cluster --isMain --basePath=comfyui0000 #主
python main.py --cuda-device 1 --listen 0.0.0.0 --port 9988 --cluster --basePath=comfyui0001
```