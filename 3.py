# class BuildingError(Exception):
#     def __str__(self):
#         return(f'with that much material the house cannot be built')
#
# def check_material(material, limit_material):
#     if material > limit_material:
#         return "enough material"
#     else:
#         raise BuildingError(material)
#
# material = 500
# print(check_material(material, 300))

# import sys
# print(sys.executable)
# print(sys.version)
# print(sys.platform)
# print(sys.modules)
# for name, module_path in sys.modules.items():
#     print(name, module_path)

# for _ in dir(__builtins__):
#     print(_)

