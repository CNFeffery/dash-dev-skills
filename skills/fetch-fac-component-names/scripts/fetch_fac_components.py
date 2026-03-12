import json
import feffery_antd_components as fac

# fac组件名称列表
fac_component_names = [
    component_name
    for component_name in dir(fac)
    if hasattr(getattr(fac, component_name), "to_plotly_json")
]

print(json.dumps(fac_component_names, ensure_ascii=False, indent=4))
