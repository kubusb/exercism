def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")
    
    def build_tree(pre_start, pre_end, in_start, in_end):
        if pre_start > pre_end or in_start > in_end:
            return {}
        
        root_value = preorder[pre_start]
        tree = {"v": root_value, "l": {}, "r": {}}
        
        in_root = inorder_map[root_value]
        left_size = in_root - in_start
        
        tree["l"] = build_tree(pre_start + 1, pre_start + left_size, 
                               in_start, in_root - 1)
        tree["r"] = build_tree(pre_start + left_size + 1, pre_end, 
                               in_root + 1, in_end)
        
        return tree
    
    if not preorder:
        return {}
    
    inorder_map = {val: idx for idx, val in enumerate(inorder)}
    return build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)
# Example usage
if __name__ == "__main__":
    preorder = ['a', 'i', 'x', 'f', 'r']
    inorder = ['i', 'a', 'f', 'x', 'r']
    try:
        result = tree_from_traversals(preorder, inorder)
        print("Reconstructed tree:")
        print(result)
    except ValueError as e:
        print(f"Error: {e}")