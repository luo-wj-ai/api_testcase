## 一、目录树

```
📁 接口自动化目录树-cloudsystem_test/
    ├── 📁 common/  # 公共模块，存放项目中通用的配置和工具
    │   ├── 📄 Adata.py  # 存储反向订购请求参数数据
    │   ├── 📄 Aheaders.py  # 存储请求头信息，包括授权和内容类型
    │   ├── 📄 Aurl.py  # 存储接口的 URL 地址
    │   └── 📄 Bthirdheader.py  # 生成第三方接口请求头的签名
    ├── 📁 config/  # 配置模块，存放项目配置文件和工具
    │   ├── 📄 Ahandle.py  # 包含验证 token 是否失效的辅助函数
    │   ├── 📄 Amobile.py  # 生成随机手机号码的工具
    │   ├── 📄 Border.py  # 包含订购相关的测试方法
    │   ├── 📄 clear_allure_results.py  # 清理 Allure 报告旧数据的脚本
    │   ├── 📄 dataportal.py  # 操作平台相关的 YAML 数据
    │   ├── 📄 deskfile.py  # 操作订购相关的 YAML 数据
    │   ├── 📄 stockdata.py  # 操作运营编排相关的 YAML 数据
    │   ├── 📄 存储token值.py  # 存储和读取 token 值
    │   ├── 📄 存储现网token值.py  # 存储和读取现网环境的 token 值
    │   └── 📄 请求头签名.py  # 生成请求头的签名
    ├── 📁 report/  # 测试报告目录，存放生成的测试报告
    ├── 📄 conftest.py  # pytest 的 fixture 和全局配置文件
    ├── 📄 data.yaml  # 存储测试数据的 YAML 文件
    ├── 📄 datatoken.yaml  # 存储 token 数据的 YAML 文件
    ├── 📄 datatoken2.yaml  # 存储另一个 token 数据的 YAML 文件
    ├── 📄 dataweb.yaml  # 存储 Web 相关数据的 YAML 文件
    ├── 📄 test_all.py  # 运行所有测试用例的脚本
    ├── 📄 test_all01.py  # 另一个运行测试用例的脚本
    ├── 📁 test_case/  # 测试用例目录，存放具体的测试用例文件
    │   ├── 📄 data.yaml  # 测试用例相关的数据文件
    │   ├── 📄 datatoken.yaml  # 测试用例相关的 token 数据文件
    │   ├── 📄 datatoken2.yaml  # 测试用例相关的另一个 token 数据文件
    │   ├── 📄 dataweb.yaml  # 测试用例相关的 Web 数据文件
    │   ├── 📄 test_540Version.py  # 测试运营编排模块的接口
    │   ├── 📄 test_Ausermanagement.py  # 测试用户管理模块
    │   ├── 📄 test_Bproductmanagement.py  # 测试产品管理模块
    │   ├── 📄 test_Cmembercenter.py  # 测试会员中心模块
    │   ├── 📄 test_DOM.py  # 测试运营管理模块
    │   ├── 📄 test_Eadvertisement.py  # 测试 OS 运营管理模块
    │   └── 📄 test_order.py  # 测试订购模块
    └── 📁 test_data/  # 测试数据目录，存放测试用例所需的数据文件
        ├── 📄 data.yaml  # 存储测试数据的 YAML 文件
        ├── 📄 data_app.yaml  # 存储应用相关数据的 YAML 文件
        ├── 📄 datatoken.yaml  # 存储 token 数据的 YAML 文件
        ├── 📄 dataweb.yaml  # 存储 Web 相关数据的 YAML 文件
        └── 📄 select_data.yaml  # 存储选择性数据的 YAML 文件
```

## 二、运行脚本

```
运行接口测试，先cd进入cloudsystem_test目录
python test_all.py
运行UI测试，直接在api的目录即可
python -m unittest AcloudUI.test_case.test_usermanagement
```
## 其他
```
{fix}:修改BUG
{feat}:添加新功能
{docs}：文档编写
{style}：代码优化
{refactor}:代码重构
{chore}：需求变动，小更改

```