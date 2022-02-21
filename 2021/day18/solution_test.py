from .solution import build_node_tree, Node


# def test_node_builder():
#     print(build_node_tree("[[0,1],[[2,2],[2,2]]]"))
#
# def test_explode_1():
#     tree = build_node_tree("[[[[[9,8],1],2],3],4]")
#     print(tree)
#     tree.reduce()
#     assert str(tree) == "[[[[0, 9], 2], 3], 4]"
#
#
# def test_explode_2():
#     tree = build_node_tree("[7,[6,[5,[4,[3,2]]]]]")
#     print(tree)
#     tree.reduce()
#     assert str(tree) == "[7, [6, [5, [7, 0]]]]"
#
#
# def test_explode_3():
#     tree = build_node_tree("[[6,[5,[4,[3,2]]]],1]")
#     print(tree)
#     tree.reduce()
#     assert str(tree) == "[[6, [5, [7, 0]]], 3]"
#
# def test_explode_and_split_1():
#     tree = build_node_tree("[[[[4,3],4],4],[7,[[8,4],9]]]")
#     tree = tree.add(Node(None, [1,1]))
#     tree.reduce()
#     while tree.has_changed():
#         tree.reset()
#         tree.reduce()
#     assert str(tree) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
