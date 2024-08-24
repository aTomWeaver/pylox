import sys
from os import path


types = {
        "Binary": "left: Expr, operator: Token, right: Expr",
        "Grouping": "expression: Expr",
        "Literal": "value",
        "Unary": "operator: Token, right: Expr",
        }


def assembleBoilerplate(class_name: str, params: str, base_class=""):
    TAB = "    "
    class_string = ""
    imports = []
    vars = ""
    if "Token" in params:
        imports.append("Token")
    if "value" in params:
        imports.append("Optional")
    if base_class:
        base_class = f"({base_class})"
    class_string += f"class {class_name}{base_class}:\n" \
        f"{TAB}def __init__(self, {params}):\n"
    for param in params.split(","):
        var = param.strip().split(":")[0]
        vars += f"{TAB}{TAB}self.{var} = {var}\n"
    class_string += vars
    return class_string, imports


def defineAst(output_dir: str, base_class: str, types: str):
    write_string = ""
    classes = []
    imports = set()
    filepath = path.join(output_dir, base_class + '.py')
    for class_name, params in types.items():
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

def defineVisitor(writer, basename, types):
    write_string = ""
    pass


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: generateAst [directory]")
        sys.exit(64)

    output_dir = args[0]
    defineAst(output_dir, "Expr", types)
