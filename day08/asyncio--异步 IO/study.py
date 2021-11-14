import asyncio
import time
# 通过 async/await 语法进行声明，是编写 asyncio 应用的推荐方式。
# 例如，以下代码段（需要 Python 3.7+）会打印 "hello"，等待 1 秒，再打印 "world":
async  def main():
    print("hello")
    await asyncio.sleep(1)
    print('world')

asyncio.run(main())

