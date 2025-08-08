#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化的mootdx和tdxpy导入测试（不依赖pandas等包）
"""

import sys
import os

# 添加当前目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def test_basic_imports():
    """测试基本导入"""
    print("🧪 测试基本包导入...")
    
    # 测试pytdx
    try:
        import pytdx
        print(f"✅ pytdx导入成功")
        print(f"   位置: {pytdx.__file__}")
    except Exception as e:
        print(f"❌ pytdx导入失败: {e}")
    
    # 测试tdxpy
    try:
        import tdxpy
        print(f"✅ tdxpy导入成功")
        print(f"   位置: {tdxpy.__file__}")
    except Exception as e:
        print(f"❌ tdxpy导入失败: {e}")
    
    # 测试mootdx（只测试基本结构，不导入依赖pandas的模块）
    try:
        import importlib.util
        mootdx_path = os.path.join(current_dir, "mootdx", "__init__.py")
        if os.path.exists(mootdx_path):
            print(f"✅ mootdx包文件存在: {mootdx_path}")
            
            # 查看mootdx包结构
            mootdx_dir = os.path.join(current_dir, "mootdx")
            mootdx_files = [f for f in os.listdir(mootdx_dir) if f.endswith('.py')]
            print(f"   mootdx模块文件: {mootdx_files[:5]}...")  # 显示前5个
        else:
            print(f"❌ mootdx包文件不存在")
    except Exception as e:
        print(f"❌ mootdx检查失败: {e}")

def test_directory_structure():
    """测试目录结构"""
    print(f"\n📁 pytdx目录结构:")
    
    items = []
    for item in os.listdir(current_dir):
        if os.path.isdir(os.path.join(current_dir, item)):
            items.append(f"📂 {item}/")
        else:
            items.append(f"📄 {item}")
    
    for item in sorted(items):
        print(f"   {item}")

def test_mootdx_structure():
    """测试mootdx包结构"""
    print(f"\n📁 mootdx包结构:")
    
    mootdx_dir = os.path.join(current_dir, "mootdx")
    if os.path.exists(mootdx_dir):
        items = []
        for item in os.listdir(mootdx_dir):
            if os.path.isdir(os.path.join(mootdx_dir, item)):
                items.append(f"📂 {item}/")
            else:
                items.append(f"📄 {item}")
        
        for item in sorted(items):
            print(f"   {item}")
    else:
        print("   ❌ mootdx目录不存在")

def test_tdxpy_structure():
    """测试tdxpy包结构"""
    print(f"\n📁 tdxpy包结构:")
    
    tdxpy_dir = os.path.join(current_dir, "tdxpy")
    if os.path.exists(tdxpy_dir):
        items = []
        for item in os.listdir(tdxpy_dir):
            if os.path.isdir(os.path.join(tdxpy_dir, item)):
                items.append(f"📂 {item}/")
            else:
                items.append(f"📄 {item}")
        
        for item in sorted(items):
            print(f"   {item}")
    else:
        print("   ❌ tdxpy目录不存在")

def main():
    """主函数"""
    print("=" * 60)
    print("🔍 pytdx项目中的mootdx和tdxpy包集成检查")
    print("=" * 60)
    
    test_basic_imports()
    test_directory_structure()
    test_mootdx_structure()
    test_tdxpy_structure()
    
    print("\n" + "=" * 60)
    print("✅ 包复制检查完成！")
    print("💡 注意：要运行mootdx功能需要安装pandas等依赖包")
    print("💡 建议：在虚拟环境中安装依赖后使用mootdx功能")
    print("=" * 60)

if __name__ == "__main__":
    main()
