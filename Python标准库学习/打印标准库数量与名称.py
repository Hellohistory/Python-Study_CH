import sys

"""
遍历sys.modules中的所有模块，并检查是否具有__file__属性
因为某些内建模块或动态创建的模块没有__file__属性,所以我们可以在迭代之前检查__file__属性是否存在
"""

# 获取标准库模块名称
stdlib_modules = [module_name for module_name, module in sys.modules.items()
                  if hasattr(module, '__file__')
                  and module.__file__ is not None and 'site-packages' not in module.__file__]

print("Python标准库模块数量：", len(stdlib_modules))
print("Python标准库模块列表：")
for module_name in stdlib_modules:
    print(module_name)
