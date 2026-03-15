import argparse
import sys
import feffery_utils_components as fuc

def main():
    parser = argparse.ArgumentParser(description="获取 feffery-utils-components 组件的参数说明文档。")
    parser.add_argument("component_name", type=str, help="需要查询的组件名称，如 FefferyDiv")
    
    args = parser.parse_args()
    component_name = args.component_name

    # 检查组件是否存在并且合法
    if not hasattr(fuc, component_name) or not hasattr(getattr(fuc, component_name), "to_plotly_json"):
        print(f"⚠️ 警告: 找不到合法的 feffery-utils-components 组件 '{component_name}'。")
        print("请检查组件名称拼写是否正确，或使用 fetch-fuc-component-names 技能获取所有有效组件列表。")
        sys.exit(1)

    # 获取组件名的 __doc__ 参数文档
    doc_content = getattr(fuc, component_name).__doc__
    
    if not doc_content:
        print(f"⚠️ 警告: 组件 '{component_name}' 存在，但没有相关的参数文档。")
        sys.exit(1)

    print(doc_content)

if __name__ == "__main__":
    main()
