#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试在pytdx项目中集成的mootdx和tdxpy功能
"""

import sys
import os

# 添加当前目录到Python路径，以便导入mootdx和tdxpy
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def test_mootdx_import():
    """测试mootdx导入"""
    print("🧪 测试mootdx导入...")
    try:
        import mootdx
        print(f"✅ mootdx导入成功，版本: {mootdx.__version__}")
        print(f"   位置: {mootdx.__file__}")
        return True
    except ImportError as e:
        print(f"❌ mootdx导入失败: {e}")
        return False

def test_tdxpy_import():
    """测试tdxpy导入"""
    print("\n🧪 测试tdxpy导入...")
    try:
        import tdxpy
        print(f"✅ tdxpy导入成功")
        print(f"   位置: {tdxpy.__file__}")
        return True
    except ImportError as e:
        print(f"❌ tdxpy导入失败: {e}")
        return False

def test_mootdx_functionality():
    """测试mootdx基本功能"""
    print("\n🧪 测试mootdx基本功能...")
    try:
        from mootdx import consts
        print(f"✅ consts模块导入成功")
        print(f"   可用市场: {[attr for attr in dir(consts) if 'MARKET' in attr]}")
        
        from mootdx.quotes import Quotes
        print(f"✅ Quotes模块导入成功")
        
        return True
    except Exception as e:
        print(f"❌ mootdx功能测试失败: {e}")
        return False

def test_tdxpy_functionality():
    """测试tdxpy基本功能"""
    print("\n🧪 测试tdxpy基本功能...")
    try:
        from tdxpy.hq import TdxHq_API
        print(f"✅ TdxHq_API导入成功")
        
        from tdxpy.exhq import TdxExHq_API
        print(f"✅ TdxExHq_API导入成功")
        
        return True
    except Exception as e:
        print(f"❌ tdxpy功能测试失败: {e}")
        return False

def test_integration():
    """集成测试"""
    print("\n🧪 集成测试：同时使用pytdx、mootdx和tdxpy...")
    try:
        # 导入pytdx
        from pytdx.hq import TdxHq_API as PytdxHqAPI
        print("✅ pytdx.hq导入成功")
        
        # 导入mootdx
        from mootdx.quotes import Quotes
        print("✅ mootdx.quotes导入成功")
        
        # 导入tdxpy
        from tdxpy.hq import TdxHq_API as TdxpyHqAPI
        print("✅ tdxpy.hq导入成功")
        
        print("✅ 三个包可以同时使用！")
        return True
    except Exception as e:
        print(f"❌ 集成测试失败: {e}")
        return False

def main():
    """主测试函数"""
    print("=" * 60)
    print("🚀 pytdx项目中的mootdx和tdxpy集成测试")
    print("=" * 60)
    
    results = []
    results.append(test_mootdx_import())
    results.append(test_tdxpy_import())
    results.append(test_mootdx_functionality())
    results.append(test_tdxpy_functionality())
    results.append(test_integration())
    
    print("\n" + "=" * 60)
    print("📊 测试结果汇总:")
    print(f"   通过: {sum(results)}/{len(results)}")
    print(f"   成功率: {sum(results)/len(results)*100:.1f}%")
    
    if all(results):
        print("🎉 所有测试通过！mootdx和tdxpy已成功集成到pytdx项目中")
    else:
        print("⚠️  部分测试失败，请检查依赖项")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
