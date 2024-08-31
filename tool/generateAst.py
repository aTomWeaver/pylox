import sys
from os import path


TAB = "    "
RETURN = "\n"
types = {
        "Expr": "",
        "Binary": "left: Expr, operator: Token, right: Expr",
        "Grouping": "expression: Expr",
        "Literal": "value",
        "Unary": "operator: Token, right: Expr",
        }


def assembleBoilerplate(class_name: str, params: str, base_class=""):
    class_string = ""
    imports = []
    vars = ""
    if "Token" in params:
        imports.append("Token")
    if "value" in params:
        imports.append("Optional")
    if base_class:
        base_class = f"({base_class})"
    class_string += f"class {class_name}{base_class}:\n"
    if params:
        class_string += f"{TAB}def __init__(self, {params}):\n"
        for param in params.split(","):
            var = param.strip().split(":")[0]
            vars += f"{TAB}{TAB}self.{var} = {var}\n"
        class_string += vars + RETURN
    class_string += defineVisitorAccept(class_name)
    return class_string, imports


def defineVisitorAccept(classname: str):
    write_string = ""
    if classname == "Expr":
        write_string += f"{TAB}def accept(self, visitor):{RETURN}"
        write_string += f"{TAB}{TAB}pass{RETURN}"
    else:
        write_string += f"{TAB}def accept(self, visitor):{RETURN}"
        write_string += f"{TAB}{TAB}return visitor.visit{classname}(self){RETURN}"
    return write_string


def defineAst(output_dir: str, base_class: str, types: dict):
    write_string = ""
    classes = []
    imports = set()
    filepath = path.join(output_dir, base_class + '.py')
    for class_name, params in types.items():
        if class_name == "Expr":
            class_string, class_imports = assembleBoilerplate(class_name, params)
        else:
            class_string, class_imports = assembleBoilerplate(class_name, params, base_class)
        classes.append(class_string)
        for item in class_imports:
            imports.add(item)
    for item in imports:
        if item == "Optional":
            write_string += "from typing import Optional\n"
        else:
            write_string += f"from {item.lower()} import {item}\n"
    write_string += "\n\n"
    for class_ in classes:
        write_string += class_ + "\n\n"
    with open(filepath, 'w') as file:
        file.writelines([write_string])

def defineVisitor(output_dir: str, base_class: str, types: dict):
    write_string = ""

    filepath = path.join(output_dir, base_class + '.py')
    with open(filepath, "w") as file:
        file.writelines([write_string])


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: generateAst [directory]")
        sys.exit(64)

    output_dir = args[0]
    defineAst(output_dir, "Expr", types)
