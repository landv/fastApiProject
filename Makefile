# 打包命令
# https://blog.csdn.net/weixin_41916986/article/details/122342035
# http://kmanong.top/kmn/qxw/form/article?id=11512&cate=56
# http://mrdoc.zmister.com/project-53/doc-1389/
# nuitka3 ./main.py --include-plugin-directory=./app --output-dir=./build -o ./build/main
# https://nuitka.net/doc/user-manual.html#command-line
# nuitka3 --follow-imports main.py
# nuitka3 --standalone --follow-import-to=app --nofollow-imports --show-progress main.py
# nuitka3 --onefile main.py
# nuitka3 打包速度慢，打包执行总出现错误。

#

# 全部编译
all:build
# pyinstaller 打包编译
build:
	# 使用pyinstaller 进行打包
	# 多文件
	# pyinstaller -D --hidden-import="main"  main.py
	# 单文件
	# pyinstaller -F --hidden-import="main"  main.py
	pyinstaller -F --hidden-import="main"  main.py
	upx ./dist/main
	mv ./dist/main ./dist/fastApiProject
#buildwin:
#	pyinstaller 无法交叉编译到windows
#	upx ./dist/main
#	mv ./dist/main ./dist/fastApiProject
clear:
	# 清理编译
	rm -rf ./build
	rm -rf ./dist
run:
	./dist/fastApiProject

reout:
	# pip的freeze命令用于生成将当前项目的pip类库列表生成 requirements.txt 文件
	pip freeze > requirements.txt
rein:
	# 安装依赖
	pip install -r requirements.txt
venv:
	# 创建虚拟环境
	virtualenv env
	#source env/bin/activate
rundev:
	# 运行
	python main.py

