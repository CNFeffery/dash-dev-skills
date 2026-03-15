import json
import feffery_utils_components as fuc

# fuc组件名称列表
fuc_component_names = [
    component_name
    for component_name in dir(fuc)
    if hasattr(getattr(fuc, component_name), "to_plotly_json")
]

print(json.dumps(fuc_component_names, ensure_ascii=False, indent=4))
