from setuptools import setup, find_packages

setup(name='hawksoft',
      version='0.1.1',
      #packages=['zhihu_hawksoft'],
      #py_modules=["my_module"], # 单文件模块写法
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # 多文件模块写法
      author="xingyongkang",
      author_email="xingyongkang@cqu.edu.cn",
      description="convert md file including latex formula to zhihui website docs",
      long_description="convert md file including latex formula to zhihui website docs",
      license="MIT",
      url="https://github.com/xingyongkang/md2zhihu",
      entry_points={
          'console_scripts': [
              'md2zhihu=hawksoft.zhihu.main:main'
          ]
      },
)