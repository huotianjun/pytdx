# pytdx + mootdx + tdxpy 三合一集成

本目录现在包含了三个强大的通达信(TDX)数据接口库：

## 📦 包含的库

### 1. pytdx (原有)
- **描述**: 原始的Python通达信接口库
- **特点**: 轻量级、稳定、纯Python实现
- **适用**: 基础行情数据获取
- **位置**: `pytdx/`

### 2. mootdx (新增 - 从ali39移植)
- **描述**: 增强版通达信接口库
- **版本**: 0.9.11
- **特点**: 
  - 内置最佳IP选择功能
  - 丰富的财经数据接口
  - 命令行工具支持
  - 支持多种数据源
- **位置**: `mootdx/`
- **配置**: `mootdx-0.9.11.dist-info/`

### 3. tdxpy (新增 - mootdx依赖)
- **描述**: mootdx的底层实现库
- **版本**: 0.1.10
- **特点**: 
  - 扩展市场数据支持
  - 底层协议实现
  - 高性能数据处理
- **位置**: `tdxpy/`
- **配置**: `tdxpy-0.1.10.dist-info/`

## 🚀 快速开始

### 基本使用

```python
import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 使用pytdx
from pytdx.hq import TdxHq_API
api = TdxHq_API()

# 使用tdxpy
from tdxpy.hq import TdxHq_API as TdxpyHqAPI
tdxpy_api = TdxpyHqAPI()

# 使用mootdx (需要先安装依赖)
# from mootdx.quotes import Quotes
# client = Quotes.factory(market='std')
```

### mootdx最佳IP选择

```bash
# 需要先安装依赖
pip install pandas numpy tenacity click prettytable

# 运行最佳IP选择
python -m mootdx bestip -vv
```

## 📋 依赖要求

### pytdx
- 无外部依赖 ✅

### tdxpy  
- 基本功能无外部依赖 ✅
- 完整功能需要pandas ⚠️

### mootdx
- **必需依赖**:
  - pandas >= 1.0.0
  - numpy >= 1.18.0
  - tenacity >= 6.0.0
  - click >= 7.0
  - prettytable >= 2.0.0
  - requests >= 2.20.0

## 🔧 安装依赖

### 方法1: 使用requirements文件
```bash
pip install -r requirements_mootdx.txt
```

### 方法2: 手动安装
```bash
pip install pandas numpy tenacity click prettytable requests
```

### 方法3: 虚拟环境(推荐)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 venv\Scripts\activate  # Windows
pip install pandas numpy tenacity click prettytable requests
```

## 📊 使用场景建议

| 场景 | 推荐库 | 原因 |
|------|--------|------|
| 基础行情获取 | pytdx | 轻量级，稳定可靠 |
| 扩展市场数据 | tdxpy | 支持扩展行情接口 |
| 自动服务器选择 | mootdx | 内置bestip功能 |
| 财经数据分析 | mootdx + pytdx | 互补优势 |
| 高并发场景 | pytdx + 连接池 | 性能稳定 |

## 🧪 测试脚本

- `test_package_structure.py` - 检查包结构和基本导入
- `demo_integration.py` - 三合一集成演示
- `test_mootdx_integration.py` - mootdx功能测试(需要依赖)

## ⚠️  注意事项

1. **依赖管理**: mootdx需要pandas等重型依赖，建议在虚拟环境中使用
2. **API差异**: 三个库的API可能略有不同，使用时请查阅相应文档
3. **性能考虑**: 根据实际需求选择合适的库
4. **生产环境**: 建议统一依赖管理和版本控制

## 📚 相关资源

- **pytdx**: 原项目文档和示例
- **mootdx**: 命令行工具 `python -m mootdx --help`
- **tdxpy**: 底层API参考

## 🎯 成功指标

- ✅ 三个库成功集成到同一项目
- ✅ 包结构完整，文件完备
- ✅ 基础导入测试通过
- ✅ 提供了使用示例和文档
- ⏳ mootdx功能测试(待安装依赖)

---

**集成完成时间**: 2025年8月8日  
**来源**: ali39主机 (39.107.244.110)  
**集成状态**: ✅ 成功
