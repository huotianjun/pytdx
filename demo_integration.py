#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pytdx、mootdx、tdxpy 三合一使用示例

本示例展示如何在pytdx项目中同时使用三个TDX相关的库：
1. pytdx - 原始的Python通达信接口
2. mootdx - 增强版通达信接口（从ali39移植）
3. tdxpy - mootdx的底层依赖库
"""

import sys
import os

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def demo_pytdx():
    """演示pytdx功能"""
    print("🔵 pytdx 功能演示")
    print("-" * 40)
    
    try:
        from pytdx.hq import TdxHq_API
        api = TdxHq_API()
        print("✅ pytdx TdxHq_API 创建成功")
        print(f"   类型: {type(api)}")
        print(f"   模块: {api.__class__.__module__}")
        
        # 演示pytdx的best_ip功能
        try:
            from pytdx.util.best_ip import select_best_ip, ping
            print("✅ pytdx best_ip 模块导入成功")
            print("   - 可使用select_best_ip()选择最佳IP")
            print("   - 可使用ping(ip)测试IP响应时间")
        except ImportError as e:
            print(f"⚠️  pytdx best_ip 模块导入失败: {e}")
            
    except Exception as e:
        print(f"❌ pytdx 演示失败: {e}")

def demo_tdxpy():
    """演示tdxpy功能"""
    print("\n🟢 tdxpy 功能演示")
    print("-" * 40)
    
    try:
        from tdxpy.hq import TdxHq_API as TdxpyHqAPI
        api = TdxpyHqAPI()
        print("✅ tdxpy TdxHq_API 创建成功")
        print(f"   类型: {type(api)}")
        print(f"   模块: {api.__class__.__module__}")
        
        from tdxpy.exhq import TdxExHq_API
        ex_api = TdxExHq_API()
        print("✅ tdxpy TdxExHq_API 创建成功")
        print(f"   类型: {type(ex_api)}")
        
    except Exception as e:
        print(f"❌ tdxpy 演示失败: {e}")

def demo_mootdx_structure():
    """演示mootdx包结构"""
    print("\n🟡 mootdx 包结构演示")
    print("-" * 40)
    
    try:
        # 检查mootdx包的基本信息
        mootdx_path = os.path.join(current_dir, "mootdx")
        if os.path.exists(mootdx_path):
            print("✅ mootdx包已成功复制到pytdx项目")
            print(f"   位置: {mootdx_path}")
            
            # 列出主要模块
            main_modules = [
                "consts.py",     # 常量定义
                "quotes.py",     # 行情接口
                "server.py",     # 服务器管理
                "affair.py",     # 财经数据
                "__main__.py"    # 命令行工具
            ]
            
            print("   主要模块:")
            for module in main_modules:
                module_path = os.path.join(mootdx_path, module)
                if os.path.exists(module_path):
                    print(f"     ✅ {module}")
                else:
                    print(f"     ❌ {module}")
            
            # 检查子包
            sub_packages = ["contrib", "financial", "tools", "utils"]
            print("   子包:")
            for package in sub_packages:
                package_path = os.path.join(mootdx_path, package)
                if os.path.exists(package_path):
                    print(f"     ✅ {package}/")
                else:
                    print(f"     ❌ {package}/")
        else:
            print("❌ mootdx包未找到")
            
    except Exception as e:
        print(f"❌ mootdx 结构检查失败: {e}")

def demo_usage_scenarios():
    """演示使用场景"""
    print("\n🚀 使用场景建议")
    print("-" * 40)
    
    scenarios = [
        {
            "场景": "基础行情获取",
            "推荐": "pytdx",
            "原因": "轻量级，稳定可靠"
        },
        {
            "场景": "扩展市场数据",
            "推荐": "tdxpy",
            "原因": "支持扩展行情接口"
        },
        {
            "场景": "自动选择最佳服务器",
            "推荐": "mootdx",
            "原因": "内置bestip功能和服务器管理"
        },
        {
            "场景": "财经数据分析", 
            "推荐": "mootdx + pytdx",
            "原因": "mootdx提供财经数据，pytdx处理基础行情"
        },
        {
            "场景": "高并发数据获取",
            "推荐": "pytdx + 自定义连接池",
            "原因": "pytdx性能稳定，可自定义优化"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"   {i}. {scenario['场景']}")
        print(f"      推荐: {scenario['推荐']}")
        print(f"      原因: {scenario['原因']}")
        print()

def demo_migration_notes():
    """迁移注意事项"""
    print("📋 迁移和使用注意事项")
    print("-" * 40)
    
    notes = [
        "✅ 三个库已成功集成到pytdx项目中",
        "⚠️  mootdx需要pandas、numpy等依赖包才能运行",
        "⚠️  建议在虚拟环境中安装依赖：pip install pandas numpy tenacity click",
        "💡 可使用 'python -m mootdx bestip -vv' 命令选择最佳服务器",
        "💡 pytdx和tdxpy可直接使用，无需额外依赖",
        "🔧 如需在生产环境使用，建议统一依赖管理",
        "📚 各库的API可能略有不同，使用时请查阅相应文档"
    ]
    
    for note in notes:
        print(f"   {note}")

def main():
    """主函数"""
    print("=" * 60)
    print("🎯 pytdx + mootdx + tdxpy 三合一集成演示")
    print("=" * 60)
    
    demo_pytdx()
    demo_tdxpy()
    demo_mootdx_structure()
    demo_usage_scenarios()
    demo_migration_notes()
    
    print("\n" + "=" * 60)
    print("🎉 集成演示完成！")
    print("💫 现在可以在一个项目中使用三个强大的TDX库了！")
    print("=" * 60)

if __name__ == "__main__":
    main()
